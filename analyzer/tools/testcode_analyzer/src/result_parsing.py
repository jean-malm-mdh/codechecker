import os.path
import typing
import plistlib


class SourceLocation:
    def __init__(self, startL, startC, endL, endC):
        self.start_line = startL


class Report:
    def __init__(self, check, location):
        self.check_name = check
        self.location = location



class ResultReport:
    def __init__(self):
        self.report_amount = 0
        self.files = []
        self.reports = []


def report_from_plist(plist_report):
    check_name = plist_report['check_name']
    location = (plist_report['location']['file'],
                plist_report['location']['line'],
                plist_report['location']['col'])
    return Report(check_name, location)

def parse_result_file(result_file: str):
    """Parses a result file, returns information relevant to the test analyzer"""
    if not os.path.exists(result_file):
        return None

    result = ResultReport()
    parsed_file = None
    with open(result_file, 'rb') as fp:
        parsed_file = plistlib.load(fp)
    result.report_amount = len(parsed_file['diagnostics'])
    result.files = parsed_file['files']
    reports = parsed_file['diagnostics']
    result.reports = list(map(report_from_plist, reports))

    return result


def get_code_from_file(file, startrow, startcol, endrow, endcol):
    """Returns the code as defined by a file and [(startrow, startcol), (endrow, endcol)] interval"""
    return ''


def assertion_is_in_code(code_string: str):
    code_string_lower = code_string.lower()
    return


def raised_on_assertion(warning_data):
    """Returns true if the analyzer considers the warning to be raised on an assertion"""
