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


def input_descriptions():
    descriptions = input("Enter food descriptions: ")
    return descriptions


def input_ingredients():
    ingredients = []
    while True:
        food_ingredient = input("Enter ingredient, type 0 to stop: ")
        if food_ingredient == "0":
            break
        ingredients.append(food_ingredient)
    return ingredients


def input_instructions():
    cooking_steps = []
    while True:
        cooking_step = input("Enter cooking steps, type 0 to stop: ")
        if cooking_step == "0":
            break
        cooking_steps.append(cooking_step)
    return cooking_steps


if __name__ == "__main__":
    # alur jalan kodenya -> hanya bisa diimplmentasikan didalam functional programming/oop programming
    usernames = read_json("usernames.json")
    user_input = input("Do you want to login or register? (login/register): ")

    if user_input == "login":
        user = login(usernames)
    elif user_input == "register":
        usernames = register(usernames)
        save_json(usernames, "usernames.json")
        exit("User created successfully!")
    else:
        raise ValueError("Invalid input. Please enter 'login' or 'register'.")

    startup(user["username"])
    print("Enter the input")
    print("1. Add food")
    print("2. Edit food")
    print("3. Show all current user foods")
    print("4. Delete food")
    print("5. exit")

    try:
        user_input = int(input("Please input your choice: "))
    except ValueError:
        print("Invalid input. Please enter a number between 1 and 5.")
        exit()

    if user_input not in [1, 2, 3, 4, 5]:
        raise ValueError("Invalid input. Please enter a number between 1 and 5.")

    # Create
    if user_input == 1:
        name = input_food_name()
        descriptions = input_descriptions()
        ingredients = input_ingredients()
        instructions = input_instructions()
        food = {
            "food_name": name,
            "descriptions": descriptions,
            "ingredients": ingredients,
            "instructions": instructions,
        }
        user["recipes"].append(food)
        for u in usernames:
            if u == user["username"]:
                usernames[u]["recipes"] = user["recipes"]
        save_json(usernames, "usernames.json")
    elif user_input == 2:
        print("This is placeholder for edit food")
    elif user_input == 3:
        for i, food in enumerate(user["recipes"], start=1):
            print(f"{i}. {food['food_name']}")
        user_input = (
            int(input("Please input your choice to see the detail of the recipe : "))
            - 1
        )
        food = user["recipes"][user_input]
        print(f"FOOD NAME : {food['food_name']}")
        print(f"FOOD DESCRIPTIONS : \n\n {food['descriptions']}")
        print(f"FOOD INGREDIENTS : \n\n")
        for i, f in enumerate(food["ingredients"], start=1):
            print(f"{i}. {f}")
        print(f"INSTRUCTIONS \n\n")
        for i, f in enumerate(food["instructions"], start=1):
            print(f"{i}. {f}")
    elif user_input == 4:
        print("This is placeholder for delete food")
    else:
        print("This is placeholder for exit")

    exit()
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
