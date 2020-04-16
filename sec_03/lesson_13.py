s = 'My name is Mike. Hi Mike.'
print(s)

# 指定文字列で開始してるかチェック
is_start = s.startswith('My')
print(is_start)

is_start = s.startswith('X')
print(is_start)

print('#########')

# 先頭から検索
print(s.find('Mike'))
# 最後から検索
print(s.rfind('Mike'))
# 存在数をカウント
print(s.count('Mike'))
# 文字列の先頭だけを大文字に変換
print(s.capitalize())
# 単語の先頭文字を大文字に変換
print(s.title())
# 文字列を大文字に変換
print(s.upper())
# 文字列を小文字に変換
print(s.lower())
# 文字列の置換
print(s.replace('Mike', 'Nancy'))