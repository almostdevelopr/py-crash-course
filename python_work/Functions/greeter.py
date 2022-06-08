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

# models printing for 3D company
def print_models(unprinted_designs, completed_models):
    """
    Simulate printing each design, untill none are left.
    Move each design to completed models after printing.
    """
    while unprinted_designs:
        current_design = unprinted_designs.pop()
        print(f"Printing models: {current_design}")
        completed_models.append(current_design)


def show_completed_models(completed_models):
    """Sow all the models that were printed."""
    print("\nThe following models have been printed.")
    for completed_model in completed_models:
        print(completed_model)


unprinted_designs = ["phone case", "robot pendant", "dodecahedron"]
completed_models = []

print_models(unprinted_designs, completed_models)
show_completed_models(completed_models)
