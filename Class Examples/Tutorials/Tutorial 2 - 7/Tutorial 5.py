__author__ = 'paulsalvatore57'


            #ALGORITHM COMPLEXITY

#Big oh notation gives us an upper bound on how long something will take (but it is not a time bound)
    #informs us of how many steps something will take
    #concerned about extremely large inputs

#Big oh notation allows us to compare two notations by comparing the ratio:
    #A1 runs at O(n)
    #A2 runs at O(n^3)
    #A2 is expected to run n^2 times slower than A1

#Ignore multiplicity since we are concerned with the lim as n approaches infinity
#We also ignore lower degree big O notation when there are many:
    #ex. O(n^2 + n^3) = O(n^3), because this term will dominate at large n values



def count_ts(a_str):
     count = 0
     for char in a_str:
        if char == 't':
           count += 1
     return count
 #if equality is not constant time (depending on class) it may not be constant time
 #strings are constant time, but for instance ints are not (as I remember from lecture)
 #here n = size a_str


def count_same_ltrs(a_str, b_str):
     count = 0
     for char in a_str:
        if char in b_str:
           count += 1
     return count
#worst case is that if character isn't in b string, you must look at every element of that string
#for loop is executed n times, innerbody is executed m times (where m = len(b_str))
#order nm complexitym O*(nm)


def factorial3(n):
     result = 1
     while n > 0:
        result *= n
        n -= 1
     return result
#O(n) complexitu, cnstant time operations within the linear while loop


def char_split(a_str):
     result = []
     index = 0
     while len(a_str) != len(result):
        result.append(a_str[index])
        index += 1
     return result
#everything in this is constant time
#O(n), where n = len(a_str)


#NOT ALL STRING AND LIST OPERATIONS ARE CONSTANT TIME:
    # http://wiki.python.org/moin/TimeComplexity, want to look for worst case

    #Things like slicing and copying are not constant time, depends on size of list/slice


def r_factorial(n):
     if n <= 0:
        return 1
     else:
        return n*r_factorial(n-1)
#O(n) complexity, since it needs to execute the recursive functions n times


def foo(n):
     if n <= 1:
        return 1
     return foo(n/2) + 1
#decreasing at an exponential rate
#O(logb(n)) >>> where recursive function is calling n/b
    #in this case n/2 is being called recursively so the complexity is O(log2(n))

#    n/2^x = 1
#        n = 2^x
#    log2n = log2(2^x)
#        x = log2n


#Fibonacci: the call tree grows, n levels of the tree to get down to n, branching factor of 2
#n levels, branching factor of 2, so complexity O(2^n)



