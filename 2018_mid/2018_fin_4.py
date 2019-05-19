
### 9. 리스트의 원소가 모두 같은지 확인

def allequal(ns):
    if len(ns) > 1:
        a = ns[0]
        for i in ns:
            if(i != a):
                return False
        return True
    else:
        return True

def adjustT(ns):
    def loop(ns, rs):
        if len(ns) > 1:
            if(ns[0] == ns[1]):
                rs.append(ns[0])
                return loop(ns[1:], rs)
            if (ns[0] < ns[1]):
                a = ns[0] + 1
                rs.append(a)
                return loop(ns[1:], rs)
            if (ns[0] > ns[1]):
                b = ns[0] - 1
                rs.append(b)
                return loop(ns[1:], rs)

        else:
            return rs + ns
    return loop(ns, [])


### 10. 동일화 노력

def equalizer(ns):
    count = 0
    if len(ns) > 1:
        a = allequal(ns)
        while a == False:
            ns = adjustT(ns)
            count = count + 1
            a = allequal(ns)
    return count


print(equalizer([4, 6, 5, 3, 7, 6, 2, 1, 3, 2])) # 9
print(equalizer([8, 2, 5, 7, 1, 1, 6, 7, 4, 8])) # 12
print(equalizer([8, 4, 5, 6, 9, 8, 6, 2, 0, 6])) # 14
print(equalizer([4, 0, 1, 0, 3, 4, 3, 3, 7, 9])) # 13
print(equalizer([1, 6, 5, 6, 8, 5, 3, 3, 3, 8])) # 13
print(equalizer([])) # 0
print(equalizer([5])) # 0
print(equalizer([4, 4, 4])) # 0
print(equalizer([4, 3])) # 1
print(equalizer([4, 5])) # 1
print(equalizer([4, 5, 4])) # 2
print(equalizer([14, 69, 87, 13, 0, 16, 83, 19, 45, 88])) # 92
