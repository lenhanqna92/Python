words_dict: dict[str, None] = {}

while True:
    word: str = input("Enter a word (press Enter to stop): ").strip()
    if word == "":
        break
    words_dict[word] = None   

print("Words entered (unique, in order):")
for w in words_dict.keys():
    print(w)