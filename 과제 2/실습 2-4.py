def smaller(a,b):
    if (a<b):
        return(a)
    else:
        return(b)
    if (a==b):
        return(a)

def smallest(x,y,z):
    c = smaller(x,y)
    d = smaller(c,z)
    return(d) # fill your expression here

print(smallest(3,5,9)) # returns 3
print(smallest(5,3,9)) # returns 3
print(smallest(5,9,3)) # returns 3
print(smallest(3,9,5)) # returns 3
print(smallest(9,3,5)) # returns 3
print(smallest(9,5,3)) # returns 3
print(smallest(3,3,5)) # returns 3
print(smallest(5,3,3)) # returns 3
print(smallest(3,5,3)) # returns 3
print(smallest(3,3,3)) # returns 3  
