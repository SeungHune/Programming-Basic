def smallest(x,y,z):
    pass # fill your code here
    if(x<y<z):
        return(x)
    if(x<z<y):
        return(x)
    if(y<x<z):
        return(y)
    if(y<z<x):
        return(y)
    if(z<x<y):
        return(z)
    if(z<y<x):
        return(z)
    if(x==y):
        if(x<z):
            return(x)
        else:
            return(z)
    if(x==z):
        if(x<y):
            return(x)
        else:
            return(y)
    if(y==z):
        if(x<y):
            return(x)
        else:
            return(y)
    if(x==y==z):
        return(x)

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
