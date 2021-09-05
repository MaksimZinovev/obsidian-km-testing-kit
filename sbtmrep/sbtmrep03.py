# This update adds ability to generate xlsx spreadsheet with columns in report: date, feature, duration, charter
import argparse
import datetime
import re
import sys
import frontmatter
import yaml
import os
import xlsxwriter
from collections import namedtuple
from datetime import datetime
from datetime import date

from pprint import pprint

FEATURES_PATH = "/Users/maksim/repos/obsidian-km-testing-kit/features"
SESSIONS_PATH = "/Users/maksim/repos/obsidian-km-testing-kit/sessions"
REPORTS_PATH = "/Users/maksim/repos/obsidian-km-testing-kit/reports"

Record = namedtuple("Record", "charter date_time")
SUPPORTED_TIME_FORMAT = r"(?P<hours>[0-2][0-9])[-:.\/](?P<mins>[0-5]\d)"


def md_files(path: str):
    """Get all md files in specified path """
    if not os.path.exists(path):
        print(f"No such folder: {path}")
    else:
        for root, dirs, files in os.walk(path):
            for file in files:
                if file.endswith(".md"):
                    yield file


def parse_time(time):
    """Pass default time 00:00 if format is invalid or not string.
    For some reason frontmatter package parses colon separated time as integers '19:33' is 1173 """
    if isinstance(time, str):
        match = re.match(SUPPORTED_TIME_FORMAT, time)
        if match:
            print(f"Hours: {match.group('hours')}, mins: {match.group('mins')}")
            return match.group('hours'), match.group('mins')
    print(f"Invalid or not supported time format: {time}. Passing default time '00:00'")
    return "00", "00"


def frontmatter_match(query: dict, session_file):
    """Verify that frontmatter contains all values in query (args from command line input)"""
    submitted_args = (k for k in query.keys() if query.get(k))
    print(f"submitted_args : {list(submitted_args)}")
    with open(SESSIONS_PATH + "/" + session_file, encoding="utf-8") as f:
        try:
            fm = frontmatter.load(f)
            for key in submitted_args:
                fm_value = fm.get(key)
                if not isinstance(fm_value, list):
                    fm_value = [str(fm.get(key))]
                else:
                    fm_value = [str(i) for i in fm_value]
                print(fm_value)
                if not query.get(key) in fm_value:
                    return False, fm
                else:
                    continue
        except yaml.YAMLError as e:
            print(f"Error processing file: {SESSIONS_PATH}/{session_file}, {e}")
        except KeyError as e:
            print(f"No such key in args: {query}, {e}")
    return True, fm


def sessions_report(query: dict):
    """ Make a list of sessions for daily report: charter extracted from markdown frontmatter + markdown link. Select
    only files that have today's (or specified) date in filename.
    """
    items = []
    for session_file in md_files(SESSIONS_PATH):
        try:
            # pprint(fm.metadata)
            match, fm = frontmatter_match(query, session_file)
            if not match:
                continue
            else:
                fm_charter = fm.get("charter") or "No charter"
                fm_created = fm.get("created").strftime('%Y-%m-%d') if fm.get("created") else "1900-01-01"
                hr, mins = parse_time(fm.get("start"))
                fm_start = hr+mins
                record = Record(
                    charter=f" - [x] {fm_charter} [{session_file}](../../sessions/{session_file})",
                    date_time=datetime.strptime(fm_created + " " + fm_start, '%Y-%m-%d %H%M'))
                items.append(record)
        except yaml.YAMLError as e:
            print(f"Error processing file: {SESSIONS_PATH}/{session_file}, {e}")
    return "Sessions:\n" + "\n".join((rec.charter for rec in sorted(items, key=lambda item: item.date_time)))


def write_log(content: str, file_name: str):
    """Write content in .md file"""
    if not os.path.exists(REPORTS_PATH):
        print(f"No such folder: {REPORTS_PATH}")
    else:
        file_path = REPORTS_PATH + "/" + file_name
        try:
            with open(file_path, "w", encoding="utf-8") as f:
                f.write(content)
                print(file_path)
        except IOError as e:
            print(f"Error writing into file:{file_path}, {e}")


def check_arg(args=None):
    """Parse arguments"""
    parser = argparse.ArgumentParser(description='Script to learn basic argparse')
    parser.add_argument('-C', '--created',
                        help='generate report for specified date (YYYY-MM-DD), e.g. python sbtmrep.py -D 2021-07-02',
                        required=False,
                        )
    # default=datetime.today().strftime('%Y-%m-%d')
    parser.add_argument('-F', '--features',
                        help='generate report for specified feature, e.g. python sbtmrep.py -F review-documents',
                        default='')

    results = parser.parse_args(args)
    pprint(vars(results))
    return vars(results)


def make_report():
    """Generate report depending on args specified by user"""
    date, feature = check_arg(sys.argv[1:])
    print('date =', date)
    print('feature =', feature)
    return sessions_report(date) if not feature else sessions_report(feature)


