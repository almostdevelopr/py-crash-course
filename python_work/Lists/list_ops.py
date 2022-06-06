motorcycles = ["honda", "yamaha", "suzuki"]
print(motorcycles)

# add element at the end of the list
motorcycles.append("ducati")
print(motorcycles)

cars = []
cars.append("honda")
cars.append("maruti")
cars.append("audi")
print(cars)

# inserting element into a list -> insert(index,element)
cars.insert(1, "bmw")
print(cars)

# deleting form the list at given index
del cars[1]
del cars[2]
print(cars)


# pop() -> delete item from list and use after deleting
print("****** POP() ******")
print(motorcycles)
popped_motorcycle = motorcycles.pop()
print(motorcycles)
print(popped_motorcycle)

last_owned = motorcycles.pop()
msg_motorcycle = f"The last motocycle I owned was a {last_owned.title()}"
print(msg_motorcycle)


too_expensive = "yamaha"
motorcycles.remove(too_expensive)
print(f"\nA {too_expensive.title()} is too expensive for me.")
print(motorcycles)
