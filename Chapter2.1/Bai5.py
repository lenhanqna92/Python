st = input("Nhap chuoi: ")
st5f = st[:5]
st5l = st[len(st) - 5 : ]
st_4st_1 = 4 * (st + " ")
st_4st_4 = 4 * (st + "\n ")

print("Chuoi cua ban la: " + st)
print("5 ki tu dau tien cua chuoi: " + st5f)
print("5 ki tu cuoi cung cua chuoi: " + st5l)
print("4 chuoi lap tren 1 dong: " + st_4st_1)
print("4 chuoi lap tren 4 dong:\n" + st_4st_4)
