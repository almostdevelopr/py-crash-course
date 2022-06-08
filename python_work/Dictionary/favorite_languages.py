favorite_languages = {
    "jen": "python",
    "sarah": "c",
    "edward": "ruby",
    "phil": "python",
}

print(f"Sarah's favorite language is {favorite_languages['sarah'].title()}")
favorite_language = favorite_languages.get("sara", "No sara value is assigned.")
print(favorite_language)

for name, language in favorite_languages.items():
    print(f"{name.title()}'s favorite language is {language.title()}")

for name in favorite_languages.keys():
    print(name.title())

print("")

friends = ["sarah", "phil"]
for name, language in favorite_languages.items():
    print(f"Hi {name.title()}")
    if name in friends:
        language = favorite_languages[name].title()
        print(f"{name.title()}, I see you love {language.title()}!")

if "erin" not in favorite_languages.keys():
    print("Erin, please take our poll!")
