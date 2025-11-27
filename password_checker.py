import re

def check_password_strength(password):
    strength = 0
    feedback = []

    # Criteria checks
    if len(password) >= 8:
        strength += 1
    else:
        feedback.append("Password should be at least 8 characters long.")

    if re.search(r"[A-Z]", password):
        strength += 1
    else:
        feedback.append("Add at least one uppercase letter (A-Z).")

    if re.search(r"[a-z]", password):
        strength += 1
    else:
        feedback.append("Add at least one lowercase letter (a-z).")

    if re.search(r"[0-9]", password):
        strength += 1
    else:
        feedback.append("Include at least one number (0-9).")

    if re.search(r"[\W_]", password):
        strength += 1
    else:
        feedback.append("Add at least one special character (!, @, #, $, etc).")

    # Strength decision
    if strength <= 2:
        verdict = "Weak"
    elif strength == 3:
        verdict = "Medium"
    elif strength == 4:
        verdict = "Strong"
    else:
        verdict = "Very Strong"

    return verdict, feedback


print("=== PASSWORD COMPLEXITY CHECKER ===")
user_password = input("Enter a password to check: ")

result, tips = check_password_strength(user_password)

print("\nPassword Strength:", result)

if tips:
    print("\nSuggestions to improve your password:")
    for t in tips:
        print("- " + t)
else:
    print("Your password is very strong! No improvements needed.")
