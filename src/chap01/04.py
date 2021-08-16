import unittest


def extract_characters(word, ind):

    if ind in [1, 5, 6, 7, 8, 9, 15, 16, 19]:
        return word[0]
    else:
        return word[:2]


class TestElements(unittest.TestCase):
    def test_extract(self):

        sentence = 'Hi He Lied Because Boron Could Not Oxidize Fluorine. New Nations Might Also Sign Peace Security Clause. Arthur King Can.'

        ans = {
            'H': 1,
            'He': 2,
            'Li': 3,
            'Be': 4,
            'B': 5,
            'C': 6,
            'N': 7,
            'O': 8,
            'F': 9,
            'Ne': 10,
            'Na': 11,
            'Mi': 12,
            'Al': 13,
            'Si': 14,
            'P': 15,
            'S': 16,
            'Cl': 17,
            'Ar': 18,
            'K': 19,
            'Ca': 20
        }

        sentence = sentence.replace(',', '').replace('.', '')

        res = {
            extract_characters(word, i + 1): (i + 1)
            for i, word in enumerate(sentence.split())
        }

        self.assertEqual(res, ans)


if __name__ == '__main__':
    unittest.main()
