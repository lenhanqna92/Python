#hien thi so gio lanh 13,12 + 0,6215Ta - 11,37V0.16 + 0,3965Ta V0.16
t = float(input("Nhap nhiet do khong khi(do C): "))
v = float(input("Nhap toc do gio(km/h): "))
w = 13.12 + (0.6215 * t) - (11.37 * (v ** 0.16)) + (0.3965 * t * (v ** 0.16))
print(f"So gio lanh la: {w:.0f}")
