import getpass
import string


def check_password(password):
    suggestions = []
    score = 0

    if len(password) >= 12:
        score += 1
    else:
        suggestions.append("Use at least 12 characters.")

    if any(char.islower() for char in password):
        score += 1
    else:
        suggestions.append("Add a lowercase letter.")

    if any(char.isupper() for char in password):
        score += 1
    else:
        suggestions.append("Add an uppercase letter.")

    if any(char.isdigit() for char in password):
        score += 1
    else:
        suggestions.append("Add a number.")

    if any(char in string.punctuation for char in password):
        score += 1
    else:
        suggestions.append("Add a symbol, such as ! or #.")

    if score <= 2:
        rating = "Needs improvement"
    elif score <= 4:
        rating = "Getting stronger"
    else:
        rating = "Good"

    return rating, suggestions


password = getpass.getpass("Enter a sample password (input hidden): ")
rating, suggestions = check_password(password)

print(f"\nRating: {rating}")

if suggestions:
    print("Suggestions:")
    for suggestion in suggestions:
        print(f"- {suggestion}")
else:
    print("It meets all the checks.")