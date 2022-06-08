requested_toppings = ["mushrooms", "green peppers", "extra cheese"]
unavailable_toppings = ["green peppers", "mushrooms"]

# checking that a list is not empty
for requested_topping in requested_toppings:
    if requested_topping in unavailable_toppings:
        print(f"Sorry, we are out of {requested_topping}")
    else:
        print(f"Adding {requested_topping}")

print("\nYour pizza is ready!")
