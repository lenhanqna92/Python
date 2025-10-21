di :dict = {
    "lower":0,
    "upper":0
}

inp : str = str(input("Enter string: "))

for char in inp:
    if(char.isupper()): di["upper"]+=1
    if(char.islower()): di["lower"]+=1

print(di)
