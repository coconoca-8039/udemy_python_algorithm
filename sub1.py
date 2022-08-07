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

#ジェネレータ
