def makeset(xs):
    ys = []
    for x in xs:
        if x not in ys:
            ys.append(x)
    return ys

def union(xs,ys):
    pass # 이 부분을 채우자
    x = makeset(xs)
    y = makeset(ys)
    return makeset(x+y)


# import random
# s1 = makeset([random.randrange(10) for _ in range(10)])
# print(s1)
# s2 = makeset([random.randrange(10) for _ in range(10)])
# print(s2)

print(union([3,2,4],[1,2,3]))
print(union([1,2,4],[1,2,3]))
print(union([5,6,2,4],[1,2,3]))
print(union([1,2,4],[1,2,3,7,11]))
