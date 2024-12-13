## デコレータなし--------------------------------

def start_end(func):
    def add_start_end():
        print('start')
        func()
        print('end')
    return add_start_end

def print_apple():
    print('これは林檎です。')

func = start_end(print_apple)
func()

## デコレータあり--------------------------------

def start_end(func):
    def add_start_end():
        print('start')
        func()
        print('end')
    return add_start_end

@start_end
def print_apple():
    print('これは林檎です。')

print_apple()

## 引数を持つ関数　デコレータなし--------------------------------

def start_end(func):
    def add_start_end(_text):
        print('start')
        func(_text)
        print('end')
    return add_start_end

def print_text(text):
    print(text + '!')

start_end(print_text)('これは林檎です。')

## 引数を持つ関数　デコレータあり--------------------------------

def start_end(func):
    def add_start_end(_text):
        print('start')
        func(_text)
        print('end')
    return add_start_end

@start_end
def print_text(text):
    print(text + '!')

print_text('これは林檎です。')

## 複数の引数　デコレータ--------------------------------

def start_end(func):
    def add_start_end(*args, **kwargs):
        print('start')
        func(*args, **kwargs)
        print('end')
    return add_start_end

@start_end
def print_join_dash(a, b):
    print(f'{a}-{b}')

print_join_dash('555', b='810')

## 複数の引数 戻り値あり　デコレータ--------------------------------

def start_end(func):
    def add_start_end(*args, **kwargs):
        print('start')
        x = func(*args, **kwargs)
        print('end')
        return x
    return add_start_end

@start_end
def add_exclamation(text):
    print('add_exclamationが実行されました。')
    return text + '!'

result = add_exclamation('これは林檎です。')
print(result)

## 複数の引数 複数の戻り値　デコレータ--------------------------------

def start_end(func):
    def add_start_end(*args, **kwargs):
        print('start')
        x = func(*args, **kwargs)
        print('end')
        return x
    return add_start_end

@start_end
def add_exclamation(text):
    print('add_exclamationが実行されました。')
    return 'これはバナナですか？',  text + '!'

result1, result2 = add_exclamation('これは林檎です。')
print(result1, result2)


