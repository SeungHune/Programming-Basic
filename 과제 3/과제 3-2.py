# 순열 permutation
# assume: n > 0, k > 0, n >= k
# 양수 인수만 제대로 처리하면 된다.
# 즉, 인수가 양수인지는 함수 호출하기 전에 이미 확인했다고 가정한다.
# 그리고  n < k 인 경우에는 0을 내주도록 해야 한다.

def permutation(n,k):
    if k > 0:
        #return None # 여기에 적절한 식을 채워 넣자.
        if (n < k):
            return 0
        else :
            return (n - k + 1)*permutation(n, k-1)
    else:
        return 1

def permutation(n,k):
    pass # 꼬리 재귀
    def loop(n,k,a):
        if (k > 0):
            if (n < k):
                return 0
            else :
                return loop(n, k-1, (n - k + 1)*a)
        else :
            return a
    return loop(n,k,1)

def permutation(n,k):
    pass # while 문
    ans = 1
    while (k > 0):
        if (n < k):
            return 0
        else :
            ans = (n - k + 1) * ans
            n = n
            k = k - 1
    return ans

print(permutation(1,1)) # => 1
print(permutation(2,1)) # => 2
print(permutation(2,2)) # => 2
print(permutation(3,1)) # => 3
print(permutation(3,2)) # => 6
print(permutation(3,3)) # => 6
print(permutation(4,1)) # => 4
print(permutation(4,2)) # => 12
print(permutation(4,3)) # => 24
print(permutation(4,4)) # => 24