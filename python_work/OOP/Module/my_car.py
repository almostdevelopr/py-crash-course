import car

my_audi = car.Car("audi", "a4", 2019)
print(my_audi.get_descriptive_name())

my_tesla = car.ElectricCar("tesla", "roadster", "2020")
print(my_tesla.get_descriptive_name())
