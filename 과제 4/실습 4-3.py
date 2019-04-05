def insert(n,ss):
    left = []
    while ss != []:
        if n <= ss[0]:
            return left + [n] + ss
        else:
            ss, left = ss[1:], left + [ss[0]]
    return left + [n]

# def insert(n,ss):
#     def loop(ss,left):
#         if ss != []:
#             if n <= ss[0]:
#                 return left + [n] + ss
#             else:
#                 return loop(ss[1:], left + [ss[0]])
#         else:
#             return left + [n]
#     return loop(ss,[])


print(insert(1, [2,3,4]))
print(insert(777, [13,34,56,78,355]))
print(insert(3, []))