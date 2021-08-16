def cipher(text):
    # 　英小文字は文字コード97-122の範囲にある。
    # http://www3.nit.ac.jp/~tamura/ex2/ascii.html
    text = [chr(219 - ord(w)) if 97 <= ord(w) <= 122 else w for w in text]
    return ''.join(text)


if __name__ == '__main__':
    text = 'Text 4 cipher func.'
    print('original text:', text)

    encode = cipher(text)
    print('cipher:', encode)
    decode = cipher(encode)
    print('cipher again:', decode)
