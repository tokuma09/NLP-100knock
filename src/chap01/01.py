import unittest


class TestSkip(unittest.TestCase):
    def test_skip(self):
        s = 'パタトクカシーー'
        ans = 'パトカー'

        self.assertEqual(s[0::2], ans)


if __name__ == '__main__':
    unittest.main()
