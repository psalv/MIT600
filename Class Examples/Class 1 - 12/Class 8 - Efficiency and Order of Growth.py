__author__ = 'paulsalvatore57'


        # 8 - EFFICIENCY AND ORDER OF GROWTH


#Efficiency is about algorithms, not coding skill and clever algorithms
#Depend on problem reducing, want to reduce problems to previously solved problems
    #space and time (trade off between space and speed) >>> most people worry about time

#Computational complexity (how long it takes to run)
    #speed of machine
    #cleverness of python implementation
    #depends on input

    #count number of basic steps; Time is proportional to change of N (input) > N (output)
    #STEP is an operation that takes constant time

#Random Access Machine (RAM) >>> instructions are sequential, assume constant time req'd to access memory

#Best case complexity: in linear search you find it immediately >>> Minimum running time
#Worst case complexity: in linear search the element is not present >>> Maximum running time (must search entire list)
#Expected case complexity: average time, don't deal with this much (too complicated, need a lot of information)

    #Almost always focuses on worst case >>> provides an upper bound to the worst that can happen (no surprises)





# def f(n):                   #computing factorial
#     assert n >= 0
#     answer = 1
#     while n > 1:
#        answer *= n
#        n -= 1
#     return answer
#Each time through the loop it executes 3 steps, goes through the loop n times
#Ignore additive steps because they have a very minute contribution
#Only care about growth of running time in respect to the size of the input

#Typically even ignore multiplicative constants (so instead of 3*n, just n in this case)
#Asymptoptic growth, limit is reach as size of input increases
    #Big oh: O(n), time grows linearly with n
    #Gives us an upper bound for the asymptotic growth of the fxn

    #   f(x) epsilon O(x^2)
    #Function F grows no faster than the quadratic polynomial x^2

#Omicron classes:

    #O(1)       = constant time         #can be very large, the number of steps does not change (step number is independent of input)
    #O(log n)   = logarithmic growth
    #O(n)       = linear
    #O(n log n) = log linear            #try not to do anything worse than log linear if possible
    #O(n^c)     = polynomial            #in practice even quadratic are impractically slow
    #O(c^n)     = exponential

#When people say f(x) is O(x^2), they mean it is about that, they use approximations


# def fact(n):            #factorial written recursively
#     assert n >= 0
#     if n <= 1:
#         return n
#     else:
#         return n*fact(n - 1)
# #the piece that we care about is the number of times the factorial is called
# #it will be called n times >>> same complexity
# #slightly higher overhead (multiplicative constant), but this is relatively minute
#
#
# def g(n):
#     x=0
#     for i in range(n):
#         for j in range(n):
#             x += 1
#     return x
# #start by finding the inner loop, go through it n times
# #the outer loop will also be gone through n times
# #complexity is n^2 (polynomial)
#
#
# def h(x):
#     assert type(x) == int and x >= 0
#     answer = 0
#     s = str(x)
#     for c in s:
#         answer += int(c)
#     return answer
# #this is the sum of the digits in some string s
# #number of decimal digits required to express an integer is the log of that magnitude of that integer:
# #O(n) where n is log10(x)
#     #you are not done complexity until you say what n represents


##Linear search:
# def search(L, e):
#     for elem in L:
#         if elem == e:
#             return True
#         if elem > e:
#             return False
#     return False
#
# L = range(100)
# print search(L, 0)
# print search(L, 50)
# print search(L, 100)


#Binary search:
def bSearch(L, e, low, high):
    global numCalls             #using this global variable outside of bSearch within bSearch >>> normally poor programming practice (confusing)
    numCalls += 1
    if high - low < 2:
        return L[low] == e or L[high] == e
    mid = low + int((high - low)/2)
    if L[mid] == e:
        return True
    if L[mid] > e:
        return bSearch(L, e, low, mid - 1)
    else:
        return bSearch(L, e, mid + 1, high)
#don't only have to look at complexity of program itself (recursive function), or is it doing something more complex than I think


def search(L, e):
    return bSearch(L, e, 0, len(L) - 1)
#all this code does is call bSearch
#need to have a consistent interface for the search function (can go back and forth between linear and binary)
#just takes a list and an element when you call the search (gets rid of necessity for low and high input)


n = 100
while n < 50000000:
    L = range(n)
    numCalls = 0
    search(L, 100)
    print "When length =", str(len(L)), ", guesses =", numCalls
    n = n*2

#beauty of a logarithmic algorithm, takes very few steps to increase the input by many degrees of magnitude
#Order: O(log(n)) where n is len(L)
