current_users = ["aric", "adam", "ross", "admin"]
new_users = ["ADMIN", "Ross", "rachel"]

# check for case sensitive test
new_users_lowercase = []
for new_user in new_users:
    new_users_lowercase.append(new_user.lower())
# print(new_users_lowercase)

for new_user in new_users_lowercase:
    if new_user in current_users:
        print("You need to enter a new username.")
    else:
        print("Username is available.")
