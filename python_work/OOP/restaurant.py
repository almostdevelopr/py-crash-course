class Restaurant:
    """A simple attemp to model a restaurant."""

    def __init__(self, restaurant_name, cuisine_type):
        """Initialize the restaurant name and cuisine type"""
        self._restaurant_name = restaurant_name
        self._cuising_type = cuisine_type

    def describe_restaurant(self):
        """Simulate to describe restaurant."""
        print(f"The name of the restaurant is {self._restaurant_name.title()}")
        print(f"The famous cuisine of the restaurant is {self._cuising_type.title()}")

    def open_restaurant(self):
        """This is will inform the users if restaurant is open or closed."""
        print(f"\n{self._restaurant_name.title()} is open now!")


# instantiate
restaurant = Restaurant("raddison blu", "indian")

restaurant.describe_restaurant()
restaurant.open_restaurant()
