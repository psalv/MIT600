__author__ = 'paulsalvatore57'


                    #18 - Optimization Problems and Algorithms

import math
import random
# import matplotlib.pylab as pylab

#R**2 = 1 - EE/MV  (estimated error/measured variance)
    #Lays between O and 1, if it is 1 than this means that the model explains all of the variability in the data
    #0 means there is no linear relation between the data and the model (model is worthless in this situation)


def rSquare(measured, estimated):
    """measured: one dimensional array of measured values
       estimate: one dimensional array of predicted values"""
    EE = ((estimated - measured)**2).sum()
    mMean = measured.sum()/float(len(measured))
    MV = ((mMean - measured)**2).sum()
    return 1 - EE/MV


#No models are ever fully correct (leave out many factors) but many are good enough

#Can use models to answer relevant questions about data (example arrow model can be used to find the speed of the arrow)
    #Know it is a quadratic equation defines the flight of an arrow:
        #The vertical peak occurs at half of the x-axis

    #How long does it take? We have enough information to figure this out based on the distances from the peak
        #Falling speed is dependent on gravity (which is a constant)

        #t = sqrt(2*yPeak/g)    g = 9.8 m/s


def getXSpeed(a, b, c, minX, maxX):
    """minX and maxX are distances in inches"""
    xMid = (maxX - minX)/2.0
    yPeak = a*xMid**2 + b*xMid + c
    g = 32.16*12            #accel. of gravity in inches/sec/sec
    t = (2.0*yPeak/g)**0.5
    return xMid/(t*12.0)

def getTrajData(file):
    file = open(file, 'r')
    distances = []
    h1, h2, h3, h4 = [],[],[],[]
    discardHeader = file.readline()
    for line in file:
        d, ht1, ht2, ht3, ht4 = line.split()
        distances.append(float(d))
        h1.append(float(ht1))
        h2.append(float(ht2))
        h3.append(float(ht3))
        h4.append(float(ht4))
    file.close()
    return(distances, [h1, h2, h3, h4])

def processTrajectories(fName):
    distances, heights = getTrajData(fName)
    distances = pylab.array(distances)*36
    totHeights = pylab.array([0]*len(distances))
    for h in heights:
        totHeights = totHeights + pylab.array(h)
    pylab.title('Trajectory of Projectile (Mean of 4 Trials)')
    pylab.xlabel('Inches from Launch Point')
    pylab.ylabel('Inches Above Launch Point')
    meanHeights = totHeights/len(heights)
    pylab.plot(distances, meanHeights, 'bo')
    a,b,c = pylab.polyfit(distances, meanHeights, 2)
    altitudes = a*(distances**2) +  b*distances + c
    speed = getXSpeed(a, b, c, distances[-1], distances[0])
    pylab.plot(distances, altitudes, 'g',
               label = 'Quad. Fit' + ', R2 = '
               + str(round(rSquare(meanHeights, altitudes), 2))
               + ', Speed = ' + str(round(speed, 2)) + 'feet/sec')
    pylab.legend()

# processTrajectories('/Users/paulsalvatore57/PycharmProjects/MIT600/Class Examples/Class 18 - 19/TrajData')
# pylab.show()

#The speed that this gives is quite close, but not completely accurate



#1 - Start with an experiment producing data
#2 - Use computation to find and EVALUATE a model (convince ourselves that this is a good model of the system)
#3 - Use theory, analysis and computation to derive a consequence of the model






###OPTIMIZATION PROBLEMS: how do we write programs to find optimal solutions to real life problems

    #1) Objective function (maximized or minimized, ex. if we are looking for the cheapest flight from Boston to NYC)
    #2) Set of constraints that must be satisfied (ex. the flight can't take more than 3 hours)

#Problem reduction: take a problem and map it onto a problem that has already been solved.



#Burglar and napsack example: what do they decide to steal? >>> typically callde a 0/1 napsack problem (we need to take all of something or none, unlike continuous napsack)
    #Weight vs. value (how much to steal)

    #Greedy algorithm: iterative and at each step you choose the locally optimal solution



#It's good to start with a class so the rest of the data is easier (useful data abstractions):
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
        result = '<' + self.name + ', '\
                 + str(self.value) + ', '\
                 + str(self.weight) + '>'
        return result

def buildItems():
    names = ['clock', 'painting', 'radio', 'vase', 'book', 'computer']
    vals = [175,90,20,50,10,200]
    weights = [10,9,4,2,1,20]
    Items = []
    for i in range(len(vals)):
        Items.append(Item(names[i], vals[i], weights[i]))
    return Items

def greedy(Items, maxWeight, keyFcn):                               #The key function is what we mean by locally optimal
    assert type(Items) == list and maxWeight >= 0
    ItemsCopy = sorted(Items, key=keyFcn, reverse = True)           #Sort items based on the key function (weight, density, or value), and reverse it (most valuable first)
    result = []
    totalVal = 0.0
    totalWeight = 0.0
    i=0
    while totalWeight < maxWeight and i < len(Items):               #Taking the first thing from the list until we run out of weight
        if (totalWeight + ItemsCopy[i].getWeight()) <= maxWeight:
            result.append((ItemsCopy[i]))
            totalWeight += ItemsCopy[i].getWeight()
            totalVal += ItemsCopy[i].getValue()
        i += 1
    return (result, totalVal)


#Three possibilities
def value(item):
    return item.getValue()
def weightInverse(item):
    return 1.0/item.getWeight()
def density(item):
    return item.getValue()/item.getWeight()

def testGreedy(Items, constraint, getKey):
    taken, val = greedy(Items, constraint, getKey)
    print ('Total value of items taken = ' + str(val))
    print 'Taken: '
    for item in taken:
        print '  ', item

def testGreedys(maxWeight = 20):
    items = buildItems()
    print 'Available items:'
    for item in items:
        print ' ', item
    print '----------'
    print 'Greedy with max value:'
    testGreedy(items, maxWeight, value)
    print '----------'
    print 'Greedy with min weight:'
    testGreedy(items, maxWeight, weightInverse)
    print '----------'
    print 'Greedy with max ratio:'
    testGreedy(items, maxWeight, density)
    print '----------'

# testGreedys()


#Greedy programs are typically highly efficient

#What is the efficiency?
    #First sorts the list so this term is O(len(items)*log(len(n))  >>> O(nlogn)
    #Then the while loop iterates through the items O(len(items)    >>> O(n)

#We like greedy algorithms because they are very often linear order
    #A reason to not like them, however, is that sometimes locally optimal solutions do not coincide with globally optimal solutions



#What if we absolutely need the optimal set?
    #Once you have clearly defined the problem it is obvious to solve, at least in a brute force method

    #1) Represent each item by a pair (value and weight)
    #2) W = max weight that can be carried
    #3) Set of available items is a vector: I
    #4) Another vector representing what has been taken: v

            #  v[i] = 0 implies I[i] has not been taken
            #  v[i] = 1 implies I[i] has been taken

    #Maximize: Sum of v[i] * I[i].value (don't take it is 0*value, you do take it's 1*value)
    #Constraint: (Sum of v[i] * I[i].weight) <= W

    #Complexity:
        #1) If we implement this in the most straight forward way which is enumerating every possible combination: O(2^n) where n = len(items)
                #v gives a binary number
                #If number of items is small this isn't so bad, but as it gets larger the algorithm will take too long to be useful
