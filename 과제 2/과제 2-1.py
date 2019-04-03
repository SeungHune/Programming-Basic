def smallerOdd(x,y):
    pass # fill your code here
    if (x%2 == 1 and y%2 == 1):
        if (x<y):
            return (x)
        elif (x>y):
            return (y)
        if (x==y):
            return (x)

    if (x%2 == 0 and y%2 == 1):
        return (y)
    if (x%2 == 1 and y%2 == 0):
        return (x)

    if (x%2 == 0 and y%2 == 0):
        return (x)

def smallestOdd(x,y,z):
    pass # fill your code here
    a = smallerOdd(x,y)
    b = smallerOdd(a,z)
    if (b%2 == 0):
        return None
    return (b)

print(smallestOdd(3,2,2)) # returns 3
print(smallestOdd(3,5,7)) # returns 3
print(smallestOdd(3,5,1)) # returns 1
print(smallestOdd(8,3,4)) # returns 3
print(smallestOdd(8,3,5)) # returns 3
print(smallestOdd(8,5,3)) # returns 3
print(smallestOdd(2,8,3)) # returns 3
print(smallestOdd(2,8,4)) # returns None