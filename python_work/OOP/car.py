class Car:
    """A simple attempt to represent a car."""

    def __init__(self, make, model, year):
        """Initialize car attributes."""
        self._make = make
        self._model = model
        self._year = year
        self._odometer_reading = 0

    def get_descriptive_name(self):
        """Return a neatly formatted descriptive name."""
        long_name = f"{self._make} {self._model} {self._year}"
        return long_name.title()

    def read_odometer(self):
        """Print a statement showing the car's mileage."""
        print(f"This car has {self._odometer_reading} miles on it.")

    def update_odometer(self, mileage):
        """Set the odometer reading to a given value.
        Rejects the change if it attempts to the odometer back."""
        if mileage >= self._odometer_reading:
            self._odometer_reading = mileage
        else:
            print("You cannot roll back an odometer.")

    def increment_odometer(self, miles):
        """Add the given amount to the odometer reading."""
        if miles >= 0:
            self._odometer_reading += miles
        else:
            print("You cannot add negative miles to roll back an odometer.")

    def fill_gas_tank(self):
        """Inform the driver to fill the gas tank."""
        print("Please fill the gas tank.")


class ElectricCar(Car):
    """Represents aspects of a car, specific to electric vehicles."""

    def __init__(self, make, model, year):
        """Initialize attributes of parent class.
        Then initialize attributes specific to an electric car."""
        super().__init__(make, model, year)
        self._batter_size = 75

    def describe_battery(self):
        """Print a statement describing the battery size of the car."""
        print(f"This car has a {self._batter_size}-kWh battery.")

    def fill_gas_tank(self):
        """Electric cars don't have gas tanks."""
        print("This car does not need gas tank.")


my_tesla = ElectricCar("tesla", "model s", 2019)
print(my_tesla.get_descriptive_name())
my_tesla.describe_battery()

my_new_car = Car("audi", "a4", "2019")
print(my_new_car.get_descriptive_name())

# change value of _odometer_reading directly
# my_new_car._odometer_reading = 23

# change value of _odometer_reading through a method
my_new_car.update_odometer(24_500)
my_new_car.update_odometer(14)
my_new_car.increment_odometer(-23)
my_new_car.read_odometer()
