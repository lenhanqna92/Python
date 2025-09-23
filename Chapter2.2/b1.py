#kiem tra so chan le
n = int(input("Nhap vao so nguyen duong: "))

if n % 2 == 0 and n > 0:
    print("Day la so chan !")
elif n < 0:
    print("Ban phai nhap so nguyen duong !")
else:
    print("Day la so le !")
