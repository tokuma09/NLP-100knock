from utils import load_UK_article, remove_emphasis
import re


def remove_inner_link(res):
    # イギリスの場合内部リンクは以下のように記載
    # [[記事名]]
    # [[記事名|表示文字]]
    # 表示文字がなければ記事名を利用する。
    # 最初の()は記事名|があれば記事名|に、そうでなければ、空文字にマッチさせる
    pattern = re.compile(r'\[\[(.*\||)(.*)\]\]')
    return {key: re.sub(pattern, r'\2', value) for key, value in res.items()}


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
    res = remove_inner_link(res)

    for key, value in res.items():
        print(key, ':', value)
