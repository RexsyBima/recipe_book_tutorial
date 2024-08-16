# sample = {'user1': {'username': 'user1', 'password': 'pass1', 'total_uang': 1000}}


def register(datas):
    username = input("Enter username: ")
    password1 = input("Enter password: ")
    password2 = input(
        "Confirm password: "
    )  # konfirmasi / validasi jika password 1 dan 2 sama
    if username not in datas and password1 == password2:
        datas[username] = {"username": username, "password": password1, "recipes": []}
        return datas
    elif username in datas:
        raise ValueError("Username already exists")
    elif password1 != password2:
        raise ValueError("Password is not same")


def login(datas):
    username = input("Enter username: ")
    password = input("Enter password: ")
    if username in datas and datas[username]["password"] == password:
        print("Login success")
        return datas[username]
    else:
        raise ValueError("Login failed, username or password is incorrect")


"""
if __name__ == '__main__':
    usernames = read_json('usernames.json')
    user_input = input("Do you want to login or register? (login/register): ")

    if user_input == 'login':
        user = login(usernames)
        print(user)
    elif user_input == 'register':
        usernames = register(usernames)
        save_json(usernames, 'usernames.json')
        print('User created successfully!')
 """
