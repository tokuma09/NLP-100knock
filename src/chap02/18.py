import pandas as pd

if __name__ == '__main__':
    df = pd.read_csv('data/chap02/popular-names.txt', sep='\t', header=None)

    print(df.sort_values(2, ascending=False))
