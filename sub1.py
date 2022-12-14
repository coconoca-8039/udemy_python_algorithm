#ルキちゃんねる参照

#内包表記
#こんなリストがあったとする
users = [
    {'id':1,'name':'tom','email':'tom@gmail.com','age':20},
    {'id':2,'name':'alice','email':'alice@gmail.com','age':25},
    {'id':3,'name':'roki','email':'roki@gmail.com','age':1000},
    {'id':4,'name':'tom','email':'john_smith@gmail.com','age':40},
]

'''
#標準的なforで記述した処理
emails = []
for user in users:
    if user['age'] < 30:
        emails.append(user['email'])
print(emails)
'''

'''
#リスト内包表記
young_user_emails = [user['email'] for user in users if user['age'] < 30]
print(young_user_emails)
'''

'''
#辞書内包表記
#idをキーにして0(1)でアクセスできる辞書を作成する
user_key_by_id = {user['id']:user for user in users}
print(user_key_by_id)
'''

'''
#セット内包表記
#ユニークな名前の集合を取得する
name_set = {user['name'] for user in users}
print(name_set)
'''

'''
#不等式に関するtips
#わざわざelseとか、面倒な演算子を使用しなくても数学的な記述方法で記述することができる
for user in users:
    if 25 <= user.get('age',0) <= 35:
        print(user)
'''

'''
#ジェネレータ
#無限に近い長さの配列を扱うことになるコード

#infinit_list = [num for num in range(0,123456789)]
#print(sum(infinit_list))

#ジェネレータ式にすると必要な分だけを確保することができる
#infinit_genertor = (num for num in range(0,123456789))
#generator(...)
'''

'''
#特定の要素を抜き出す
#ジェネレータ式の応用で、年齢が25歳の人を1人だけ取得する、いなければNoneを返す
user = next((user for user in users if user.get('age',0) ==  25),None)
print(user)
'''

'''
#デコレータ
from functools import wraps
def logger(separator:str = '-'):
    def decorator(func):
        @wraps(func)
        def wrapper(*args,**kwargs):
            #事前処理
            print(10 * separator)
            result = func(*args,**kwargs)
            #事後処理
            #print(result)
            print(10 * separator)
            return result
        return wrapper
    return decorator

@logger('-')
def func():
    print('デコレータのテスト')
func()
'''
