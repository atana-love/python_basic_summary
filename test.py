# ●文字列について-------------------------
price = 100
print(f'この商品は{price}円です。') # この商品は100円です。


# ●リストについて-------------------------
fruit_list = ['リンゴ', 'Apple', '林檎', 'ringo']
print(fruit_list[1]) # Apple

## リストの分割について
x = ['a','b','c','d','e','f','g','h']
y = x[2:6]
print(y) # ['c', 'd', 'e', 'f']
### 開始位置や終了位置を省略することも可能

## リストの追加、削除について
x = [11, 22, 33]
x.append(44)
x.remove(22)
print(x) # [11, 33, 44]

## 特徴　
### 違う型も入れれる　ソートするとエラー
x = [1,2,'a','b']
### 同じ要素を入れれる　ソートするとNone
x = ['a','b','a']


# ●辞書について-------------------------
x = {
    '国語': 10,
    '数学': 20,
    '英語': 30,
}
print(x['数学']) # 20
## x[key]とx.get(key)の使いわけについて
## x[key]は必ずkeyが存在する時に使用する。ないときはエラー
## x.get(key)はkeyがないときはNoneを返す

## 辞書への追加、削除について
x['社会'] = 40
del x['英語']
print(x) # {'国語': 10, '数学': 20, '社会': 40}

## Keyだけを取得
print(x.keys()) # dict_keys


# ●集合について-------------------------
## 集合は順序を持たず、同じ値は持てない
x = {1, 3, 5}
## 要素の追加、削除について
x.add(7)
x.remove(3)
print(x) # {1, 5, 7}

## 和集合、差集合、積集合
x = {0, 1, 3, 6}
y = {0, 2, 5, 6}
z = x | y # 和集合
print(z) # {0, 1, 2, 3, 5, 6}
z = x - y #差集合
print(z) # {1, 3}
z = x & y # 積集合
print(z) # {0, 6}


# ●クラスについて-------------------------
## Javaのようにクラス変数を定義する必要はない
class User:
    def __init__(self, name, mail_address, point):
        self.name = name
        self.mail_address = mail_address
        self.point = point

    def add_point(self, point):
        self.point += point

user_1 = User('佐藤', 'sato@example.com', 500)
user_1.add_point(100)
print(user_1.name) # 佐藤
print(user_1.point) # 600
