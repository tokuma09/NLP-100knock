import pandas as pd
import argparse


def get_parser():
    parser = argparse.ArgumentParser(description='先頭n行取得')
    parser.add_argument('--n', help='読み込む行数', type=int)

    return parser


def main():
    parser = get_parser()
    arg = parser.parse_args()

    df = pd.read_csv('data/chap02/popular-names.txt', sep='\t', header=None)
    print(df.head(arg.n))


if __name__ == "__main__":
    main()
