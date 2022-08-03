import os.path
import typing
import plistlib
import sys
sys.path.append('')

#TODO: This file has a lot of info ~/codechecker/tools/report-converter/codechecker_report_converter/report/__init__.py
class Location:
    def __init__(self, fileID: int, row: int, col: int):
        self.line = row
        self.col = col
        self.file_id = fileID

    def __eq__(self, other):
        if isinstance(other, Location):
            return self.line == other.line \
                   and self.col == other.col \
                   and self.file_id == other.file_id
        else:
            return self == other


class SourceRange:
    def __init__(self, start: Location, end: Location):
        assert start.file_id == end.file_id
        self.startLoc = start
        self.endLoc = end
        self.fileID = start.file_id

    def __init__(self, loc: Location):
        self.__init__(loc, loc)


class Report:
    def __init__(self, check, location):
        self.check_name = check
        self.location = location
        self.bug_path = []


class ResultReport:
    def __init__(self):
        self.report_amount = 0
        self.files = []
        self.reports = []


class Edge:
    def __init__(self, edgeFrom, edgeTo):
        self.edge_from = edgeFrom
        self.edge_to = edgeTo


def report_from_plist(plist_report):
    def loc_of_plist(_loc):
        return Location(_loc['file'],
                        _loc['line'],
                        _loc['col'])

    def bugpath_from_plist(path_elem):
        edge = path_elem['edges'][0]
        start = edge['start']
        end = edge['end']
        range = Edge(SourceRange(loc_of_plist(start[0]),
                                 loc_of_plist(start[1])),
                     SourceRange(loc_of_plist(end[0]),
                                 loc_of_plist(end[1])))
        return

    check_name = plist_report['check_name']
    loc = plist_report['location']
    bugpath = plist_report['path']
    bugpath_list = list(map(bugpath_from_plist, bugpath))
    location = loc_of_plist(loc)
    res = Report(check_name, location)
    res.bug_path = bugpath_list
    return res


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
    raise NotImplementedError('TBD')


def assertion_is_in_code(code_string: str):
    raise NotImplementedError('TBD')


def raised_on_assertion(warning_data):
    """Returns true if the analyzer considers the warning to be raised on an assertion"""
    raise NotImplementedError('TBD')
