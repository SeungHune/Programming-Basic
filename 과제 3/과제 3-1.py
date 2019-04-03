# 덧셈만으로 제곱 계산
# 작성한 함수는 정수 인수에 대해서 제대로 작동하면 된다.
# 그런데 앞 문제와는 달리 음수 인수에 대해서도 제대로 작동해야 함을 명심하자.

def square(n):
    def loop(n):
        if n > 0:
            #return None # 여기에 적절한 식을 채워 넣자.
            return 2*n -1 + loop(n-1)
        else:
            return 0
    return loop(abs(n)) # 음수를 처리하려면 이 부분을 손봐야 한다.

def square(n):
    pass # 꼬리 재귀
    def loop(n,a):
        if n > 0:
            return loop(n-1, a + (2*n - 1))
        else :
            return a
    return (loop(abs(n), 0))

def square(n):
    pass # while 문
    n = abs(n)
    ans = 0
    while n > 0:
        ans = ans + (2*n -1)
        n = n -1
    return ans

print(square(0)) # => 0
print(square(1)) # => 1
print(square(-2)) # => 4
print(square(3)) # => 9
print(square(-4)) # => 16
print(square(5)) # => 25