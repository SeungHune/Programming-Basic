def blast(ns):
    bs = []
    #pass  # 이 부분을 채우자
    for n in ns:
        if (n <= 0):
            pass
        else:
            t = n
            while (t > 0):
                t = t -1
                bs.append(n)
    return bs

print(blast([]))
print(blast([1,2,4]))
print(blast([3,5]))
print(blast([2,-3,3]))