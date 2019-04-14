def findAll(filename,key):
    infile = open(filename,"r")
    outfile = open("result.txt","w")
    text = infile.read()
    position = text.find(key)
    t = ""
    while(text.find(key,position) != -1):
        a = text.find(key,position)
        position = a + 1
        print(a)
        t = t + key + " is at "+ str(a) + ".\n"
    if (position == -1):
        outfile.write(key + " is not found.\n")
    else:
        outfile.write(t)
    outfile.close()
    infile.close()
    print("Done")

# findAll('article.txt','computer')
# """
# computer is at 3222.
# computer is at 3310.
# computer is at 3554.
# computer is at 3678.
# computer is at 6162.
# computer is at 10926.
# """
# findAll('article.txt','Whole Earth')
# """
# Whole Earth is at 10686.
# Whole Earth is at 11231.
# """
# findAll('article.txt','Apple')
# """
# Apple is at 4333.
# Apple is at 4408.
# Apple is at 4695.
# Apple is at 5539.
# Apple is at 5718.
# Apple is at 6299.
# Apple is at 6332.
# Apple is at 6398.
# Apple is at 6557.
# """
findAll('article.txt','apple')
# """
# apple is not found.
# """