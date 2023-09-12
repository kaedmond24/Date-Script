##############################################################################################################################
# Created by Kevin Edmond.
#
# This python script is used to simulate two people on a date. You begin by providing your date's name and your starting budget.
# Next, you provide the level (1-3) of restaurants you would like to attend. Menu prices for each restaurant is relative to the
# restaurant level. At the restaurant, your and your date provide a meal and drink selection from the provided menu. When the
# meal is complete, you receive an order total which is then subtracted from your budget. Outside of the restaurant, you check
# your budget and ask for a second date. Depending on the remaining budget, you will receive one of three responses.
#
#
# Please read README.md for full notes on script.
#
###############################################################################################################################

from time import sleep


# Get your name
my_name = input("Your Name: ").capitalize()

# Get date's name
date_name = input("Date's Name: ").capitalize()

# Starting budget
budget = int(input('Enter Budget: '))

# Select Restaurant Star Level
restaurant_level = int(input("Select Restauant Level [1, 2, or 3]: "))
order_total = 0

restaurants = {
    1: {
        'name': "McDowell's",
        'menu': {
            'chicken nuggets': 5,
            'fish sandwich': 10,
            'burger and fries': 15,
        },
        'drink': {
            'soda': 2,
            'iced tea': 3,
            'milkshake': 5
        }
    },
    2: {
        'name': "The Yellowcake Factory",
        'menu': {
            'house salad': 10,
            'old classic burger': 20,
            'shrimp scampi': 25,
            'chicken fettuccini alfredo': 30
        },
        'drink': {
            'water': 0,
            'soda': 4,
            'frozen drink': 8,
            'beer': 10,
            'cocktail': 15
        }
    },
    3: {
        'name': "The Grillin Capital",
        'menu': {
            'seared salmon': 45,
            'lamb chops': 60,
            'lobster tail': 70,
            'bone-in ribeye': 80,
        },
        'drink': {
            'artesian natural water': 10,
            'cocktail': 20,
            'white wine': 50,
            'sparkling wine': 75,
            'red wine': 100,
        }
    },
}

# Restaurant Greeting
print(" ")
print(" ***** ***** ***** ***** ***** ")
print(f"    Welecome to {restaurants[restaurant_level]['name']}!")
print(" ***** ***** ***** ***** ***** ")
print(" ")
print(f"Waiter: Hello, {my_name} and {date_name}!")
print("Waiter: Can I take your order?")
sleep(1)

# Show food menu
print(restaurants[restaurant_level]['menu'])

# Get food menu orders
my_menu_order = input("Your Menu Order: ").lower()
order_total += restaurants[restaurant_level]['menu'][my_menu_order]

date_menu_order = input("Date's Menu Order: ").lower()
order_total += restaurants[restaurant_level]['menu'][date_menu_order]

# Show drink menu
print("...and what would you like to drink?")
print(restaurants[restaurant_level]['drink'])

# Get drink menu orders
my_drink_order = input("Your Menu Order: ").lower()
order_total += restaurants[restaurant_level]['drink'][my_drink_order]

date_drink_order = input("Date's Menu Order: ").lower()
order_total += restaurants[restaurant_level]['drink'][date_drink_order]


# Get order total
print("I hope you all enjoyed your meal!")
print(f"Your total bill will be ${order_total}!")

# Pay Order Bill Total
print("Paying for meal...")
budget -= order_total
sleep(2)
print(f"Leaving {restaurants[restaurant_level]['name']}...")
print(" ")
sleep(2)

# Show Remaining Budget
print("Checking your Hell's Fargo app...")
print(f"Hi {my_name}, you have ${budget} in your account.")
sleep(2)


print(f"{my_name}: Hey {date_name}, want to go out again sometime?")
sleep(1)
if budget < 50:
    print(f"{date_name}: Nah... I'm Good!")
    print(f"{date_name}: But...")
    print(" *Tires Screeching* ")
    sleep(1)
    print(f"{my_name} drives off in their Little Red Corvette...")
elif budget >= 50 and budget <= 75:
    print(f"{date_name}: Call me tomorrow!")
    sleep(1)
    print(f"{date_name}: I'll see if I can clear my schedule.")
else:
    print(f"{date_name}: Definitely!")
    sleep(1)
    print(f"{date_name}: What time are you coming over?")
