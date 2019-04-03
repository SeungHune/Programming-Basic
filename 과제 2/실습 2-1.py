def monthlyPaymentPlan(principal, interest, year):
    pass  #fill your code here
    r = interest/1200
    m = year*12
    p = principal
    d = int((((1+r)**m)*p*r)/((1+r)**m -1))
    return(d)

print(monthlyPaymentPlan(10000000, 2.8, 4))
# should print 220460
