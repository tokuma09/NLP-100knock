import pandas as pd
import re


def load_UK_article():
    try:
        df = pd.read_json('data/chap03/jawiki-country.json', lines=True)
    except:
        df = pd.read_json('../../data/chap03/jawiki-country.json', lines=True)

    return df[df['title'] == 'イギリス']['text'].values[0]


def remove_emphasis(res):
    return {key: re.sub(r'\'+', '', value) for key, value in res.items()}


def remove_inner_link(res):
    # [[記事名]]
    # [[記事名|表示文字]]
    # 表示文字がなければ記事名を利用する。
    # 最初の()は記事名|があれば記事名|に、そうでなければ、空文字にマッチさせる
    pattern = re.compile(r'\[\[(.*\||)(.*)\]\]')
    return {key: re.sub(pattern, r'\2', value) for key, value in res.items()}


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
