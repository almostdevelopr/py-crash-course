for value in range(1, 5):
    print(value)


# even numbers
even_numbers = list(range(2, 11, 2))
print(f"Even numbers: {even_numbers}")

# odd numbers
some_numbers = list(range(1, 10))
print(f"Numbers: {some_numbers}")

squares = []
for value in range(1, 11):
    # square = value**2
    # squares.append(square)
    squares.append(value**2)

print(f"Squares (FOR LOOP): {squares}")

# list comprehension
squares_comp = [value**2 for value in range(1, 11) if value % 2 == 0]
print(f"Even Squares (LIST COMPREHENSION): {squares_comp}")
