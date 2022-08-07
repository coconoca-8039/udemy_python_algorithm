#デコレータの勉強
#始めに実行されるのは、func = func1(func2)
#def func1()の引数にfunc2が設定される
#def wrapperは実行されず、しかしエラーも出さずにreturn wrapperをfunc1に返す
#func = wrapper　となる
#func1()はwrapper()と同義
#wrapper()が実行されることによりdef wrapper()が実行されることになる

import datetime

def print_datetime(f):
    def wrapper(*args,**kwargs):    #可変長引数
        print(f'開始:{datetime.datetime.now()}')
        f(*args,**kwargs)
        print(f'終了:{datetime.datetime.now()}')
        print('')
    return wrapper

#@~~でデコレーション
@print_datetime
def calc1(base,height):
    print('calc1の実行')
    print(base * height / 2)

calc1(3,15)
#print_datetime(calc)(3,10)

@print_datetime
def calc2(a,b,c,d):
    print('calc2の実行')
    print(a*b*c*d)

calc2(2,2,2,2)
