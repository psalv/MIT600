__author__ = 'paulsalvatore57'



                # Tutorial 10



#Key idea of dynamic programming is to not have to compute things multiple times, it is a form of laziness

#Requires optimal substructure (local optimum combine to global optimums) and overlapping subproblems (big problem can be broken down into smaller problems).


#An example is the fibonacci function:

    # f0 = 0
    # f1 = 1
    # fn = fn-1 + fn-2  If you combine the solution for the n-1 and n-2 solution you get the solution for n

#No dynamic programming:
def fib(num):
    global steps
    steps += 1
    if num == 1 or num == 0:
        return num
    else:
        return fib(num-1) + fib(num-2)
def testFib(n):
    global steps
    for i in xrange(n):
        print '%24s' %('The {} fibonacci number:'.format(i)), '%7s' %(fib(i)), '%7s' %('  Steps: '), '%10d' %(steps)
        steps = 0

# testFib(40)

#This code is extremely inefficient to compute the fibonacci number since it must recalculate each instance many times.
#This code struggles to get to the 40th fibonacci number as opposed to below:



def fibDyn(num, visited):
    global steps
    if num == 0:
        return 0, visited
    if num == 1:
        return 1, visited
    steps += 1
    answer = visited[0] + visited[1]
    visited.pop(0)
    visited.append(answer)
    return answer, visited

steps = 0

def testFibDyn(n):
    global steps
    visited = [0, 1]
    for i in xrange(n):
        new = fibDyn(i, visited)
        print '%24s' %('The {} fibonacci number:'.format(i)), '%7s' %(new[0])
        if steps > 1:
            raise ValueError
        steps = 0
        visited = new[1]

# testFibDyn(200)

#This dynamic implementation can get to the 20000th fibonacci number before the previous can get to the 40th, this is a massive difference, each call is only one step.

#This now has a linear complexity.





#Here is a way that he implemented it in a single function, this is honestly way better but I'm positive I could have worked this out:

def hisFibDyn(n, memo = None):
    if memo == None:
        memo = {0:0, 1:1}

    global steps
    steps += 1

    if n not in memo:
        memo[n] = hisFibDyn(n - 1, memo) + hisFibDyn(n - 2, memo)

    return memo[n]

import sys
sys.setrecursionlimit(10000)
# print hisFibDyn(500), 'Steps: ', steps





#The next example looks at the number of paths that a robot can take to get from one side of a rectangle to another.
#This can be broken down into if n or m = 1 there is only one path (base case).

def robotPaths(n, m):
    global steps
    steps += 1
    if n == 1 or m == 1:
        return 1
    else:
        return robotPaths(n-1, m) + robotPaths(n, m-1)

# print robotPaths(14, 14), 'Steps: ', steps






def robotPathsDyn(n, m, memo = None):
    global steps

    if memo == None:
        memo = {}

    if (n, m) not in memo:
        steps += 1

        if n == 1 or m == 1:
            memo[(n, m)] = 1

        else:
            memo[(n, m)] = robotPathsDyn(n-1, m, memo) + robotPathsDyn(n, m-1, memo)

        memo[(m, n)] = memo[(n, m)]

    return memo[(m, n)]

# print robotPathsDyn(140, 140), steps



#18:00