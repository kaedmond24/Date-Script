##############################################################################################################################
# Created by Kevin Edmond.
#
# To Be Updated
# To Be Updated
#
#
# Please read README.md for full notes on script.
#
###############################################################################################################################

from time import sleep

date_name = input("Date's Name: ").capitalize()

# starting budget
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
print("Waiter: Can I take your order?")

# Show menu
print(restaurants[restaurant_level]['menu'])

# Get menu orders
my_menu_order = input("Your Menu Order: ").lower()
order_total += restaurants[restaurant_level]['menu'][my_menu_order]

date_menu_order = input("Date's Menu Order: ").lower()
order_total += restaurants[restaurant_level]['menu'][date_menu_order]

# Get Drink Orders
print("...and what would you like to drink?")
print(restaurants[restaurant_level]['drink'])

# Get Drink Orders
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
(f"Leaving {restaurants[restaurant_level]['name']}...")

# Show Remaining Budget
print("Checking bank app...")
print(f"You have ${budget} in your account.")
sleep(2)


print(f"Hey {date_name}, want to go out again sometime?")
sleep(1)
if budget < 50:
    print("Nah... I'm Good!")
    sleep(1)
    print("But... *You drive off in your Little Red Corvette*")
elif budget >= 50 and budget <= 75:
    print("Call me tomorrow!")
    print("I'll see if I can clear my schedule.")
else:
    print("Definitely!")
    print("What time are you coming over?")