def write_report():
    """Write report depending on args specified by user"""
    query = check_arg(sys.argv[1:])
    created = query.get('created') or datetime.today().strftime('%Y-%m-%d')
    # print('date =', date)
    # print('feature =', feature)
    # pass dictionary with singla pair e.g.  date:[2021-08-01] or feature: [supplier-workflows]
    write_log(sessions_report(query), f"sessions.{created}.md")


def sessions_report_spreadsheet(query: dict):
    """ Make a list of sessions for daily report: charter extracted from markdown frontmatter + markdown link. Select
    only files that have today's (or specified) date in filename.
    """
    sessions = []
    for session_file in md_files(SESSIONS_PATH):
        # pprint(fm.metadata)
        match, fm = frontmatter_match(query, session_file)
        if not match:
            continue
        else:
            sessions.append(fm.to_dict())
    # print(f"sessions: {sessions}")
    return sessions


def split_sessions(_sessions: list):
    """ Split sessions with multiple features in metadata. Where "features" field includes multiple features
     duration is evenly split between  all features. This will allow to account time per feature.
      Also make sure all "features" fields are strings and not lists """
    sessions = []
    for session in _sessions:
        if session.get("features"):
            if isinstance(session.get("features"), list) and session.get("duration"):
                    for feature in session.get("features"):
                        sessions.append(session.copy())
                        sessions[-1]["duration"] = session.get("duration")//len(session.get("features"))
                        # print(f'split duration: {session.get("duration")//len(session.get("features"))}, feature: {feature}')
                        # print(f'sessions[-1]["duration"]: {sessions[-1]["duration"]} ')
                        sessions[-1]["features"] = feature
            else:
                sessions.append(session)
        else:
            sessions.append(session)
    # pprint(sessions)
    return sessions


def split_sessions_ref(_sessions: list):
    """ Split sessions with multiple features in metadata. Where "features" field includes multiple features
     duration is evenly split between  all features. This will allow to account time per feature.
      Also make sure all "features" fields are strings and not lists """
    sessions = []
    for session in _sessions:
        features = session.get("features")
        duration = session.get("duration")
        if features:
            features = features if isinstance(features, list) else [features]
            for feature in features:
                sessions.append(session.copy())
                sessions[-1]["features"] = feature
                sessions[-1]["duration"] = duration//len(features) if duration else 0
                # print(f'split duration: {session.get("duration")//len(session.get("features"))}, feature: {feature}')
                # print(f'sessions[-1]["duration"]: {sessions[-1]["duration"]} ')
        else:
            sessions.append(session)
    # pprint(sessions)
    return sessions


def get_timestamp(fm_created: datetime.date, fm_start: str) -> int:
    hours, mins = parse_time(fm_start)
    dt = datetime.combine(fm_created or date(2000,1,1),
                          datetime.strptime(hours + mins, "%H%M").time())
    return int(dt.timestamp())


def create_spreadsheet(sessions: list):
    """Generate spreadsheet for sessions dates and charters"""
    workbook = xlsxwriter.Workbook(f'{REPORTS_PATH}/report.xlsx')
    worksheet = workbook.add_worksheet("sessions")

    worksheet.write('A1', 'created')
    worksheet.write('B1', 'timestamp')
    worksheet.write('C1', 'session')
    worksheet.write('D1', 'module')
    worksheet.write('E1', 'features')
    worksheet.write('F1', 'duration')
    worksheet.write('G1', 'charter')

    sessions_sorted = sorted(sessions, key=lambda session: get_timestamp(session.get('created'), session.get('start')))
    for num, _ in enumerate(sessions_sorted):
        print(f"\nnum: {num},  date: {sessions_sorted[num].get('created')}, session: {sessions_sorted[num].get('session')}, duration: {sessions_sorted[num].get('duration')},  charter: {sessions_sorted[num].get('charter')}")
        hours, mins = parse_time((sessions_sorted[num].get('start')))
        print(f"start: {hours}-{mins}")
        worksheet.write(f'A{num+2}', str(sessions_sorted[num].get('created')))
        timestamp = get_timestamp(sessions_sorted[num].get('created'), sessions_sorted[num].get('start'))
        worksheet.write(f'B{num+2}', timestamp)
        worksheet.write(f'C{num+2}', str(sessions_sorted[num].get('session')))
        module = sessions_sorted[num].get('module') or ""
        worksheet.write(f'D{num+2}', str((module[0]) if isinstance(module, list) else (module or "")))
        worksheet.write(f'E{num+2}', str(sessions_sorted[num].get('features')))
        worksheet.write(f'F{num+2}', sessions_sorted[num].get('duration'))
        worksheet.write(f'G{num+2}', str(sessions_sorted[num].get('charter')))

    workbook.close()


# Main entry point
query = check_arg(sys.argv[1:])
# query = {'created': '2021-08-20', 'features': ''}
print(f"query: {query}")
sessions = sessions_report_spreadsheet(query)
sessions_per_feature = split_sessions_ref(sessions)
create_spreadsheet(sessions_per_feature)

