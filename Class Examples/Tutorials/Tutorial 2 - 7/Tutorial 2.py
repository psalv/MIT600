__author__ = 'paulsalvatore57'

            #LOOPS, TUPLES, STRINGS, AND FXNS



###DEFINING A RANGE GOING UP BY SELECT AMOUNT >>> RANGE(start, end+1, step size)
#print range(1, 100, 3)

# tuple_1 = (243, 'my', 2332.8)
# print tuple [0:3]
# print tuple_1[-1]
# print len(tuple_1)

###TUPLE OF TUPLES
# tuple_t = (('just', 'got'), 'and', 'real')    #tuples of tuples
# print len(tuple_t)
# print tuple_t[0]
# print (tuple_t[0])[-1]                        #can print out tuples of tuples
# print tuple_t

# tuples are immutable, can't assign items to tuples that are already assigned




###SLICING OF TUPLES
# tuple_2 = (3,14, 6, 7, 232, 20202)
# print tuple_2[1:3]
# print tuple_2[1:]
# print tuple_2[:3]
# print tuple_2[3]
# print tuple_2[3]
# print tuple_2[:]

###TUPLES ARE IMMUTABLE, but can have elements added to them;
# can't change specific regions such as tuple[3] = 4,
# tuple_3 = tuple_2 + (1, 21)
# print tuple_3

# Parenthesis are grouping icon in python,
# if you want a tuple with one element you need to include a comma after the element:
# not_a_tuple = (50)
# is_a_tuple = (50,)
# print not_a_tuple
# print is_a_tuple





# strings are immutable and non-scalar, have multiple characters, and can get to certain characters:
# ex = 'example'
# print ex
# print ex[0]
# print ex[1]
# print ex[0:2]
#
# # immutable, so can't assign variables:
# ex[1] = q

###ITERATION OVER A STRING >>> LETTER
# for letter in ex:
#     print letter

###FXNS FOR STRING >> UPPER, LOWER, FIND(x), REPLACE(old, new)
# ex = 'example'
# print ex.upper()
# print ex.lower()
# print ex.find('e')                      #can be done for sub strings, this finds the very first
# print ex.find('23')                     #if it doesn't find it, will return -1
# print ex.replace('e', 'Q')
# print ex.lower().replace('e', 'Q')      #can do multiple transformations at once
#
# ex2 = 'eeeeeeeee'
# print ex2.replace('e', 'Q', 3)          #can signify total number of replacements you want to do
#
# ex = ex.upper()                         #permenantely change string qualities
# print 'new ex = ', ex



###BREAK STATEMENT
# x = int(raw_input('Enter a perfect cube:'))
# for ans in range (0, abs(x)+1):
#     if ans**3 == abs(x):
#         break
# if x < 0:
#     ans = -(ans)
# if ans**3 != x:
#     print 'The input is not a perfect cube'
# else:
#     print 'The cube root of', x, 'is:', ans

###NESTED LOOP
# for i in range (0, 10):
#     for j in range (10, 1000):         #this nested loop will pick out only even values of j
#         if j % 2 == 0:                 #percent sign means modulus, this cause it means is j evenly divisible by 2
#             break                      #only breaks out of first loop, not both






###FUNCTIONS
# def cube(number):                                               #def tells that we are defining a function, have a meaningful name, a set of parameters
#     """Takes a number and returns the cube of that number       #allows you to describe what the function does
#         Input: number (float or int)                            #shuld include what qualifies as input and output
#         Output: number**3 (float)"""
#     return number**3                                            #functions must return something
#
# print cube(3)
# print cube(3.23)

# #REQUIRES A RETURN STATEMENT, OR WILL RETURN NONE:
# def times2(number):
#     answer = number*2
# print times2(2)
#
# def times2(number):
#     answer = number*2
#     return answer
# print times2(2)




###VARIABLE SCOPE
# gl_var = 1                                          #global variables must be defined before calling the function
# def fxn(variables):
#     """Takes variables, returns none
#         input: variables
#         output: none"""
#     lc_var = 2
#     print 'Local variable:', lc_var
#     print 'Global variables:', gl_var
#     print 'Parameter input into fxn:', variables
#
# gl_var2 = 3
# fxn(gl_var2)
# print lc_var                      #this returns an error because this variable has local scope to the function fxn


# gl_var = 0
# def incrementing(x):
#     global gl_var                   #to refernce a global variable need to reference it with global key word
#     x = x + 1                       #overwriting what is in local parameter, but not what is in global parameter of y, changes stay within fcn
#     gl_var += 1
#     return x                        #PRINT != RETURN
#
# y = 10
#
# print incrementing(y)
# print y




