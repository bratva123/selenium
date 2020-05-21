import unittest

from uniTestPackage.assertDemo1 import AsserDemo
from uniTestPackage.test_case_demo2 import TestCaseDemo
#get all test from testclass 1 and test class 2

tc1 = unittest.TestLoader().loadTestsFromTestCase(AsserDemo)
tc2 = unittest.TestLoader().loadTestsFromTestCase(TestCaseDemo)


smoke_test = unittest.TestSuite([tc1, tc2])

unittest.TextTestRunner(verbosity=2).run(smoke_test)
