last_names = ['今西', '佐藤', '鈴木', '田中']
first_names = ['航平', '謙介', '康二', '康介']

# print(last_names[0] + first_names[0] + 'さん')
# print(last_names[1] + first_names[1] + 'さん')
# print(last_names[2] + first_names[2] + 'さん')
# print(last_names[3] + first_names[3] + 'さん')

for i in range(len(last_names)):
    print(last_names[i] + first_names[i] + 'さん')

# zip(a, b) で複数のリストの要素を同時に取得
# 3つ以上のリストから要素を取り出すことも可能
for last_name, first_name in zip(last_names, first_names):
    print(last_name + first_name + 'さん')

# print('出席番号', 0, '番目の' + last_names[0] + 'さん')
# print('出席番号', 1, '番目の' + last_names[1] + 'さん')
# print('出席番号', 2, '番目の' + last_names[2] + 'さん')
# print('出席番号', 3, '番目の' + last_names[3] + 'さん')

for i in range(len(last_names)):
    print('出席番号', [i], '番目の' + last_names[i] + 'さん')

# enumerate リストの「要素番号」と「要素」を同時に取得
for num, last_name in enumerate(last_names):
    print('出席番号', num, '番目の' + last_name + 'さん')