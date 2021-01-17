# 関数の作成
def create_mail(recv, bill):
    # ローカル変数(関数内で作った変数)
    tmp = '''{}様
PT企画の斉藤です。
今月の請求額は{}円です。
'''
    # 文字列.format(値1, 値2) 文字列内の{}に任意の値を差込
    msg = tmp.format(recv, bill)
    print(msg)

create_mail('山本', 40000)