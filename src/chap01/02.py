import unittest


class TestCombine(unittest.TestCase):
    def test_combine(self):
        s1 = 'パトカー'
        s2 = 'タクシー'
        ans = 'パタトクカシーー'

        res = ''
        for char1, char2 in zip(s1, s2):
            res += char1 + char2

        self.assertEqual(res, ans)


if __name__ == '__main__':
    unittest.main()
