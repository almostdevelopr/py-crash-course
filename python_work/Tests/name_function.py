"""A module for function to test."""


def get_formatted_name(first_name, last_name, middle_name=""):
    """Generate neatly formatted name."""
    if middle_name:
        full_name = f"{first_name} {middle_name} {last_name}"
    else:
        full_name = f"{first_name} {last_name}"
    return full_name.title()
