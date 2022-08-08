#独学プログラマー
'''
#カプセル化
class Data:
    def __init__(self):
        self.nums = [1,2,3,4,5]

    def change_data(self,index,n):
        self.nums[index] = n

data_one = Data()
data_one.nums[0] = 100
print(data_one.nums)

data_two = Data()
data_two.change_data(0,100)
print(data_two.nums)
'''

'''
#継承
#親クラスの定義
class Shape:
    def __init__(self,w,l):
        #初期化
        self.width = w
        self.len = l

    def print_size(self):
        print("{} by {}".format(self.width,self.len))

#子クラスの定義
#親クラスの情報を継承しているから、wとlの情報を持っている
class Square(Shape):
    def area(self):
        return self.width * self.len

    #親クラスと同じ名前のメソッドを子クラスで定義する
    #メソッドオーバーライド
    def print_size(self):
        print("I am {} by {}.".format(self.width,self.len))

a_square = Square(20,20)
print(a_square.area())
a_square.print_size()
'''

#コンポジション
#「has a ~」の関係を表す
class Dog:
    def __init__(self,name,breed,owner):
        self.name = name
        self.breed = breed
        self.owner = owner

class Person:
    def __init__(self,name):
        self.name = name

mick = Person("Mick Jaggner")
stan = Dog("Stanly","Bulldog",mick)
print(stan.owner.name)
