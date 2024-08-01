# x = {"name": "John", "age": 30, "car": None}  # JSON = Dictionary kalau di Python
import json

user1 = {'username' : 'user1', 'password' : 'pass1'}
user2 = {'username' : "user2", 'password' : 'pass2'}

usernames = [user1, user2]
print(usernames)

user_test = 'user3'
user_test_pass = 'pass4'

for user in usernames:
    if user['username'] == user_test and user['password'] == user_test_pass:    
        print('Login success')
    else:
        print('Login failed')



exit()
username = input("Enter username: ")
password1 = input("Enter password: ")
password2 = input("Confirm password: ")  # konfirmasi / validasi jika password 1 dan 2 sama
# database
if password1 == password2:
    print("User created successfully!")
    user = {"username": username, "password": password1}
    with open('usernames.json', 'w') as f: 
        json.dump(user, f)
else:
    raise ValueError("Passwords do not match.")


