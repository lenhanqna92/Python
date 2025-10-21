def make_list () -> list:
    arr : list = []
    for i in range(1,21):
        arr.append(i**2)
    return arr
print (make_list())