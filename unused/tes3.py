#       username
data1 = {"username": "value1", "password": "value2", 'total_uang' : 12000} #orang a
data2 = {"username": "value1", "password": "value3", 'total_uang' : 10000}
data3 = {"username": "value1", "password": "value2", 'total_uang' : 8000} #orang b

data = [data1, data2, data3]

user_test = 'value1'
user_test_pass = 'value2'

for user in data:
    if user['username'] == user_test and user['password'] == user_test_pass:    
        print('login success', user)
        break
