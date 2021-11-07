from utils import load_UK_article

if __name__ == '__main__':

    # 改行して1行ずつリストで保存
    uk_article = load_UK_article().split('\n')
    # [[Category:から始まるものを抽出
    res = [text for text in uk_article if text.startswith('[[Category:')]
    print(res)
