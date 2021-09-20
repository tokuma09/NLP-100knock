import pandas as pd
import argparse


def get_parser():
    parser = argparse.ArgumentParser(description='ファイル分割')
    parser.add_argument('--n', help='分割数', type=int)

    return parser


def main():
    parser = get_parser()
    arg = parser.parse_args()

    df = pd.read_csv('data/chap02/popular-names.txt', sep='\t', header=None)

    step = (len(df) // arg.n)

    for i in range(arg.n):
        df_split = df.iloc[i * step:(i + 1) * step]
        df_split.to_csv(f'output/chap02/python_split{i+1}.txt',
                        sep='\t',
                        index=None,
                        header=None)


if __name__ == "__main__":
    main()
