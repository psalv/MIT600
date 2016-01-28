__author__ = 'paulsalvatore57'
###My way to solve decimal problem:
##x = 0.1
##epsilon = 0.00001
##low = 0.0
##high = x
##ans = (high + low)/2.0
##while abs(ans**2 - x) >= epsilon and ans <= x and x >= 1:
##    #print 'ans =', ans, 'low =', low, 'high =', high
##    if ans**2 < x:
##        low = ans
##    else:
##        high = ans
##    ans = (high + low)/2.0
##if 0 < x < 1:
##    low = x
##    high = 1
##    ans = (high + low)/2
##    while abs(ans**2 - x) >= epsilon and ans >= x:
##        #print 'ans =', ans, 'low =', low, 'high =', high
##        if (ans**2) > x:
##            high = ans
##        else:
##            low = ans
##        ans = (high + low)/2.0
##print ans, 'is close to square root of', x

##
##
####His way to solve the decimal problem, this didnt actually solve the problem
####for all decimals places, just for 0.5
##x = 0.6
##epsilon = 0.01
##low = 0.0
##high = max(x, 1)
##ans = (high + low)/2.0
##while abs(ans**2 - x) >= epsilon and ans <= x:
##    print 'ans =', ans, 'low =', low, 'high =', high
##    if ans**2 < x:
##        low = ans
##    else:
##        high = ans
##    ans = (high + low)/2.0
##print ans, 'is close to square root of', x



####rebuilt squareroot code from scratch with all necessary considerations for
####every possible input
# x = float(raw_input('Enter a number: '))
# e = 0.0000001
# low = 0
# high = x
# ans = (low + high)/2
# n = 0
# if x >= 0:
#     if (x) >= 1:
#         while abs(abs(ans**2) - abs(x)) > e and ans < x:
#             n += 1
#             if ans**2 > x:
#                 high = ans
#             else:
#                 low = ans
#             ans = (high + low)/2
#     else:
#         high = 1
#         low = x
#         ans = (low + high)/2
#         while abs(ans**2 - abs(x)) > e:
#             n += 1
#             if ans**2 > x:
#                 high = ans
#             else:
#                 low = ans
#             ans = (high + low)/2
#     print 'The square root of', x, 'is:', ans
#     print 'Number of guesses: ', n
# else:
#     print 'Not feasible for negative numbers'


