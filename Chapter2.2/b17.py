di :dict = {
    "alphas":0,
    "digits":0
}

inp : str = str(input("Enter string: "))

for char in inp:
    if(char.isalpha()): di["alphas"]+=1
    if(char.isdigit()): di["digits"]+=1

print(di)