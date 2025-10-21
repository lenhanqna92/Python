def Factorial(num:int)->int:
    if(num == 0):
        return 1
    return(num*Factorial(num-1))
print(Factorial(8))
