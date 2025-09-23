a = float(input("Nhap so a: "))
b = float(input("Nhap so b: "))
c = float(input("Nhap so c: "))
print("Cac so ban vua nhap la: ",a, b, c)

if a > b and a > c:
    print("a la so lon nhat")
elif b > a and b > c:
    print("b la so lon nhat")
else:
    print("c la so lon nhat")

