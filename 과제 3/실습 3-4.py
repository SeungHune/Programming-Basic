def mult0(m,n):
    if n > 0:
        return m + mult0(m,n-1)
    else:
        return 0

print(mult0(3,6))

def mult1(m,n):
    def loop(n,ans):
        if n > 0:
            return loop(n-1, ans+m)
        else:
            return ans
    return loop(n, 0)

print(mult1(3,6))