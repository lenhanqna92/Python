filename = 'sample.txt'
try:
    with open('sample.txt') as file:
        content = file.read()
except FileNotFoundError:
    print("not found")
else:
    tu = content.split()
    so_tu = len(tu)
    print("File " + filename + " có " + str(so_tu) + " từ.")