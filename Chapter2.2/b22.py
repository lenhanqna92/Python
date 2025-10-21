def make_list () -> list:
    arr : list = []
    for i in range(1,21):
        arr.append(i**2)
    return arr
arr:list = make_list()

print(arr[:5]+arr[len(arr)-5:])