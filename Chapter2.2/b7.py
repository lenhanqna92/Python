num = int(input('nhap so: '))
bac = int(input('nhap bậc của số: '))
sum = 0
temp = num
while temp > 0:
   digit = temp % 10
   sum += digit ** bac
   temp //= 10
if num == sum:
   print(num, "is Amstrong, level : " + str(bac))
else:
   print(num, "is not Amstrong")

