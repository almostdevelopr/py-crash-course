cars = ["mercedes", "yamaha", "honda", "bmw", "audi"]
for car in cars:
    if car == "bmw":
        print(car.upper())
    else:
        print(car.title())

# toppings.py
requested_topping = "mushroom"
if requested_topping != "anchovies":
    print("Hold the anchovies!")

# magic_numbers.py
answer = 17
if answer != 42:
    print("That is not the correct answer. Please try again!")

# in keyword
toppings = ["mushrooms", "onions", "pineapple"]
print("mushroom" in toppings)

# banned users
banned_users = ["andrew", "carolina", "david"]
user = "marie"
if user not in banned_users:
    print(f"{user.title()}, you can post a response if you wish.")

game_active = True
can_edit = False

# with the help of boolean values we can track state of a program
# or a particular condition that is important to your program

car = "subaru"
print("Is car=='subaru? I predict True.")
print(car == "subaru")

age = 15
if age >= 18:
    print("You are old enough to vote.")
    print("Have yo regisetred to vote yet?")
else:
    print("Sorry, you are too young to vote.")
    print("Please regiester to vote as soon as you turn 18!")
