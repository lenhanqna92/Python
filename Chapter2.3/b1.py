fn = 'sample.txt'
try: 
    with open(fn) as file:
        contents = file.read()
except FileNotFoundError:
    msg = "file " + fn + ' khong ton tai'
    print(msg)