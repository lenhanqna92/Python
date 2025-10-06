st = input("Input your string: ")
st_upper = 0
st_lower = 0
st_space = 0

for c in st :
    if c.isupper():
        st_upper += 1
    elif c.islower():
        st_lower += 1
    elif c == " ":
        st_space += 1
    else:
        pass

print('Sum of upper character is: ', st_upper)
print('Sum of lower character is: ', st_lower)
print('Sum of whitespace character is: ', st_space)