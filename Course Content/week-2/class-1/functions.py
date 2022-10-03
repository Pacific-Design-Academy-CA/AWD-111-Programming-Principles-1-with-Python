# Major task: Make dinner:
    # Ask what do you want for dinner? 6
    # Go to the grocery store and get ingredients
    # make dinner

def dinner_menu(food):
    print("Dinner Menu:", food)
    supermarket = "thrifties"
    ingredients = "spaghetti & meatballs"
    get_groceries(supermarket, ingredients)


def get_groceries(supermarket, ingredients):
    print("Going to", supermarket)
    print("Getting the following groceries", ingredients)
    print("\n--------------\n")
    make_dinner("7 pm")

def make_dinner(time):
    print("Got the ingredients, making dinner .......")
    print("\n--------------\n")
    print("Dinner completed before", time)

print("Marjor task prepare dinner loading..\n----------\n")

food = "spaghetti"

dinner_menu(food)
