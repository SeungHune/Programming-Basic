def search(key,ns):
    index = -1
    ss = []
    for n in ns:
        if (key == n):
            index = index + 1
            ss.append(index)
        else:
            index = index + 1
    return ss
    if (ns == []):
        return []

print(search(3,[])) # -1
print(search(3,[4,6,3,3,3])) # 3
print(search(3,[3,3,3,3,3])) # 0
print(search(3,[4,2,7,6,5])) # -1