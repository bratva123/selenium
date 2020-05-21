import unittest

class AsserDemo(unittest.TestCase):
    def test_assertTrueFalse(self):
        a = True
        self.assertTrue(a,"a is not false")
        b = False
        self.assertFalse(b, "b is not false")

    def test_assertEqual(self):
        a = "Test"
        b = "test"
        self.assertNotEqual(a, b, msg="'a' is to 'b'")

if __name__ =='__main__':
    unittest.main(verbosity=2)