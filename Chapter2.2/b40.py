nums :tuple[int] = (1,2,3,4,5,6,7,8,9,10,11,12)

whr_to_sep = len(nums)//2

tp1:tuple[int] = nums[:whr_to_sep]
tp2:tuple[int] = nums[whr_to_sep:]

print(tp1)
print(tp2)
