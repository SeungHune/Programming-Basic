def findAllSentences(filename,key) :
    infile = open(filename,"r")
    outfile = open("result.txt","w")
    text = infile.read()
    t = ""
    count = 0
    while(True):
        a,b,c = text.partition(".")
        if (a.find(key) != -1):
            t = t + "\'" + key + "\'" + " appears 1 time.\n" + (a+b).strip() + "\n\n"
            count = count + 1
            text = c
        else:
            text = c
        if(text.find(key) == -1):
            break
    ans = t + "\'" + key + "\'" + " appears " + str(count) + " times in " + str(count) + " sentences.\n"
    outfile.write(ans)
    outfile.close()
    infile.close()
    print("done")

findAllSentences("article.txt", "computer")
# def findAll(filename,key):
#     infile = open(filename,"r")
#     outfile = open("result.txt","w")
#     text = infile.read()
#     position = text.find(key)
#     t = ""
#     while(text.find(key,position) != -1):
#         a = text.find(key,position)
#         position = a + 1
#         print(a)
#         t = t + key + " is at "+ str(a) + ".\n"
#     if (position == -1):
#         outfile.write(key + " is not found.\n")
#     else:
#         outfile.write(t)
#     outfile.close()
#     infile.close()
#     print("Done")