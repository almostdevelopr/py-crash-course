requested_toppings = ["olives", "onions"]
unavailable_toppings = ["green peppers", "mushrooms"]

# checking that a list is not empty
if requested_toppings:
    for requested_topping in requested_toppings:
        if requested_topping in unavailable_toppings:
            print(f"Sorry, we are out of {requested_topping}")
        else:
            print(f"Adding {requested_topping}")
else:
    print("Are you sure you want a plain pizza?")
print("\nYour pizza is ready!")
