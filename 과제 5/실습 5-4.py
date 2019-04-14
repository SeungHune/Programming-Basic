def oneSentencePerLine(filename) :
    infile = open(filename,"r")
    outfile = open("result.txt","w")
    text = infile.read()
    count1 = 0
    count2 = 0
    while (True):
        a,b,c = text.partition(".")
        if (a.find("?") != -1):
            q,w,e = a.partition("?")
            outfile.write((q+w).strip()+"\n\n")
            count1 = count1 + 1
            text = e + b + c
        else:
            outfile.write((a+b).strip()+"\n\n")
            count2 = count2 + 1
            text = c
        if (c == ""):
            break
    print(count1)
    print(count2)
    count = count1 + count2
    print(count)
    outfile.write("There are " + str(count) + " sentences in total.\n")
    outfile.close()
    infile.close()
    print("Done")

oneSentencePerLine("article.txt")