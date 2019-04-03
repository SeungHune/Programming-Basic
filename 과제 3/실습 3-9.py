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

print(rsmult0(3, 6))
print(rsmult0(57, 86))
print(int(5/2))
print(5%2)