# 可変長引数について
# 複数の引数を受け取ることが出来る。
# ● *args　   →　タプルとして受け取る可変長引数
# ● **kwargs　→　辞書として受け取る可変長引数

# *args  可変長引数 + 普通の引数
# 普通の引数が先の場合
def func(x, *args):
    print(x, args)

func(1, 'a', 'b', 3)  # >>> 1 ('a', 'b', 3)


# 普通の引数が後の場合 （引数でxを指定する必要がある）
def func(*args, x):
    print(args, x)
    
func(1, 'a', 'b', x=3) # >>> (1, 'a', 'b') 3


# **kwargsの使い方について
def func(**kwargs):
    print(kwargs)
    
func(id='1', name='時崎') # >>> {'id': '1', 'name': '時崎'}
func(item=199, price=555) # >>> {'item': 199, 'price': 555}


# また*args と違い普通の引数は先に書く必要がある。
def func(x, **kwargs):
    print(x, kwargs)
    
func(1, item=199, price=555) # >>> 1 {'item': 199, 'price': 555}
