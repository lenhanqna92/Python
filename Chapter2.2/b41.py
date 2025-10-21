nums : tuple[int] = (1,2,3,4,5,6,7,8,9,10)

even_nums : tuple[int] = tuple(i for i in nums if(i%2==0))

print(even_nums)