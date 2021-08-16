def make_ngram(sentence, n):

    return [
        ''.join(sentence[ind:ind + n]) for ind in range(len(sentence) - n + 1)
    ]


if __name__ == '__main__':

    s1 = 'paraparaparadise'
    s2 = 'paragraph'

    n = 2
    X = make_ngram(s1, n)
    Y = make_ngram(s2, n)

    print(f'和集合: {set(X) | set(Y)}')
    print(f'積集合: {set(X) & set(Y)}')
    print(f'差集合: {set(X) - set(Y)}')
    print('se' in (set(X) & set(Y)))
