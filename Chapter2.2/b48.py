def avg(a: float, b: float, c: float) -> float:
    return (a + b + c) / 3


x = float(input("Enter n1: "))
y = float(input("Enter n2: "))
z = float(input("Enter n3: "))

avg = avg(x, y, z)
print("avg:", avg)
