"""A class that can be used to represent a car."""


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


class Battery:
    """A simple attempt to model a battery for an electric car."""

    def __init__(self, battery_size=75):
        """Initialize battery's attribute."""
        self._battery_size = battery_size
        self._range = 0

    def describe_battery(self):
        """Print a statement describing the battery size of the car."""
        print(f"This car has a {self._battery_size}-kWh battery.")

    def get_range(self):
        """Print a statement about the range this battery provides."""
        if self._battery_size == 75:
            self._range = 260
        elif self._battery_size == 100:
            self._range = 315
        print(f"This can go about {self._range} miles on a full charge.")

    def upgrade_battery(self):
        """Add extra capacity to the battery of a car."""
        if self._battery_size == 75:
            self._battery_size += 25


class ElectricCar(Car):
    """Represents aspects of a car, specific to electric vehicles."""

    def __init__(self, make, model, year):
        """Initialize attributes of parent class.
        Then initialize attributes specific to an electric car."""
        super().__init__(make, model, year)
        self.battery = Battery()

    # def describe_battery(self):
    #     """Print a statement describing the battery size of the car."""
    #     print(f"This car has a {self._batter_size}-kWh battery.")

    def fill_gas_tank(self):
        """Electric cars don't have gas tanks."""
        print("This car does not need gas tank.")
