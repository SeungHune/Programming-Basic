def rsmult0(m,n):
    def loop(m,n):
        if n > 1:
            if (n%2 == 1):
                return m + loop(m*2, int(n/2))
            else:
                return loop(m * 2, int(n / 2))
        else: # n == 1
            return m
    if n > 0:
        return loop(m,n)
    else:
        return 0

def rsmult1(m,n):
    def loop(m,n,a):
        if n > 1:
            if (n%2 == 1):
                return loop(m*2, int(n/2), a+m)
            else :
                return loop(m*2, int(n/2), a)
        else: # n == 1
            return a+m
    if n > 0:
        return loop(m, n, 0)
    else:
        return 0

print(rsmult1(57, 86))
print(rsmult1(4, 5))