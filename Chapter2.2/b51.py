def is_good(password: str) -> bool:
    if len(password) < 8:
        return False

    special = "!@#$%^&*()_-+=,./?:'\"{}[]\\|"
    has_upper = any(c.isupper() for c in password)
    has_lower = any(c.islower() for c in password)
    has_digit = any(c.isdigit() for c in password)
    has_special = any(c in special for c in password)

    print("Upper:", has_upper, "Lower:", has_lower, "Digit:", has_digit, "Special:", has_special)

    return has_upper and has_lower and has_digit and has_special
if __name__ == "__main__":
    pw = input("Enter a password: ")
    if is_good(pw):
        print("This is a good password.")
    else:
        print("This is NOT a good password.")