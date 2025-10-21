total = 0
count = 0
while(True):
    inp = input("Nhap số: ")
    if inp == "done":
        break
    print(inp)
    value = float(inp)
    total += value
    count += 1
    
aver = total / count
print("trung binh cua cac so la: ", aver)