import pandas as pd

if __name__ == '__main__':
    df_1 = pd.read_csv('output/chap02/python_col1.txt', header=None)

    df_2 = pd.read_csv('output/chap02/python_col2.txt', header=None)

    df_res = pd.concat([df_1, df_2], axis=1)
    df_res.to_csv('output/chap02/python_13.txt',
                  sep='\t',
                  index=False,
                  header=None)
