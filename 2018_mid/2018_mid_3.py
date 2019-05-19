def count_upto(n):
    if n < 0:
        return []
    else:
        return count_upto(n - 1) + [n]

def count_upto(n):
    def loop(n,ns):
        if n < 0:
            return ns
        else:
            return loop(n-1, [n] + ns)
    return loop(n,[])

print(count_upto(0))  # [0]
print(count_upto(5))  # [0, 1, 2, 3, 4, 5]
print(count_upto(-3))  # []