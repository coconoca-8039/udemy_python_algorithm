#デコレータの勉強
#始めに実行されるのは、func = func1(func2)
#def func1()の引数にfunc2が設定される
#def wrapperは実行されず、しかしエラーも出さずにreturn wrapperをfunc1に返す
#func = wrapper　となる
#func1()はwrapper()と同義
#wrapper()が実行されることによりdef wrapper()が実行されることになる

def func1(f):
    def wrapper():
        print('開始')
        f()
        print('終了')
    return wrapper

def func2():
    print("Called func2")

func = func1(func2)
func()
