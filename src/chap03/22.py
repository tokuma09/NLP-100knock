from utils import load_UK_article

if __name__ == '__main__':

    uk_articles = load_UK_article().split('\n')

    res = [
        text.split(':')[1].replace('|*', '').replace(']', '')
        for text in uk_articles if text.startswith('[[Category:')
    ]

    print(res)
