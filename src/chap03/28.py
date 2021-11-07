from utils import load_UK_article, remove_emphasis
import re


def remove_markup(value):

    # 言語系
    lang_pattern = re.compile(r'{{(.*\||)(.*?)}}')
    # 参照系
    ref_pattern = re.compile(r'<(.*)>')
    # 強調系
    em_pattern = re.compile(r'\'+')
    # リンク関連
    link_pattern = re.compile(r'\[\[(.*\||)(.*)\]\]')
    file_pattern = re.compile(r'\[\[(File|ファイル):(.+?\||)(.*)\}?\}?')

    # 削除
    value = re.sub(lang_pattern, r'\2', value)
    value = re.sub(ref_pattern, '', value)
    value = re.sub(em_pattern, '', value)
    value = re.sub(link_pattern, r'\2', value)
    value = re.sub(file_pattern, r'\3', value)
    return value


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
    res = {key: remove_markup(value) for key, value in res.items()}

    # 強調表現を除く
    res = remove_emphasis(res)
    for key, value in res.items():
        print(key, ':', value)
