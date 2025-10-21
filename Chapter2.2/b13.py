lines:list = []
print("enter(blank to exit):")

while True:
    line:str = input()
    if line == "":   
        break
    lines.append(line.upper())  

print("\nRS:")
for l in lines:
    print(l)