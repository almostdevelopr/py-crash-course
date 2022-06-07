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

print(f"Squares: {squares}")
