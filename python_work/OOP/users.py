class User:
    """A simple attempt to model user."""

    def __init__(self, first_name, last_name, location):
        """Initialize first name and last name for the user."""
        self._first_name = first_name
        self._last_name = last_name
        self._location = location
        self._full_name = f"{self._first_name.title()} {self._last_name.title()}"
        self._login_attempts = 0

    def increment_login_attempts(self):
        """Increment the login attempt counter by 1."""
        self._login_attempts += 1
        # print(self._login_attempts)

    def reset_login_attempts(self):
        """Resets the login attempts to 0."""
        self._login_attempts = 0

    def print_login_attempts(self):
        """Prints the login attempts made."""
        print(f"Login attempts: {self._login_attempts}")

    def describe_user(self):
        """This will describe the user with information critical for the same
        user.
        """
        # full_name = f"{self._first_name.title()} {self._last_name.title()}"
        # print(f"User name: {self._first_name.title()} {self._last_name.title()}")
        print(f"User name: {self._full_name}")
        print(f"{self._full_name} lives in {self._location}")

    def greet_user(self):
        """Greets user with personalized message."""
        print(f"\nWelcome, {self._full_name}!")


user = User("eric", "william", "LA")
user.describe_user()
user.greet_user()

user_0 = User("eric", "adams", "san francisco")
user_0.describe_user()
user_0.greet_user()
user_0.increment_login_attempts()
# print()
# user_0.reset_login_attempts()
user_0.print_login_attempts()
