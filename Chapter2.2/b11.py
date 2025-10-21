listnum : list = list()

while True :
    inp : any = input("Enter numbers:")
    if(inp == "done"): break
    else: listnum.append(int(inp))

SUM : int = sum(listnum)

print (f"avg: {SUM/len(listnum)}")