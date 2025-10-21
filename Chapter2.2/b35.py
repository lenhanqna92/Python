numbers_str: str = input("Enter numbers: ")

numbers: list[int] = [int(x) for x in numbers_str.split(",")]

odd_numbers: list[int] = [n for n in numbers if n % 2 != 0]

print("Odd_nums:", odd_numbers)