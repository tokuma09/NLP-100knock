def make_ngram(sentence, n):

    return [
        ''.join(sentence[ind:ind + n]) for ind in range(len(sentence) - n + 1)
    ]


if __name__ == '__main__':
    sentence = 'I am an NLPer'
    n = 2
    print('by word')
    print(make_ngram(sentence.split(), n))

    print('by char')
    # drop space
    print(make_ngram(sentence.replace(' ', ''), n))
