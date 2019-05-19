def minsteps0(n):
    if n > 1:
        r = 1 + minsteps0(n - 1)
        if n % 2 == 0:
            r = min(r, 1 + minsteps0(n // 2))
        if n % 3 == 0:
            r = min(r, 1 + minsteps0(n // 3))
        return r
    else:
        return 0

def minsteps1(n):
    memo = [0] * (n + 1)
    def loop(n):
        print(memo)
        if n > 1:
            if memo[n] != 0:
                return memo[n]
            else:
                memo[n] = 1 + loop(n - 1)
                if n % 2 == 0:
                    memo[n] = min(memo[n], 1 + loop(n // 2))
                if n % 3 == 0:
                    memo[n] = min(memo[n], 1 + loop(n // 3))
                return memo[n]
        else:
            return 0
    return loop(n)

print(minsteps1(3))

def minsteps(n):
    memo = [0] * (n + 1)
    for i in range(len(memo)):
        print(memo)
        if (n > 1):
            if (memo[n] != 0):
                return memo[n]
            else:
                n = n -1
                memo[n] = 1 + memo[n-1]
                if (n % 2 == 0):
                    n =  n // 2
                    memo[n] = min(memo[n], 1 + memo[n//2])
                if (n % 3 == 0):
                    n = n // 3
                    memo[n] = min(memo[n], 1 + memo[n//3])
    return memo[n]

print(minsteps(3))
