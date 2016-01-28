__author__ = 'paulsalvatore57'


            #23 - Dynamic Programming


#Properties that allow dynamic programming to be applicable:

    #1) Optimal substructure: can construct a globally optimal solution by combining solutions to sub-problems.

    #2) Overlapping sub-problems: need to solve the same problem multiple times > use memoization for look up instead of resolving the problem.

#Using these parameters we think of our mergeSort program: it does not contain overlapping sub-problems therefore is not a problem for dynamic programming.

#Alternatively the shortestPath program doesn't necessarily have optimal substructure (shortest form A > B + B > C is not necessarily shortest from A > C, can be dif. links).
    #If you have the shortest path from A > C defined as A > B > D > E > C, than we know the shortest path from B > E,
    #This is the optimal substructure that we have and therefore the structure we can exploit.




#Know we consider the knapsack problem (optimization). The knapsack problem uses a depth first search method and backtracking to iterate through every possibility.
    #To ask if dynamic programming can be used to solve this problem we ask does this problem exhibit the two properties listed above.

    #1) Optimal substructure: Yes, since if you know the value for each locally different combination of elements we can find the global optimum.
        #Each parent node selects the better of the children.

    #2) Overlapping sub-problems:
        #Our problem is: given a set of items, and an available weight, which items should we take?
        #We need to know how much weight we have available but not why (don't need to now which items we have already taken).
            #This is because there may be many sets of items adding up to the same weight, and therefore the same problem to solve.

        #YOU STILL MUST KEEP TRACK OF WHICH ITEMS ARE AVAILABLE. That is important, however the taken items is not.




import random

class Item(object):
    def __init__(self, n, v, w):
        self.name = n
        self.value = float(v)
        self.weight = float(w)
    def getName(self):
        return self.name
    def getValue(self):
        return self.value
    def getWeight(self):
        return self.weight
    def __str__(self):
        result = '<' + self.name + ', ' + str(self.value) + ', '\
                 + str(self.weight) + '>'
        return result

def buildManyItems(numItems, maxVal, maxWeight):
    Items = []
    for i in range(numItems):
        Items.append(Item(str(i), random.randrange(1, maxVal), random.randrange(1, maxWeight)))
        # Items.append(Item(str(i), random.randrange(1, maxVal), random.randrange(1, maxWeight)*random.random()))
    return Items



#After reading the code below this is how I interpreted it to work:
    #1) Check to see if the list of available items is empty, if so the result will also be empty.
    #2) Checks to see if the first item in available list will put you over weight, if so removes it from the list (not useable) and runs solve again.
    #3) Considers the first item:
        #Either runs solve with that item, removing it from weight and taking it's value > recursively calls to repeat this process
        #Or skips the first item and runs solve recursively with the same weight as before.
        #These steps will iterate through every feasible item combination until the toConsider list is emty at which point it will come out of the list,
        #Return the results, and at each recursive level it will compare which value is higher (with or without an item) and the higher value will move forward.
    #4) When everything comes out of the recursive calls the final comparison of with/without the first item will be made, at which point an answer will be returned.

def solve(toConsider, avail):
    global numCalls
    numCalls += 1
    if toConsider == [] or avail == 0:
        result = (0, ())
    elif toConsider[0].getWeight() > avail:
        result = solve(toConsider[1:], avail)
    else:
        nextItem = toConsider[0]
        #Explore left branch
        withVal, withToTake = solve(toConsider[1:], avail - nextItem.getWeight())
        withVal += nextItem.getValue()
        #Explore right branch
        withoutVal, withoutToTake = solve(toConsider[1:], avail)
        #Choose better branch
        if withVal > withoutVal:
            result = (withVal, withToTake + (nextItem,))
        else:
            result = (withoutVal, withoutToTake)
    return result

def smallTest(numItems = 10, maxVal = 20, maxWeight = 15):
    global numCalls
    numCalls = 0
    Items = buildManyItems(numItems, maxVal, maxWeight)
    val, taken = solve(Items, 50)
    for item in taken:
        print(item)
    print 'Total value of items taken = ' + str(val)
    print 'Number of calls = ' + str(numCalls)

# smallTest()






#In fast solve we are incorporating a memo (initially set to known because it is an implementation feature, not a specification feature).

#A feature of python this is exploring deals with mutable objects:
    #When memo = None in the initially call of fastSolve, this will only be true for the first call of the function.
    #The next call, when memo becomes a dict, this dict is what will be put in place of the None object.
    #This means that if you call fastSolve two separate times in a program (unrelated instances) that the memo will carry over, giving the wrong answer.
    #To get around this we reinitialize memo with each call when it is None.

def fastSolve(toConsider, avail, memo = None):
    global numCalls
    numCalls += 1
    if memo == None:
        #Initialize for first invocation
        memo = {}
    if (len(toConsider), avail) in memo:
        #Use solution found earlier: toConsider is a list of items and the length keeps track of where we are in the list
        result = memo[(len(toConsider), avail)]
        return result
    elif toConsider == [] or avail == 0:
        result = (0, ())
    elif toConsider[0].getWeight() > avail:
        #Lop off first item in toConsider and solve
        result = fastSolve(toConsider[1:], avail, memo)
    else:
        item = toConsider[0]
        #Consider taking first item
        withVal, withToTake = fastSolve(toConsider[1:], avail - item.getWeight(), memo)
        withVal += item.getValue()
        #Consider not taking first item
        withoutVal, withoutToTake = fastSolve(toConsider[1:], avail, memo)
        #Choose better alternative
        if withVal > withoutVal:
            result = (withVal, withToTake + (item,))
        else:
            result = (withoutVal, withoutToTake)
    #Update memo
    memo[(len(toConsider), avail)] = result
    return result





import time
import sys
sys.setrecursionlimit(2000) #This code increases the recursion depth limit of python such that this will not raise an error.
def test(maxVal = 10, maxWeight = 10, runSlowly = False):
    random.seed(0)
    global numCalls
    capacity = 8*maxWeight
    print '#items, #num taken, Value, Solver, #calls, time'
    for numItems in (4,8,16,32,64,128,256,512,1024):
        Items = buildManyItems(numItems, maxVal, maxWeight)
        if runSlowly:
            tests = (fastSolve, solve)      #Want to try both to solve, this means that the parameters must be the same (this is important).
        else:
            tests = (fastSolve,)
        for func in tests:
            numCalls = 0
            startTime = time.time()
            val, toTake = func(Items, capacity)
            elapsed = time.time() - startTime
            funcName = func.__name__
            print numItems, len(toTake), val, funcName, numCalls, elapsed

test()

#Running time is dependent on the constant time of look something up in memo:
    #Number of elements in mem is dependent on number of possible value in toConsider and avail.
    #toConsider is governed by number of items,
    #avil depends upon initial available weight, as well as the number of different weights the sets of items can add up to.
    #Lower number of items means you have a lower number of possible sums.

#If you increase the number of possible weights (seen in the commented out code in items that multiplies by random.random) there are infinite possibilities.
    #Not probable for weights to be found in the memo so fastSolve is doing the same job as solve.

#This problem is pseudo-polynomial time (meaning that it is sometimes polynomial but there are cases where it will be exponential).

