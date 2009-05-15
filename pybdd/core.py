
from pybdd.testcase import Testcase

class Core(object):
    def collect_tests(self):
        return ["foo.feature"]

    def run_tests(self):
        tests = self.collect_tests()
        result = 0
        for testfile in tests:
            testcase = Testcase(testfile)
            if testcase.run() != 0:
                result = 1
                break

        return result
