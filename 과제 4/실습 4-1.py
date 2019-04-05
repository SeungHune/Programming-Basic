def insert(n,ss):
    if ss != []:
        if n <= ss[0]:
            return [n] + ss
        else:
            return [ss[0]] + insert(n, ss[1:])
    else:
        return [n]

print(insert(5, [2,4,6,7]))
print(insert(4, [2,3,6] ))
print(insert(1, [] ))
print(insert(123, [34,78,155,924,1203] ))