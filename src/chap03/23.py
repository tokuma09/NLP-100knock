from utils import load_UK_article
import re

if __name__ == '__main__':

    uk_articles = load_UK_article().split('\n')

    # ==を除いて文字のみ抽出しキーにしたあと、=の数-1をレベル
    res = {
        re.sub('(=*)', '', text).strip(): re.match('(=*)', text).end() - 1
        for text in uk_articles if text.startswith('=')
    }

    for key, value in res.items():
        print(key, value)
