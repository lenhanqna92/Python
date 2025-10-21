START = 200
END = 301

def is_all_even(num:int)->bool:
    num_str : str = str(num)
    return (int(num_str[0])%2 == 0) and (int(num_str[1])%2 == 0) and (int(num_str[2])%2 == 0)

arr : list = []
for num in range (START,END):
    if(is_all_even(num=num)):
        arr.append(str(num))
print(",".join(arr))