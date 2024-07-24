from src.auth import register, login
from src.utils import read_json, save_json

def startup(username: str):
    print("############################################")
    print("########## Welcome to Recipe Book ##########")
    print("############################################")
    print(f"Hi {username} :D")


def input_food_name():
    food_name = input("Enter food name: ")
    return food_name


def input_ingredients():
    ingredients = []
    while True:
        food_ingredient = input("Enter ingredient, type 0 to stop: ")
        if food_ingredient == "0":
            break
        ingredients.append(food_ingredient)
    return ingredients


def input_cooking_steps():
    cooking_steps = []
    while True:
        cooking_step = input("Enter cooking steps, type 0 to stop: ")
        if cooking_step == "0":
            break
        cooking_steps.append(cooking_step)
    return cooking_steps


if __name__ == "__main__":
    # alur jalan kodenya -> hanya bisa diimplmentasikan didalam functional programming/oop programming
    usernames = read_json('usernames.json')
    user_input = input("Do you want to login or register? (login/register): ")

    if user_input == 'login':
        user = login(usernames)
        print(user)
    elif user_input == 'register':
        usernames = register(usernames)
        save_json(usernames, 'usernames.json')
        exit('User created successfully!')
    else:
        raise ValueError("Invalid input. Please enter 'login' or 'register'.")
    
    startup(user['username'])
    # hashing -> sensor password / informasi sensitif
    # jainudin12345 -> hashing/encode -> iausgdaisdgasiuegq07912397t1231
    # jainudin12345 -> hashing/encode -> iausgdaisdgasiuegq07912397t1231 == iausgdaisdgasiuegq07912397t1231
    # 
    exit()
    # Create
    while True:
        food_name = input_food_name()
        food_ingredients = (
            input_ingredients()
        )  # gimana caranya masukin ingredients ini kedalam db (one to many relationship)
        cooking_steps = (
            input_cooking_steps()
        )  # gimana caranya masukin cooking steps ini kedalam db (one to many relationship)
        recipe = {
            "food_name": food_name,
            "ingredients": food_ingredients,
            "cooking_steps": cooking_steps,
        }
        recipes.append(recipe)
        exit_ = input("Do you want to exit? (y/n): ")
        if exit_ == "y":
            print(recipes)
            exit()
        elif exit_ == "n":
            continue
        else:
            raise ValueError("Invalid input. Please enter 'y' or 'n'.")  #
