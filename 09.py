import random


def shuffle_char(word):
    if len(word) <= 4:
        return word
    else:
        center_list = random.sample(word[1:-1], k=len(word[1:-1]))
        return ''.join([word[0]] + center_list + [word[-1]])


if __name__ == '__main__':
    random.seed(0)
    original = 'I couldn’t believe that I could actually understand what I was reading : the phenomenal power of the human mind .'

    print('----- original -----')
    print(original)
    print('----- shuffled -----')
    print(' '.join([shuffle_char(word) for word in original.split()]))
