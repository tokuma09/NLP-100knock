import unittest


class TestReversed(unittest.TestCase):
    def test_reverse(self):
        string = 'stressed'
        answer = 'desserts'
        self.assertEqual(string[::-1], answer)


if __name__ == '__main__':
    unittest.main()
