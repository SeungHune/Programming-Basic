def gcd(m,n):
    while n != 0:
        return gcd(n,m%n)

    return abs(m)

print(gcd(48,18))
