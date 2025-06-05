import re
import getpass

def check_password_strength(password):
    criteria = {
        "length": len(password) >= 8,
        "uppercase": bool(re.search(r"[A-Z]", password)),
        "lowercase": bool(re.search(r"[a-z]", password)),
        "number": bool(re.search(r"[0-9]", password)),
        "special": bool(re.search(r"[!@#$%^&*(),.?\\\":{}|<>]", password)),
    }

    print("\nPassword Strength Check:")
    for key, passed in criteria.items():
        print(f"[{'+' if passed else '-'}] {key.capitalize()} requirement: {'OK' if passed else 'Missing'}")

    strength = sum(criteria.values())

    if strength <= 2:
        return "WEAK"
    elif strength == 3 or strength == 4:
        return "MODERATE"
    else:
        return "STRONG"

if __name__ == "__main__":
    print(" Password Strength Checker ")
    password = getpass.getpass("Enter your password: ")
    rating = check_password_strength(password)
    print(f"\n Strength: {rating}")
