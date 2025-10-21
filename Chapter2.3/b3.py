def count_words(filename):
    try:
        with open(filename) as file:
            contents = file.read()
    except FileNotFoundError:
        print('not found')
    else:
        tu = contents.split()
        so_tu = len(tu)
        print("File " + filename + " co " + str(so_tu) + "tu")
        
filenames = ['sample.txt', 'sample2.txt', 'sample3.txt']
for filename in filenames:
    count_words(filename)          