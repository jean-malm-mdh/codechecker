from tools.report_converter.codechecker_report_converter.report import Report
from tools.report_converter.codechecker_report_converter.report.report_file import get_reports
from typing import List


def reports_from_file(file):
    return get_reports(file)


def get_codeline_for_warning(report):
    return report.file.get_line(report.line)

def get_bugpath(report):
    # Go through each bugevent
    # put into file, line, col map the related info
    # return result (in order, how?)
    return [1,2,3]
