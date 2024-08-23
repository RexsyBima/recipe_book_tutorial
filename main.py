from src.auth import register, login
from src.utils import read_json, save_json, print_enumerate, update_json


def startup(username: str):
    print("############################################")
    print("########## Welcome to Recipe Book ##########")
    print("############################################")
    print(f"Hi {username} :D")


def input_food_name(base_input="Enter food name: "):
    food_name = input(base_input)
    return food_name


def input_descriptions(base_input="Enter food descriptions: "):
    descriptions = input(base_input)
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


def add_food(user, database):
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
    update_json(database, user, filename="database.json")


def show_user_food(
    user,
):
    print_enumerate(
        user["recipes"], key="food_name", title=f"{user['username'].upper()} FOOD LIST"
    )
    user_input = (
        int(input("Please input your choice to see the detail of the recipe : ")) - 1
    )
    print(user_input, len(user["recipes"]))
    # if user_input < 0 or user_input >= len(user["recipes"]):
    #    raise ValueError("Invalid input. Please enter a correct food number.")
    if user_input not in list(range(len(user["recipes"]))):
        raise ValueError("Invalid input. Please enter a correct food number.")
    food = user["recipes"][user_input]
    print(f"FOOD NAME : {food['food_name']}")
    print(f"FOOD DESCRIPTIONS : \n\n {food['descriptions']}")
    print(f"FOOD INGREDIENTS : \n\n")
    for i, f in enumerate(food["ingredients"], start=1):
        print(f"{i}. {f}")
    print(f"INSTRUCTIONS \n\n")
    for i, f in enumerate(food["instructions"], start=1):
        print(f"{i}. {f}")


def delete_food(user, database):
    for i, food in enumerate(user["recipes"], start=1):
        print(i, food["food_name"])
    food_to_delete = int(input("Please enter the food you want to delete : ")) - 1
    if food_to_delete < 0 or food_to_delete >= len(user["recipes"]):
        raise ValueError("Invalid input. Please enter a correct food number.")
    sure = bool(
        int(
            input(
                f"Are you sure you want to delete {user['recipes'][food_to_delete]['food_name']} food? 0 for no, other than 0 yes: "
            )
        )
    )
    if sure:
        user["recipes"].pop(food_to_delete)
    update_json(database, user, filename="database.json")


def show_feature_menu():
    print("Enter the input")
    print("1. Add food")
    print("2. Edit food")
    print("3. Show all current user foods")
    print("4. Delete food")
    print("5. get all username food recipes")
    print("6. Search chef recipe")
    print("7. exit")


def edit_food_pt1(user):
    print_enumerate(
        user["recipes"], key="food_name", title=f"{user['username'].upper()} FOOD LIST"
    )
    food_index_to_edit = (
        int(input("Please enter the food you want to edit")) - 1
    )  # Self explanatory
    food = user["recipes"][food_index_to_edit]  # Use the list indexingg to edit food
    sure = bool(  # Self explanatory
        int(
            input(
                f"Are you sure you want to edit this food, {food['food_name']}? 0 for No, other than 0 for Yes : "
            )
        )
    )
    return food_index_to_edit, sure


def edit_food_pt2(food_index_to_edit: int, sure: bool, user):
    if not sure:
        raise ValueError(
            f"Canceling Editing for food {user['recipes'][food_index_to_edit]['food_name']}."
        )
    else:
        print("1. Edit food name")
        print("2. Edit food descriptions")
        print("3. Edit food ingredients")
        print("4. Edit food instructions")
        edit_input = int(input("Please enter your choice: "))
        return edit_input


def edit_food_pt3(food_index_to_edit: int, edit_input: int, user, database):
    food = user["recipes"][food_index_to_edit]
    match edit_input:
        case 1:
            food["food_name"] = input_food_name(base_input="Enter new food name: ")
        case 2:
            food["descriptions"] = input_descriptions(
                base_input="Enter new descriptions: "
            )
        case 3:
            for i, ingredients in enumerate(food["ingredients"], start=1):
                print(f"{i}. {ingredients}")
            ingredients_to_edit = (
                int(input("Please enter the ingredients you want to edit")) - 1
            )
            food["ingredients"][ingredients_to_edit] = input("Enter new ingredient : ")
        case 4:
            for i, instructions in enumerate(food["instructions"], start=1):
                print(f"{i}. {instructions}")
            instructions_to_edit = (
                int(input("Please enter the instructions you want to edit")) - 1
            )
            food["instructions"][instructions_to_edit] = input(
                "Enter new instruction : "
            )
        case _:
            raise ValueError("Invalid input. Please enter a number between 1 and 4.")
    update_json(database, user, filename="database.json")


def get_user_input():
    try:
        user_input = int(input("Please input your choice: "))
    except ValueError:
        print("Invalid input. Please enter a number between 1 and 5.")
        exit()

    if user_input not in [1, 2, 3, 4, 5, 6, 7]:
        raise ValueError("Invalid input. Please enter a number between 1 and 5.")
    return user_input


def get_all_user_foods(
    database, username
):  # TODO FIX THIS, so it be able to get all user food in detail
    recipes: list[dict] = []
    for d in database:
        recipes.append({database[d]["username"]: database[d]["recipes"]})
    for user in recipes:
        for k in user:
            if k == username:
                print(k, "(You)")
            else:
                print(k)
            food = user[k]
            for i, f in enumerate(food, start=1):
                print(f"{i}.", f["food_name"])


def search_chef(database: dict):
    chef_input = input("Please enter username : ")
    for d in database:
        if d.lower() == chef_input.lower():
            chef_data = database[d]
            return chef_data
    raise ValueError("Chef not found")


if __name__ == "__main__":
    # alur jalan kodenya -> hanya bisa diimplmentasikan didalam functional programming/oop programming
    database = read_json("database.json")
    user_input = input("Do you want to login or register? (login/register): ")

    if user_input == "login":
        user = login(database)
    elif user_input == "register":
        database = register(database)
        save_json(database, "database.json")
        exit("User created successfully!")
    else:
        raise ValueError("Invalid input. Please enter 'login' or 'register'.")

    startup(user["username"])
    while True:
        show_feature_menu()
        user_input = get_user_input()

        # Create
        match user_input:
            case 1:  # Add food
                add_food(user, database)
            case 2:
                food_index_to_edit, sure = edit_food_pt1(user)
                edit_input = edit_food_pt2(food_index_to_edit, sure, user)
                edit_food_pt3(food_index_to_edit, edit_input, user, database)
            case 3:  # SHow all user foods
                show_user_food(user)
            case 4:  # Delete user food
                delete_food(user, database)
            case 5:  # get all user in db foods
                get_all_user_foods(database, user["username"])
            case 6:
                chef_data = search_chef(database)
                show_user_food(chef_data)
            case 7:
                print("exitting program, saving...")
                save_json(database, "database.json")
                exit()


""" 
NOTE
1.  # Edit Food Nambahin data permakanan, nbahin step cooking (ingredients), ngurangin step cooking/ menghapus bbrp step cooking, dst nya # if user input when editt  is empty, delete that step
2. If user input is empty during description for an ex, cancel editing
"""
