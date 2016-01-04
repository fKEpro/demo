
# unit test

import unittest
import mathu


class TestMathu(unittest.TestCase):
    def test_add(self):
        res = mathu.Mathu().add(5, 8)
        self.assertEqual(res, 13)

    def test_div(self):
        res = mathu.Mathu().div(10, 8)
        self.assertGreater(res, 1)

    def test_check_even(self):
        res = mathu.Mathu().check_even(4)
        self.assertTrue(res)

    def test_error(self):
        self.assertRaises(ZeroDivisionError, lambda:mathu.Mathu().div(5, 0))

if __name__ == '__main__':
    unittest.main()


