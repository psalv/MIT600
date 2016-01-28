###Problem 1

##x = float(raw_input('Starting balance: '))
##p = -(float(raw_input('Rate paid off: ')))/100
##i = (float(raw_input('Yearly interest rate: '))/12)/100
##m = 1.0
##q = 0
##while m <= 12.0:
##    y = p*x + i*x
##    x = x + y
##    m = m + 1.0
##    print 'Month:', m
##    print 'Amount paid off: ', -y
##    print 'Amount remaining: ', x
##    q = q + abs(p*x)
##else:
##    print 'End of year balance: ', x
##    print 'Amount paid: ', q




#####Problem 2
#####Find a fixed payment by which all will be paid off by the end of the year
##
##x = float(raw_input('Starting balance: '))
##i = (float(raw_input('Yearly interest rate: '))/12)/100
##r = 0
##m = 1.0
##while x >= 0:
##    z = x
##    r = r + 10
##    #print r
##    while r <= i*z:         #this is to skip the steps wherein the interest is greater than the payment
##        r = r + 10
##    while m <= 12.0:
##        y = r - i*z
##        z = z - y
##        #print z
##        if z > 0:
##            m = m + 1.0
##        else:               #this is to get us out of the loop once th epayment is made
##            break
##    if z <= 0:
##        break
##    else:
##        m = 1.0
##print 'Monthly payment of: ', r
##print 'Months to pay off: ', m
##print 'Final balance: ', z












#####Problem 3
#####Find a fixed amount by which all will be paid off by the end of the year, using bisectional approach
##
x = float(raw_input('Starting balance: '))
i = (float(raw_input('Yearly interest rate: '))/12)/100
high = x
low = x/12
e = 0.01
ans = (high + low)/2
z = 1
n = 0
while abs(z) > e:
    n += 1
    m = 1.0
    z = x
    while m <= 12.0:
        y = ans - i*z
        z = z - y
        m = m + 1.0
    if z < 0:
        high = ans
    else:
        low = ans
    #print "z: ", z
    ans = (high + low)/2
    #print "ans: ", ans
print 'The monthly payment will be: ', ans
print 'Months taken to complete: ', m - 1
print 'Number of guesses: ', n
    # should be 25.5 guesses



