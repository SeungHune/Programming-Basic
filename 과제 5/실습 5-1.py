def findLast(filename,key):
    infile = open(filename, "r")
    content = infile.read()
    t = 0
    while (content.find(key,t) != -1):
        x = content.find(key,t)
        t = x + 1
        y = str(x)
    result = open("result.txt", "w")
    if (content.find(key) == -1):
        result.write(key +" is not found.")
    else:
        result.write(key + " is at " + y + " the last time.")
    infile.close()
    result.close()


findLast('article.txt','computer') # computer is at 10926 the last time.
# findLast('article.txt','Whole Earth') # Whole Earth is at 11231 the last time.
# findLast('article.txt','Apple') # Apple is at 6557 the last time.
# findLast('article.txt','apple') # apple is not found.