def count_upto(n):
    def loop(n,ns):
        if n < 0:
            return ns
        else:
            return loop(n-1, [n] + ns)
    return loop(n,[])

def count_upto(n):
    ns = []
    while (n >= 0):  # 이 부분을 채우자
        ns = [n] + ns
        n = n - 1
    return ns

print(count_upto(0))  # [0]
print(count_upto(5))  # [0, 1, 2, 3, 4, 5]
print(count_upto(-3))  # []