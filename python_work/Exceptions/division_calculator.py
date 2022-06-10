"""This module shows behaviour of the try-except block."""
try:
    print(5 / 0)
except ZeroDivisionError:
    print("You cannnot divide by zero.")
print("outside of try-except block")
