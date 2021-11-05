import pandas as pd


def load_UK_article():
    try:
        df = pd.read_json('data/chap03/jawiki-country.json', lines=True)
    except:
        df = pd.read_json('../../data/chap03/jawiki-country.json', lines=True)

    return df[df['title'] == 'イギリス']['text'].values[0]
