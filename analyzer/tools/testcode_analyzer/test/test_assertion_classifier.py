import pytest
from ..src.result_parsing import parse_result_file, raised_on_assertion, ResultReport, Location


def test_parse_plist_result_missing_file():
    """[Negative]: Does function handle invalid files"""
    invalid_file = parse_result_file('./testdata/not_a_valid_file.plist')
    assert invalid_file is None

def test_parse_plist_result_existing():
    result = parse_result_file('./testdata/has_assertion.plist')
    assert result is not None
    assert isinstance(result, ResultReport)

def test_plist_report_data():
    result = parse_result_file('./testdata/has_one_report.plist')
    assert result.report_amount == 1
    assert result.files == ['./testdata/has_assertion.cpp']


def test_plist_report_diagnostics():
    result = parse_result_file('./testdata/has_one_report.plist')
    first_report = result.reports[0]
    ROW_NR = 238
    COL_NR = 3
    expected_loc = Location(0, ROW_NR, COL_NR)
    assert first_report.check_name == 'core.NullDereference'
    assert first_report.location == expected_loc
    assert result.files[first_report.location.file_id] == './testdata/has_assertion.cpp'

