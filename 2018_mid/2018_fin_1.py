def symmetric(sqmat):
    size = len(sqmat)
    for i in range(size):
        for j in range(size):
            if (i != j and sqmat[i][j] != sqmat[j][i]):
                return False
    return True


print(symmetric([[2,3],[3,2]])) # True
print(symmetric([[2,3],[2,3]])) # False
print(symmetric([[1,7,3],[7,4,-5],[3,-5,6]])) # True
print(symmetric([[1,1,1,1],[1,1,1,1],[1,1,1,1],[1,1,1,1]])) # True
print(symmetric([[1,2,3,4],[2,1,4,3],[3,4,1,2],[4,3,2,1]])) # True

##### 1. 9의 보수
# 수의 각 자리수에서 9와의 차이로 얻는 수를 9의 보수라고 한다.
# 정수를 받아서 9의 보수를 구하는 함수를 작성하시오.
# 인수 n은 자연수라고 가정
def complement9(n):
    s = str(n)
    ans = ""
    for c in s:
        d = 9 - int(c)
        ans = ans + str(d)
    return int(ans)

# print(0,">>",complement9(0)) # 9
# print(9,">>",complement9(9)) # 0
# print(4,">>",complement9(4)) # 5
# print(18,">>",complement9(18)) # 81
# print(40,">>",complement9(40)) # 59
# print(307,">>",complement9(307)) # 692
# print(9999,">>",complement9(9999)) # 0
# print(9142,">>",complement9(9142)) # 857
# print(9965,">>",complement9(9965)) # 34

##### 2. 찾기
# 원소 key와 원소의 리스트 xs를 인수로 받아서
# key가 xs에서 처음 나오는 위치번호를 리턴하는 함수
# key가 xs에 없으면 -1을 리턴
def search1st(key,ns) :
    index = 0
    for n in ns :
        if key == n :
            break
        else :
            index += 1
    if index == len(ns) :
        return -1
    else :
        return index

# print(search1st(3,[])) # -1
# print(search1st(3,[4,6,3,3,3])) # 2
# print(search1st(3,[3,3,3,3,3])) # 0
# print(search1st(3,[4,2,7,6,5])) # -1

# 원소 key와 원소의 리스트 xs를 인수로 받아서
# xs에 있는 모든 key의 위치번호의 리스트를 리턴하는 함수를 작성하시오.
def searchAll(key,ns) :
    index = 0
    indexes = []
    for n in ns :
        if key == n :
            indexes += [index]
        index += 1
    return indexes

# print(searchAll(3,[])) # []
# print(searchAll(3,[4,6,3,3,3])) # [2,3,4]
# print(searchAll(3,[3,3,3,3,3])) # [0,1,2,3,4]
# print(searchAll(3,[4,2,7,6,5])) # []


##### 3~4. 올려 세기

def countUpTo(n):
    if n < 0:
        return []
    else:
        return countUpTo(n-1) + [n]

def countUpTo(n):
    def loop(n,ns):
        if n < 0:
            return ns
        else:
            return loop(n-1,[n]+ns)
    return loop(n,[])

def countUpTo(n):
    ns = []
    while n >= 0:
        ns = [n] + ns
        n -= 1
    return ns

def countUpTo(n):
    ns = []
    for i in range(n+1):
        ns.append(i)
    return ns

# print(countUpTo(0)) # [0]
# print(countUpTo(5)) # [0, 1, 2, 3, 4, 5]
# print(countUpTo(-3)) # []


##### 5~6. 리스트 원소별로 더하기
##### 이해하고 꼬리재귀, while루프 버전으로 바꾸기
def zippo(xs,ys):
    if xs == [] or ys == []:
        return xs + ys
    else:
        return [xs[0]+ys[0]] + zippo(xs[1:],ys[1:])

def zippo(xs,ys):
    def loop(xs,ys,zs):
        if xs == [] or ys == []:
            return zs + xs + ys
        else:
            return loop(xs[1:],ys[1:],zs+[xs[0]+ys[0]])
    return loop(xs,ys,[])

def zippo(xs,ys):
    zs = []
    while not (xs == [] or ys == []):
        zs = zs + [xs[0]+ys[0]]
        xs, ys = xs[1:], ys[1:]
    return zs + xs + ys

# print(zippo([],[]))
# print(zippo([2,7,4],[7,2,5]))
# print(zippo([2,7,4],[7,2,5,9,9]))
# print(zippo([2,7,4,9,9],[7,2,5]))

##### 7. Blast
# 정수 리스트를 받아서 각 정수를 그 수만큼 나열하여 붙여서 내주는 함수를
# 중첩 for 루프를 사용하여 작성하시오.

def blast(ns):
    bs = []
    for n in ns:
        ns = []
        for _ in range(n):
            ns.append(n)
        bs += ns
    return bs

# print(blast([]))
# print(blast([1,2,4]))
# print(blast([3,4,5,1,2,4]))
# print(blast([2,-3,3]))

##### 8~10. 집합
def makeset(xs):
    ys = []
    for x in xs:
        if x not in ys:
            ys.append(x)
    return ys

def union(xs,ys):
    zs = []
    for x in xs:
        if x not in ys:
            zs.append(x)
    return zs+ys

def diff(xs,ys):
    zs = []
    for x in xs:
        if x not in ys:
            zs.append(x)
    return zs

def intersect(xs,ys):
    zs = []
    for x in xs:
        if x in ys:
            zs.append(x)
    return zs

# ## Test
# import random
# s1 = makeset([random.randrange(10) for _ in range(10)])
# print(s1)
# s2 = makeset([random.randrange(10) for _ in range(10)])
# print(s2)
# print(union(s1,s2))
# print(diff(s1,s2))
# print(intersect(s1,s2))


##### 11. Equivalent class
def equiv_class(ns):
    ns.sort()
    if ns == [] :
        return []
    else :
        top = ns[0]
        nss = [[top]]
        for n in ns[1:] :
            top = nss[-1][0]
            if n == top :
                tops = nss[-1]
                nss = nss[:-1]
                nss.append(tops+[n])
            else :
                nss.append([n])
        return nss

# print(equiv_class([])) # []
# print(equiv_class([3])) # [[3]]
# print(equiv_class([4,3,2,4,4])) # [[2],[3],[4,4,4]]
# print(equiv_class([2,4,4,2,2,3])) # [[2,2,2],[3],[4,4]]

##### 12. Permutation
#정수 리스트를 받아서 원소의 가능한 모든 순열의 리스트를 만드는 함수 perm
#을 작성하시오.
def perm(xs):
    ps = [[]]
    for x in xs:
        ns = []
        for p in ps:
            ns.append(p+[x])
        ps += ns
    return ps

# print(perm([])) # [[]]
# print(perm([1])) # [[],[1]]
# print(perm([1,2])) # [[],[1],[2],[1,2]]
# print(perm([1,2,3])) # [[], [1], [2], [1, 2], [3], [1, 3], [2, 3], [1, 2, 3]]
# print(perm([1,2,3,4])) # [[], [1], [2], [1, 2], [3], [1, 3], [2, 3], [1, 2, 3], [4], [1, 4], [2, 4], [1, 2, 4], [3, 4], [1, 3, 4], [2, 3, 4], [1, 2, 3, 4]]