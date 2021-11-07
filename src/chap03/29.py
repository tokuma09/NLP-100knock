import re

import requests

from utils import (load_UK_article, remove_emphasis, remove_inner_link,
                   remove_markup)


def get_url(fname, endpoint="https://www.mediawiki.org/w/api.php"):

    fname = 'Flag of the United Kingdom.svg'
    params = {
        'action': 'query',
        'format': 'json',
        'prop': 'imageinfo',
        'titles': f'File:{fname}',
        'iiprop': 'url'
    }
    data = requests.get(endpoint, params=params).json()
    flag_url = data['query']['pages']['-1']['imageinfo'][0]['url']

    return flag_url


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
    res = remove_inner_link(res)

    # 国旗URLを保存
    flag_url = get_url(res['国旗画像'])
    print(flag_url)
