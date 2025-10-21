def is_palindrom(st:str)->bool:
    return st == st[::-1]

data : list[str] = ["anna", "civic", "level", "hannah", "linh"]

for st in data :
    print(f"Palindrom: {is_palindrom(st)}")