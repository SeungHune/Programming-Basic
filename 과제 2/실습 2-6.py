def isinteger(s):
    return s.isdigit() or (s[0] == '-' and s[1:].isdigit())

def isfloat(s):
    a,b,c = s.partition('.');
    if (len(a) == 0 and len(c) == 0):
        return False;
    if(len(a) == 0):
        return(isinteger(c));
    if(a[0] == "-" and len(a) < 2):
        return(isinteger(c));
    if(a[0] == "-" and len(a) >= 2 and len(c) >= 1):
        return(isinteger(a) and isinteger(c))
    if(len(c) == 0):
        return(isinteger(a));
    if(a[0] != "-" and len(c) >=1):
        return(isinteger(a) and isinteger(c));
    if(len(a) == 0 and len(c) == 0):
        return False;



print(isfloat(".112"), 1)
print(isfloat("-.112"), 2)
print(isfloat("3.14"), 3 )
print(isfloat("-3.14"), 4)
print(isfloat("5."),5 )
print(isfloat("5.0"),6)
print(isfloat("-777.0"),7)
print(isfloat("-777."),8)
print(isfloat("."),9)
print(isfloat(".."),10)
print(isfloat("-.-123"))
