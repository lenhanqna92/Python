def compare_strings(s1: str, s2: str) -> None:
    if len(s1) > len(s2):
        print(s1)
    elif len(s2) > len(s1):
        print(s2)
    else:
        print(s1)
        print(s2)


# --- Example usage ---
str1:str = str(input("Enter s1: "))
str2:str = str(input("Enter s2: "))

compare_strings(str1, str2)