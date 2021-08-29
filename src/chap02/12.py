import pandas as pd

if __name__ == '__main__':
    df = pd.read_csv('data/chap02/popular-names.txt', sep='\t', header=None)

    df[0].to_csv('output/chap02/python_col1.txt', index=False, header=None)
    df[1].to_csv('output/chap02/python_col2.txt', index=False, header=None)
