from utils import load_UK_article
import re


def remove_emphasis(res):
    return {key: re.sub(r'\'+', '', value) for key, value in res.items()}


if __name__ == '__main__':

    uk_article = load_UK_article()

    # 基礎情報は以下の様にデータが含まれる
    # |key =value(ここに1スペース入りうる)
    # keyは任意の文字で最後にスペースが,
    # valueは最初の1文字にスペースが入ることもあるが、任意の文字
    pattern = r'\|(.*)\s=\s*(.+)'
    res = {}
    for match in re.findall(pattern, uk_article):
        res[match[0].strip()] = match[1].strip()

    # 強調表現を除く
    res = remove_emphasis(res)
    for key, value in res.items():
        print(key, ':', value)
