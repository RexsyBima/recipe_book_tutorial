import json

user1 = {'username' : 'user1', 'password' : 'pass1'}
user2 = {'username' : "user2", 'password' : 'pass2'}

datas = {user1['username']: user1, user2['username']: user2}
datas2 = {'user1': {'username': 'user1', 'password': 'pass1'}, 'user2': {'username': 'user2', 'password': 'pass2'}}
#print(x)

#dict_test = {'user1': {'username': 'user1', 'password': 'pass1'}}
user_test = 'user1'
user_test_pass = 'pass1'

if user_test in datas and user_test_pass == datas[user_test]['password']:
    print('login success')