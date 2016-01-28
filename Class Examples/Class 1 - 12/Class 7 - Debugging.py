__author__ = 'paulsalvatore57'


        # 7 - DEBUGGING

          # Goal: move towards a bug free program



#BINARY: only have digits 0 and 1

# 0101 = 1*4 + 0*2 + 1*1 = 5

            # 0000 = 0
            # 0001 = 1
            # 0010 = 2
            # 0011 = 3
            # 0100 = 4
            # 0101 = 5
            # 0110 = 6
            # 0111 = 7
            # 1000 = 8
            # 1001 = 9
            # 1010 = 10
            # 1011 = 11
            # 1100 = 12
            # 1101 = 13
            # 1110 = 14
            # 1111 = 15

# n digits, how many binary numbers can be represented by the digits? 2^n
# computers work in base 2, and people work in base 10, can cause confusion >>> fractional numbers only


# 0.125 = 1/8 = 1e-1 + 2e-2 + 5e-3
# 0.001 = 1e-3
# 0.1 = 1e-1 (decimal), infinite in binary (can stop at some finite number of bits, which is what python does)

#print statement by default rounds to 17 digits
# print repr(0.1)   #will give the approximation it is using



# x = 0.0
# numIters = 100000
# for i in range(numIters):       #incrementing x by a tenth
#     x += 0.1
# print x                         #prints 10000.0, because print automatically rounds
# print repr(x)
# print 10.0*x == numIters        #should have equal number of iterations as 10*x, since you are adding by 0.1
#                                     #when comparing you will get false
#                                     #don't test if two floating numbers are equal to each other
#
# def close(x, y, epsilon = 0.00001): #better to define a close function to see if numbers are good enough for our purposes
#     return abs(x - y) < epsilon
#
# if close(10.0*x, numIters):
#     print 'Good enough'










#Some people use the built in debuggers, but print statements are often more useful
#print statements search for the place in our program where things have gone wrong >>> be systemaic in search
    #use an approximation to the binary search method



#Questions:

#How could it produce the result it did?
#Study available data           >>> keep in mind you don't yet understand this program because it isn't working correctly
    #test results
    #lines of the program itself
    #probe the program with more print statements
#Form a hypothesis consistent with the data           >>> isolating what I believe to be the issue
#Design and run a repeatable experiment               >>> testing different variables to check if I have the solution








# def isPal(x):
#     """requires x to be a list
#        returns True if the list is a palindrome; False otherwise"""
#     assert type(x) == list
#     temp = x[:]                 #this parenthesis will clone the list
#     temp.reverse()                   #aliasing, x and temp are pointing to the same object
#     if temp == x:
#         return True
#     else:
#         return False

# def silly(n):
#     """requires: n is an int > 0
#     Gets n inputs from user
#     Prints 'Yes' if the inputs are a palindrome; 'No' otherwise"""
#     assert type(n) == int and n > 0
#     result = []
#     for i in range(n):
#         elem = raw_input('Enter something: ')
#         result.append(elem)
#     if isPal(result):
#         print 'Is a palindrome'
#     else:
#         print 'Is not a palindrome'


# #TEST HARNESS: code making it easier to test the program, ends up saving you work
# def isPalTest():
#     L = [1, 2]
#     result = isPal(L)
#     print 'Should print False:', result
#     L = [1, 2, 1]
#     result = isPal(L)
#     print 'Should print True:', result
# isPalTest()