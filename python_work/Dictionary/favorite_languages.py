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
