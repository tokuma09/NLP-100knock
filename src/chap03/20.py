import pandas as pd

if __name__ == '__main__':
    df = pd.read_json('data/chap03/jawiki-country.json', lines=True)
    print(df[df['title'] == 'イギリス']['text'].values[0])
