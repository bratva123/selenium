import unittest


class TestCaseDemo(unittest.TestCase):
    def setUp(self):
        print("I will run once before every test")

    def test_methodA(self):
        print("running Method A")

    def test_methodB(self):
        print("running test method B")

    def tearDown(self):
        print("i will run after every test")

if __name__ == '__main__':
    unittest.main(verbosity=2)

