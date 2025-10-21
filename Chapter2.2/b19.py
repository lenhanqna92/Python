import re

with open("./resource/lorem.txt", "r", encoding="utf-8") as f:
    text = f.read().lower()

words : list = re.findall(r"\b\w+\b", text)

freq : dict = {}
for w in words:
    if w in freq:
        freq[w] += 1
    else:
        freq[w] = 1

top10 : list= sorted(freq.items(), key=lambda x: x[1], reverse=True)[:10]

for word, count in top10:
    print(word, count)