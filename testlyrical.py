import unittest
from lyrical import multiply


class TestFileName(unittest.TestCase):
    def test_function1(self):
        self.assertEqual(multiply(2, 4), 8)
        self.assertEqual(multiply(2, 0), 0)
    

if __name__ == '__main__':
    unittest.main()