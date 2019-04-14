def binSearchClosest(list, key):
    index = 0
    gap = 100000
    if (list == []):
        return None
    for i in range(len(list)):
        if (list[i] == key):
            return i
        else:
            b = abs(list[i] - key)
            if (b < gap):
                gap = b
                index = i
    return  index

print(binSearchClosest([], 3))
print(binSearchClosest([8], 3))
print(binSearchClosest([3], 3))
print(binSearchClosest([1,2,5,7,8], 3))
print(binSearchClosest([1,2,5,7,8], 5))
print(binSearchClosest([1,2,5,7,8], 6))
print(binSearchClosest([1,2,5,9,10], 8))