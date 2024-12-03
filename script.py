# from my_module import print_module
# もしモジュールが同じ階層にない場合は
## from サブディレクトリ名.モジュール名 import 関数名・クラス名
from my_packeges.sub_packeges.my_module import print_module
from datetime import datetime

print('script開始')
print_module()
print('script終了')

print(datetime.today())