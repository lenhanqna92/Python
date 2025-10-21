nums : list[int] = [1,2,6,22,99] 

def to_binary_number(num:int)->str:
    return bin(num)[2:]

for num in nums:
    print(f"{num}:->{to_binary_number(num)}")