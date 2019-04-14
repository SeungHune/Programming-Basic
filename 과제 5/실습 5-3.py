def findAllNCount(filename,key):
    infile = open(filename,"r")
    outfile = open("result.txt","w")
    text = infile.read()
    position = text.find(key)
    count = 0
    while (text.find(key,position) != -1):
        a = text.find(key,position)
        position = a + 1
        count = count + 1
    if (count == 0):
        outfile.write((key + " is not found"))
    elif (count == 1):
        outfile.write(key + " is found " + str(count) + " time.\n")
    else:
        outfile.write(key + " is found " + str(count) + " times.\n")
    print(key + " is found " + str(count) + " times.\n")
    outfile.close()
    infile.close()
    print("Done")

# def findAll(filename,key):
#     infile = open(filename,"r")
#     outfile = open("result.txt","w")
#     text = infile.read()
#     position = text.find(key)
#     t = ""
#
#     while(text.find(key,position) != -1):
#         a = text.find(key,position)
#         position = a + 1
#         print(a)
#         t = t + str(a) + ", "
#     ans = t[:-2]
#     if (position == -1):
#         outfile.write(key + " is not found")
#     else:
#         outfile.write("at " + ans + ".")
#     outfile.close()
#     infile.close()
#     print("Done")

findAllNCount('article.txt','.') # computer is found 6 times.
findAllNCount('article.txt','?') # Whole Earth is found 2 times.
# findAllNCount('article.txt','Apple') # Apple is found 9 times.
# findAllNCount('article.txt','commencement') # commencement is found 1 time.
# findAllNCount('article.txt','apple') # apple is not found