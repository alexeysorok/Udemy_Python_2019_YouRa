import unittest
import upper


class TestUpper(unittest.TestCase):
    def test_one_world(self):
        text = 'hello'
        result = upper.upper_text(text)
        self.assertEqual(result, 'HELLO')

if __name__ == '__main__':
    unittest.main()

