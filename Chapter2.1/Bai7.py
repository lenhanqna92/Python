#tinh dien tich tam giac
from math import sin, pi

a = float(input("Nhap do dai canh a: "))
b = float(input("Nhap do dai canh b: "))
c = float(input("Nhap do dai canh c: "))

print("Luu y: tong 3 goc khong lon hon 180 do")
d = float(input("Nhap do lon goc a: "))
e = float(input("Nhap do lon goc b: "))
f = float(input("Nhap do lon goc c: "))

goca = d * pi / 180
gocb = e * pi / 180
gocc = f * pi / 180

ct1 = (0.5 * a * b * sin(gocc))
ct2 = (0.5 * a * c * sin(gocb))
ct3 = (0.5 * b * c * sin(goca))

tong = int(d + e + f)
if tong != 180:
    print("tam giac khong hop le !")
else:
    print("Tinh dien tich theo goc c: " , ct1)
    print("Tinh dien tich theo goc b: " , ct2)
    print("Tinh dien tich theo goc a: " , ct3)
