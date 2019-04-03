def fastmult1(m,n):
    def loop(m,n,ans):
        if n > 0:
            if n % 2 == 0:
                return loop(2*m, n//2, ans)
            else:
                return loop(m, n-1, ans+m)
        else:
            return ans
    return loop(m,n,0)

print(fastmult1(3,6))

def fastmult(m,n):
    ans = 0
    while n > 0:
        if n % 2 == 0:
            m = 2 * m
            n = n//2
            ans = ans
        else:
            m = m
            n = n - 1
            ans = ans + m
    return ans

print(fastmult(3, 6))