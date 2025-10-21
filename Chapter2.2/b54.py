def format_list(words: list[str]) -> str:
    if not words:
        return ""
    if len(words) == 1:
        return words[0]
    if len(words) == 2:
        return words[0] + " and " + words[1]
    return ", ".join(words[:-1]) + " and " + words[-1]


def main():
    words = []
    print("Enter words (press Enter with no input to stop):")
    while True:
        word = input("Word: ").strip()
        if word == "":
            break
        words.append(word)

    result = format_list(words)
    print("Formatted list:", result)


if __name__ == "__main__":
    main()
    