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
        food_ingredient = input("Enter ingredient, type exit to stop: ")
        if food_ingredient == "exit":
            break
        ingredients.append(food_ingredient)
    return ingredients


def input_cooking_steps():
    cooking_steps = []
    while True:
        cooking_step = input("Enter cooking steps, type exit to stop: ")
        if cooking_step == "exit":
            break
        cooking_steps.append(cooking_step)
    return cooking_steps


if __name__ == "__main__":
    # alur jalan kodenya -> hanya bisa diimplmentasikan didalam functional programming/oop programming
    startup("Bimbim")
    recipes = []
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
