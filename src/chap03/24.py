from utils import load_UK_article
import re

if __name__ == '__main__':
    uk_article = load_UK_article()

    # ファイル:file name | ~という形で保存されているので、正規表現で抽出
    # マッチするグループの2つ目をプリント
    # .+?は最低1回任意の文字が出るが最小数でのマッチになる
    for file in re.findall(r'\[\[(File|ファイル):(.+?)\|', uk_article):
        print(file[1])
