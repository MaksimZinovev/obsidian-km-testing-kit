# This update adds ability to generate lists of sessions for particular feature
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
    """Pass default time 00:00 if format is invalid"""
    if isinstance(time, str):
        match = re.match(SUPPORTED_TIME_FORMAT, time)
        if match:
            print(f"Hours: {match.group('hours')}, mins: {match.group('mins')}")
            return match.group('hours'), match.group('mins')
    print(f"Invalid or not supported time format: {time}. Passing default time '00:00'")
    return "00", "00"


def frontmatter_match(query: dict, session_file):
    """Verify that frontmatter contains all values in query (args from command)"""
    submitted_args = (k for k in query.keys() if query.get(k))
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


def create_spreadsheet():
    """Generate spreadsheet for sessions dates and charters"""
    workbook = xlsxwriter.Workbook('hello.xlsx')
    worksheet = workbook.add_worksheet()

    worksheet.write('A1', 'Hello world')

    workbook.close()


# Main entry point
write_report()



