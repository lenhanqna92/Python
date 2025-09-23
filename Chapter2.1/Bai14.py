from math import log10
a = int(input("Nhap a: "))
b = int(input("Nhap b: "))
tong = a + b
hieu = a - b
tich = a * b
thuong = a / b
du = a % b
log = log10(a)
mu = a ** b
print("Tổng của a và b:",tong, "\nHiệu của a và b",hieu, "\nTích của a và b:",tich,
      "Thương của a chia cho b:",thuong, "\nChia lay du:",du, "\nlog10a:",log,
      "\na mu b:",mu)