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

def fastmult0(m,n):
    if n > 0:
        if n % 2 == 0:
            return fastmult0(2*m, n//2)
        else:
            return m + fastmult0(m,n-1)
    else:
        return 0

print(fastmult0(3,6))