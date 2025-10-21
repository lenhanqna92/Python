def main() -> None:
    letter: str = str(input("Enter a single letter: ")).lower().strip()[:1]

    if letter in ("a", "e", "i", "o", "u"):
        print(f"'{letter}' is a vowel.")
    elif letter == "y":
        print(f"'{letter}' can be either a vowel or a consonant.")
    elif letter.isalpha():  
        print(f"'{letter}' is a consonant.")
    else:
        print("You did not enter a valid letter.")
        