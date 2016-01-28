__author__ = 'paulsalvatore57'
##y = float(raw_input('Enter:'))
##print y
##
##
##x = int(raw_input('Enter an integer: '))
##if x%2 == 0:
##    print 'Even'
##if x%2.5 == 0:
##    print "Test"
##    print x/2.5
##else:
##    print 'Odd'
##    if x%3 != 0:
##        print 'And not divisible by 3'

###Find the cube root of a perfect cube
##x = int(raw_input('Enter an integer: '))
##ans = 0
##while ans*ans*ans < abs(x):
##    ans = ans + 1
##    print 'current guess =', ans
##if ans*ans*ans != abs(x):
##    print x, 'is not a perfect cube'
##else:
##    if x < 0:
##        ans = -ans
##    print 'Cube root of ' + str(x) + ' is ' + str(ans)


####find all of the cube roots up until 500
##x = -10
##while abs(x*x*x) < float(500):
##    x = x + 1
##    print x -1
##while abs(x*x*x) > float(500):
##    x = x + 1
##    print x





#print numbers 1-100, multiples of 3 print fizz, multiples of 5 print fuzz,
#3 and 5 print fizzfuzz



##for x in range (1, 101):
##    for y in range (1, 34):
##        if 5.0*y == x:
##            x = 'fuzz'
##        if 3.0*y == x:
##            x = 'fizz'
##        if 15.0*y == x:
##            x = 'fizzfuzz'
##    print x
##



for x in range (1, 101):
    if x % 3 == 0 or x % 5 == 0:
        x = str(x)
        x = ''
        if x % 3 == 0:
            x = x + 'fizz'
        if x % 5 == 0:
            x = x + 'buzz'
    print x
