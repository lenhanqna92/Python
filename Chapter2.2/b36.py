numbers: list[int] = []

while True:
    n: int = int(input("Enter number (0 to stop): "))
    if n == 0:
        break
    numbers.append(n)
numbers.sort()

# Hiển thị kết quả
print("print:6")
for num in numbers:
    print(num)