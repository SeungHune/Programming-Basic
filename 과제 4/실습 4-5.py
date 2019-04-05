def insert(n,ss):
    left = []
    while ss != []:
        if n <= ss[0]:
            return left + [n] + ss
        else:
            ss, left = ss[1:], left + [ss[0]]
    return left + [n]

# def insertionsort(ns):
#     def loop(ns,ss):
#         if ns != []:
#             return loop(ns[1:], insert(ns[0],ss))
#         else:
#             return ss
#     return loop(ns,[])

def insertionsort(ns) :
    ss = []
    while ns != []:
        ns, ss = ns[1:], insert(ns[0], ss)
    return ss

print((insertionsort([3,5,4,2])))