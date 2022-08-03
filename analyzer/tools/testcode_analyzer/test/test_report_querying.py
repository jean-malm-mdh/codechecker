import unittest
import sys
import os

sys.path.append(f"{os.getenv('HOME')}/codechecker/tools/report-converter")
from analyzer.tools.testcode_analyzer.src.analysis_report import reports_from_file, get_codeline_for_warning, get_bugpath

# TESTS TO CREATE
## Get all reports from file
## Get code from bug event
## Query report for bugevent content
### example: Last event (bug) was raised on assertion

class TestReportQuerying(unittest.TestCase):
    def test_CanGetAllReportsFromFile(self):
        reports = reports_from_file('./testdata/has_one_report.plist')
        self.assertEqual(1, len(reports))

    def test_CanRetrieveErrorLine(self):
        reports = reports_from_file('./testdata/has_one_report.plist')
        only_report = reports[0]
        self.assertEqual('  MOZ_RELEASE_ASSERT(TypedEnum(unsignedIntegerNewResult) == newResult);\n', get_codeline_for_warning(only_report))

    def test_CanGetBugEventGraph(self):
        reports = reports_from_file('./testdata/has_one_report.plist')
        bugpath = get_bugpath(reports[0])
        # Assumption is bugpath has control*warning{1}Note*
        self.assertEqual(3, len(bugpath))
        #self.assertListEqual([()], bugpath)


if __name__ == '__main__':
    unittest.main()
