__author__ = 'paulsalvatore57'

            #RECURSION, PSEUDOCODE, DEBUGGING


#RECURSION:

#Multiplication example
#Basecase: In x*n, when n = 1, answer = 1

# def multiply(x, n):
#     if n == 0 or m == 0:
#         return 0
#     elif n >= 1:
#         return x + multiply(x, n - 1)
#     elif n <= -1:
#         return -x + multiply(x, n + 1)
#
# def Testmultiply():         #set up a function to test the function I have written with all possible cases
#     print multiply(2, 2)
#     print multiply(-2, 2)
#     print multiply(2, -2)
#     print multiply(-2, -2)
#     print multiply(-2, 0)
#     print multiply(0, 2)
#
# Testmultiply()






#You DON'T ALWAYS need to work recursively, can work iteratively;
#Iterative fibonacci:

# def iFib(x):
#     ans = 0
#     ans1 = 1
#     n = 0
#     if x == 0:
#         return 0
#     while n < x:
#         c = ans1
#         ans1 = ans1 + ans
#         n += 1
#         ans = c
#     return ans1
#
# print iFib(8000)       #this way actually works better than recursion, less intensive on the computer, can go much higher





#Default parameters for functions,
#Can specify that certain parameters are optional, or you can give default values to them:

# def examplep(x = 100, y = None):
#     print x
#     print y
# examplep()




# #Recursive bisectional square root:
#
# def recbi(x, epsilon = 0.0001, low = None, high = None):
#     if low == None:
#         low = 0
#     if high == None:
#         high = x
#     midpoint = (low + high)/2.0
#     if abs(midpoint**2 - x) <= epsilon or midpoint > x:
#         return midpoint
#     else:
#         if midpoint**2 < x:
#             return recbi(x, epsilon, midpoint, high)
#         else:
#             return recbi(x, epsilon, low, midpoint)
#
# print recbi(25)






#FLOATING POINT: inexact, should not compare for exact equality
    #More info: IEEE 754


# a = 10/100.0
# b = 1/100.0
# c = 9/100.0
#
# if a == b + c:
#     print "Equal"
# else:
#     print repr(b + c)
#
# e = 0.001       #amount of error that we are willing to tolerate in our calculations
#
# if abs(a - (b + c)) < e:
#     print "Close to equal"
# else:
#     print "Not close enough"



#USEFUL FXN TO KEEP AROUND FOR TESTING CLOSENESS OF TWO NUMBERS:
# def close(x, y, epsilon = 0.00001):
#     return abs(x - y) < epsilon



#Floating point is not exact, but it is consistent:
# d = b + c
# print c == d - b    #subtracting the same inexact question





#PSEUDOCODE: states program function in easier to read languages (easy planning method for algorithms)
#Hangman:
    #select random word, tell length
    #display a masked word                                      #while have guesses remaining keep doing all this
    #gives available letters, and intakes letter selection          #and the word is not guessed
    #removes letter from list of available letters
    #checks to see if letter is in masked word
        #if it isn't decrease number of available guesses
        #if it is, add to correct letters guess
            #unmask the select letter





#CHECKING FOR PRIMER NUMBERS
# def prime(n):
#     assert type(n) == int and n > 0
#     if abs(n) <= 3:
#         return True
#     else:
#         for x in range (2, int(n**0.5) + 1):
#             if n % x == 0:
#                 return False
#     return True
#
# print prime(8)





#Debugging:
#When designing a test harness, you want to determine the boundaries of the program that you need to test