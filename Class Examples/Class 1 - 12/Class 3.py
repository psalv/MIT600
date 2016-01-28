__author__ = 'paulsalvatore57'
#seeing if i remember the logic to fidn cube roots
##x = int(raw_input('enter a number:'))
##y = 0
##while y**3 < abs(x):
##    y = y + 1
##if y**3 != x:
##    print "not perfect cube"
##else:
##    if x < 0:
##        y = -y
##    print y

##
###approximation
##x = 270000
##epsilon = 0.01
##numGuesses = 0
##ans = 0.0
##while abs(ans**2 - x) >= epsilon and ans <= x:
##    ans += 0.1
##    numGuesses += 1
##print 'numGuesses =', numGuesses
##if abs(ans**2 - x) >= epsilon:
##    print 'Failed on square root of', x
##else:
##    print ans, 'is close to square root of', x
##
##using bisectional search




## cube route modification only rquires changing the exponent
x = -12345
epsilon = 0.00001
numGuesses = 0
low = 0.0
high = abs(x)
ans = (high + low)/2.0
while abs(ans**3 - abs(x)) >= epsilon and ans <= abs(x):
    #print low, high, ans
    numGuesses += 1
    if ans**3 < abs(x):
        low = ans
    else:
        high = ans
    ans = (high + low)/2.0
if x < 0:
    ans = -ans
print 'numGuesses =', numGuesses
print ans, 'is close to cube root of', x
print ans**3





##
##x = 1       #doesn't work for values less than one because ans > x
##e = 0.01
##guesses = 0
##high = x
##low = 0.0
##ans = (high + low)/2.0
##while abs(ans**2 - x) >= e and ans <= x:
##    guesses += 1
##    if ans**2 < x:
##        low = ans
##    else:
##        high = ans
##    ans = (high + low)/2.0
##if ans < 0:
##    print "No possible solution"
##else:
##    print "Square root aproximation: " + str(ans), "Number of guesses: " + str(guesses)
##
