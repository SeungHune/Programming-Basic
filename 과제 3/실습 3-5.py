def mult(m,n):
    ans = 0
    while n > 0:
        n = n-1
        ans = ans + m
    return ans

print(mult(3,6))

def mult1(m,n):
    def loop(n,ans):
        if n > 0:
            return loop(n-1, ans+m)
        else:
            return ans
    return loop(n, 0)