class Restaurant:
    """A simple attemp to model a restaurant."""

    def __init__(self, restaurant_name, cuisine_type):
        """Initialize the restaurant name and cuisine type"""
        self._restaurant_name = restaurant_name
        self._cuising_type = cuisine_type

    def describe_restaurant(self):
        """Simulate to describe restaurant."""
        print(f"\nThe name of the restaurant is {self._restaurant_name.title()}")
        print(f"The famous cuisine of the restaurant is {self._cuising_type.title()}")

    def open_restaurant(self):
        """This is will inform the users if restaurant is open or closed."""
        print(f"\n{self._restaurant_name.title()} is open now!")


# instantiate
restaurant_0 = Restaurant("raddison blu", "indian")
restaurant_1 = Restaurant("hyat", "italian")
restaurant_2 = Restaurant("club mahindra", "continental")

# 1
restaurant_0.describe_restaurant()
restaurant_0.open_restaurant()
# 2
restaurant_1.describe_restaurant()
# 3
restaurant_2.describe_restaurant()
