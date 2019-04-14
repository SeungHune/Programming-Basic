def searchWidestGap(list):
    gap = 0
    index = 0
    if (list == []):
        return (0,-1)
    for i in range(len(list)):
        if (list[-1] == list[i]):
            pass
        else:
            if (list[i] < list[i+1]):
                a = list[i+1] - list[i]
            if(gap < a):
                gap = a
                index = i
            else:
                pass
    return (gap, index)
print(searchWidestGap([]))
print(searchWidestGap([3]))
print(searchWidestGap([3,5,8,20,22]))
print(searchWidestGap([3,5,8,20,22,34,37,40]))


# import random
# def testSearchWidestGap():
#     db = random.sample(range(500),100)
#     print("Searching the widest gap...")
#     db.sort()
#     print(db)
#     index, gap = searchWidestGap(db)
#     print("The widest gap is:", gap)
#     print("between", db[index], "and", db[index+1])
#     print("at", index)
#
# testSearchWidestGap()