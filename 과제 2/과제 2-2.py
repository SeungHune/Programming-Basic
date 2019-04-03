def isRRN(s):
    (front, mid, back) = s.partition("-")
    return front_ok(front) and mid == "-" and back_ok(s)


#윤년 체크
def isleapyear(year):
    if (year >= 0):
        if ((year%4 == 0) and (year%100 != 0)):
            return True
        if (year%4 == 0):
            if(year%100 == 0):
                if(year%400 == 0):
                    return True
                else:
                    return False
        else:
            return False
        return False
    else:
        return None

#년 월 체크 - 앞자리 체크(윤년 포함)
def front_ok(front):
    a = int(front[0:2])
    month = int(front[2:4])
    day = int(front[4:6])
    if (month > 12):
        return False
    if (day > 31):
        return False
    if (a >= 20):
        birthYear = int("19"+front[0:2])
    else:
        birthYear = int("20"+front[0:2])

    if (isleapyear(birthYear) == True):
        if (month == 1):
            if (day <= 31):
                return True
            else:
                return False
        if (month == 2):
            if (day <= 29):
                return True
            else:
                return False
        if (month == 3):
            if (day <= 31):
                return True
            else:
                return False
        if (month == 4):
            if (day <= 30):
                return True
            else:
                return False
        if (month == 5):
            if (day <= 31):
                return True
            else:
                return False
        if (month == 6):
            if (day <= 30):
                return True
            else:
                return False
        if (month == 7):
            if (day <= 31):
                return True
            else:
                return False
        if (month == 8):
            if (day <= 31):
                return True
            else:
                return False
        if (month == 9):
            if (day <= 30):
                return True
            else:
                return False
        if (month == 10):
            if (day <= 31):
                return True
            else:
                return False
        if (month == 11):
            if (day <= 30):
                return True
            else:
                return False
        if (month == 12):
            if (day <= 31):
                return True
            else:
                return False

    if (isleapyear(birthYear) == False):
        if (month == 1):
            if (day <= 31):
                return True
            else:
                return False
        if (month == 2):
            if (day <= 28):
                return True
            else:
                return False
        if (month == 3):
            if (day <= 31):
                return True
            else:
                return False
        if (month == 4):
            if (day <= 30):
                return True
            else:
                return False
        if (month == 5):
            if (day <= 31):
                return True
            else:
                return False
        if (month == 6):
            if (day <= 30):
                return True
            else:
                return False
        if (month == 7):
            if (day <= 31):
                return True
            else:
                return False
        if (month == 8):
            if (day <= 31):
                return True
            else:
                return False
        if (month == 9):
            if (day <= 30):
                return True
            else:
                return False
        if (month == 10):
            if (day <= 31):
                return True
            else:
                return False
        if (month == 11):
            if (day <= 30):
                return True
            else:
                return False
        if (month == 12):
            if (day <= 31):
                return True
            else:
                return False

#뒷자리 체크
def back_ok(s):
    a = int(s[0])
    b = int(s[1])
    c = int(s[2])
    d = int(s[3])
    e = int(s[4])
    f = int(s[5])
    g = int(s[7])
    h = int(s[8])
    i = int(s[9])
    j = int(s[10])
    k = int(s[11])
    l = int(s[12])
    m = int(s[13])
    if (m == 11 - ((2*a+3*b+4*c+5*d+6*e+7*f+8*g+9*h+2*i+3*j+4*k+5*l) % 11) ):
        return True
    else:
        return False

    if (10 == 11 - ((2*a+3*b+4*c+5*d+6*e+7*f+8*g+9*h+2*i+3*j+4*k+5*l) % 11) ):
        if (m == 0):
            return True
        else:
            return False

    if (11 == 11 - ((2*a+3*b+4*c+5*d+6*e+7*f+8*g+9*h+2*i+3*j+4*k+5*l) % 11) ):
        if (m == 1):
            return True
        else:
            return False
