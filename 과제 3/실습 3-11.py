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

def rsmult(m,n):
    ans = 0
    while n > 1:
        if (n%2 == 1):
            ans = ans + m
            m = m * 2
            n = int(n/2)
        else:
            ans = ans
            m = m * 2
            n = int(n/2)
    if (n == 1):
        return ans + m

print(rsmult(57, 86))
print(rsmult(3, 6))
print(rsmult(4, 5))
