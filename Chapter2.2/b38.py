negatives: list[int] = []
zeros: list[int] = []
positives: list[int] = []

while True:
    line: str = input("Enter nums (blank-1 to stop): ").strip()
    if line == "":
        break
    n: int = int(line)
    if n < 0:
        negatives.append(n)
    elif n == 0:
        zeros.append(n)
    else:
        positives.append(n)

ordered_numbers: list[int] = negatives + zeros + positives

print("Reordered numbers:")
for num in ordered_numbers:
    print(num)