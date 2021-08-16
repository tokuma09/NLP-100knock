import unittest


class TestLength(unittest.TestCase):
    def test_length(self):
        sentence = 'Now I need a drink, alcoholic of course, after the heavy lectures involving quantum mechanics.'
        ans = [3, 1, 4, 1, 5, 9, 2, 6, 5, 3, 5, 8, 9, 7, 9]

        sentence = sentence.replace(',', '').replace('.', '')
        res = [len(word) for word in sentence.split()]

        self.assertEqual(res, ans)


if __name__ == '__main__':
    unittest.main()
