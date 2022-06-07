million_numbers = list(range(1, 1000001))
print(f"Initial number: {min(million_numbers)}")
print(f"Terminal number: {max(million_numbers)}")
print(f"Sum of one million numbers: {sum(million_numbers)}")

odd_numbers = list(range(1, 20, 2))
for num in odd_numbers:
    print(num)


print("\n")

threes = []
for num in range(3, 31):
    threes.append(num * 3)
print(f"threes: {threes}")


# cubes
cubes = [val**3 for val in range(1, 11)]
print("Cubess--->>")
for cube in cubes:
    print(cube)
