import unittest
import uniTestPackage.assertDemo1

class TestCaseDemo(unittest.TestCase):
    @classmethod
    def setUpClass(cls):
        print("*#"*30)
        print("run first tim before all test cases")
        print("*#"*30)

    def setUp(self):
        print("I will run once before every test")

    def test_methodA(self):
        print("running Method A")

    def test_methodB(self):
        print("running test method B")

    def tearDown(self):
        print("i will run after every test")
    @classmethod
    def tearDownClass(cls):
        print("*#" * 30)
        print("run first time after all test cases")
        print("*#" * 30)


if __name__ == '__main__':
    unittest.main(verbosity=2)

