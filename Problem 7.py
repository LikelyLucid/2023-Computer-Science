Bread_Prices = {
    "Wholemeal": 1.00,
    "White": 0.80,
    "Cheesy White": 1.20,
    "Gluten Free": 1.40
}

Meat_Prices = {
    "Chicken": 2.69,
    "Beef": 3.00,
    "Salami": 4.00,
    "Vegan Slice": 3.30
}

Garnish_Prices = {
    "Onion": 1.69,
    "Tomato": 1.00,
    "Lettuce": 2.00,
    "Cheese": 2.50
}

def sandwich_maker():
    print("Welcome to the Sandwich Maker!")
    bread_choice = _extracted_from_sandwich_maker_3(
        "Please select your bread:",
        Bread_Prices,
        "Please enter your bread choice: ",
    )
    meat_choice = _extracted_from_sandwich_maker_3(
        "Please select your meat:",
        Meat_Prices,
        "Please enter your meat choice: ",
    )
    garnish_choice = _extracted_from_sandwich_maker_3(
        "Please select your garnish:",
        Garnish_Prices,
        "Please enter your garnish choice: ",
    )
    print("Your sandwich will cost: $" + str(Bread_Prices[bread_choice] + Meat_Prices[meat_choice] + Garnish_Prices[garnish_choice]))
    confirm = input("Would you like to confirm your order? (Y/N) ")
    if confirm == "Y":
        print("Thank you for your order!")
    else:
        print("Please make your changes.")
        sandwich_maker()


# TODO Rename this here and in `sandwich_maker`
def _extracted_from_sandwich_maker_3(arg0, arg1, arg2):
    print(arg0)
    for bread in arg1:
        print(bread)
    return input(arg2)

sandwich_maker()