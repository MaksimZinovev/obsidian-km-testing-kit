# This update adds support for different time formats

import datetime
import re
import sys
import frontmatter
import yaml
import os
from collections import namedtuple
from datetime import datetime
import argparse
from pprint import pprint

FEATURES_PATH = "/Users/maksim/repos/aerofiler-qa/features"
SESSIONS_PATH = "/Users/maksim/repos/aerofiler-qa/sessions"
REPORTS_PATH = "/Users/maksim/repos/aerofiler-qa/reports"

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


def daily_rep(report_date):
    """ Make a list of sessions for daily report: charter extracted from markdown frontmatter + markdown link. Select
    only files that have today's (or specified) date in filename.
    """
    items = []
    for session_file in md_files(SESSIONS_PATH):
        date = report_date if report_date else datetime.today().strftime('%Y-%m-%d')
        if date in session_file:
            try:
                with open(SESSIONS_PATH + "/" + session_file, encoding="utf-8") as f:
                    fm = frontmatter.load(f)
                    # pprint(fm.metadata)
                    fm_charter = fm.get("charter") if fm.get("charter") else "No charter"
                    fm_created = fm.get("created").strftime('%Y-%m-%d') if fm.get("created") else "1900-01-01"
                    hr, min = parse_time(fm.get("start"))
                    fm_start = hr+min
                    record = Record(
                        charter=f" - [x] {fm_charter} [{session_file}](../../sessions/{session_file})",
                        date_time=datetime.strptime(fm_created + " " + fm_start, '%Y-%m-%d %H%M'))
                    items.append(record)
            except yaml.YAMLError as e:
                print(f"Error processing file: {SESSIONS_PATH}/{session_file}, {e}")
    return "Sessions:\n" + "\n".join((rec.charter for rec in sorted(items, key=lambda item: item.date_time)))


def feature_rep(feature: str):
    """ Make a list of sessions for feature: charter extracted from markdown frontmatter + markdown link. Select only
    files which have specified feature name in filename.
    """
    items = []
    for session_file in md_files(SESSIONS_PATH):
        if feature in session_file:
            try:
                with open(SESSIONS_PATH + "/" + session_file, encoding="utf-8") as f:
                    fm = frontmatter.load(f)
                    fm_charter = fm.get("charter") if fm.get("charter") else "No charter"
                    list_item = f" - [x] {fm_charter} [{session_file}](../sessions/{session_file})"
                    # print(list_item)
                    items.append(list_item)
            except yaml.YAMLError as e:
                print(f"Error processing file: {SESSIONS_PATH}/{session_file}, {e}")
    return "Sessions:\n" + "\n".join(items)


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
    parser.add_argument('-D', '--date',
                        help='generate report for specified date, e.g. python sbtmrep.py -D 2021-07-02',
                        required=False,
                        default=datetime.today().strftime('%Y-%m-%d'))
    parser.add_argument('-F', '--feature',
                        help='generate report for specified feature, e.g. python sbtmrep.py -F review-documents',
                        default='')

    results = parser.parse_args(args)
    return (results.date,
            results.feature)
datetime.today().strftime('%Y-%m-%d')


def make_report():
    """Generate report depending on args specified by user"""
    date, feature = check_arg(sys.argv[1:])
    print('date =', date)
    print('feature =', feature)
    return daily_rep(date) if not feature else feature_rep(feature)


def write_report():
    """Write report depending on args specified by user"""
    date, feature = check_arg(sys.argv[1:])
    # print('date =', date)
    # print('feature =', feature)
    write_log(daily_rep(date), f"sessions.{date}.md") if not feature else write_log(feature_rep(feature),

                                                                                    f"sessions.{feature}.md")
# Main entry point
write_report()




