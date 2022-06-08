def greet_user(username):
    """Display a simple greeting."""
    print(f"Hello, {username.title()}!")


# greet_user("jessie")


def get_formatted_name(first_name, last_name):
    """Returns a full name, neatly formatted."""
    full_name = f"{first_name} {last_name}"
    return full_name.title()


musician = get_formatted_name("jimi", "hendrix")
print(musician)
