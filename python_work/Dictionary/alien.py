alien_0 = {"color": "green", "points": 5}

print(alien_0["color"])
print(alien_0["points"])

# print("\n")

new_points = alien_0["points"]
print(f"You just earned {new_points} points!")

print("")

print(alien_0)

alien_0["x_position"] = 0
alien_0["y_position"] = 25
alien_0["speed"] = "slow"
print(alien_0)
print(f"Original position: {alien_0['x_position']}")

if alien_0["speed"] == "slow":
    x_increment = 1
elif alien_0["speed"] == "medium":
    x_increment = 2
else:
    # must be fast alien
    x_increment = 3

# The new position is the old_position plus the increment
alien_0["x_position"] = alien_0["x_position"] + x_increment

print(f"New position: {alien_0['x_position']}")
