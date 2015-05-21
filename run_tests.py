import unittest
from synergine_lifegame.test.LifeGameTestSuite import LifeGameTestSuite

runnable = unittest.TestSuite()
tests_suites = [LifeGameTestSuite()]

for testsuite in tests_suites:
    for test_case in testsuite.get_test_cases():
        runnable.addTest(unittest.makeSuite(test_case))

runner=unittest.TextTestRunner()
test_result = runner.run(runnable)

if test_result.failures or test_result.errors:
  exit(1)

