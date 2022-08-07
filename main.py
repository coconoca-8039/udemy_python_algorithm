#デコレータの勉強
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
