import re

print("===== PASSWORD STRENGTH CHECKER =====")

password = input("Enter your password: ")

score = 0
suggestions = []

# Check length
if len(password) >= 8:
    score += 1
else:
    suggestions.append("Use at least 8 characters.")

# Check uppercase
if re.search(r"[A-Z]", password):
    score += 1
else:
    suggestions.append("Add at least one uppercase letter (A-Z).")

# Check lowercase
if re.search(r"[a-z]", password):
    score += 1
else:
    suggestions.append("Add at least one lowercase letter (a-z).")

# Check number
if re.search(r"[0-9]", password):
    score += 1
else:
    suggestions.append("Add at least one number (0-9).")

# Check special character
if re.search(r"[^A-Za-z0-9]", password):
    score += 1
else:
    suggestions.append("Add at least one special character (!, @, #, $, etc.).")

# Check common/simple passwords
common_passwords = ["password", "12345678", "qwerty", "password123", "admin"]

if password.lower() in common_passwords:
    print("\nStrength: Very Weak")
    print("Suggestion: Avoid common passwords.")
else:
    if score <= 2:
        strength = "Weak"
    elif score == 3:
        strength = "Medium"
    elif score == 4:
        strength = "Strong"
    else:
        strength = "Very Strong"

    print("\nPassword Strength:", strength)

    if suggestions:
        print("\nSuggestions to improve your password:")
        for suggestion in suggestions:
            print("-", suggestion)
    else:
        print("\nYour password meets all basic strength checks!")