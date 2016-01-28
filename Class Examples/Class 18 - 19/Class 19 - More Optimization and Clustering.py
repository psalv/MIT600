__author__ = 'paulsalvatore57'



                        #19 - More Optimization and Clustering


#Still working on greedy problem, we last left off with the brute force approach that was unfeasible

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

def dToB(n, numDigits):
    """requires: n is a natural number less than 2**numDigits
      returns a binary string of length numDigits representing the
              the decimal number n."""
    assert type(n)==int and type(numDigits)==int and n >=0 and n < 2**numDigits
    bStr = ''
    while n > 0:
        bStr = str(n % 2) + bStr
        n = n//2
    while numDigits - len(bStr) > 0:
        bStr = '0' + bStr
    return bStr

#If we want a vector to indicate which items are being taken, therefore we need a string of 0s (not taken) and 1s (taken)


#Generates a power set, or in other words all of the subsets of the set (every single one, exponential order)
def genPset(Items):
    """Generate a list of lists representing the power set of Items"""
    numSubsets = 2**len(Items)
    templates = []
    for i in range(numSubsets):
        templates.append(dToB(i, len(Items)))
    pset = []
    for t in templates:
        elem = []
        for j in range(len(t)):
            if t[j] == '1':
                elem.append(Items[j])
        pset.append(elem)
    return pset

#This will take constraints and give us the best set (or rather one of the best sets, there cn be multiple)
def chooseBest(pset, constraint, getVal, getWeight):
    bestVal = 0.0
    bestSet = None
    for Items in pset:
        ItemsVal = 0.0
        ItemsWeight = 0.0
        for item in Items:
            ItemsVal += item.getValue()
            ItemsWeight += item.getWeight()
        if ItemsWeight <= constraint and ItemsVal > bestVal:
            bestVal = ItemsVal
            bestSet = Items
    return (bestSet, bestVal)


def testBest():
    Items = buildItems()
    pset = genPset(Items)
    taken, val = chooseBest(pset, 20, Item.getValue, Item.getWeight)
    print ('Total value of items taken = ' + str(val))
    for item in taken:
        print '  ', item

# testBest()

#This finds a better answer then the greedy algorithm
    #Greedy finds local optimums, but is not guaranteed to reach a global optimum
    #This code finds the global optimum by looking at every possible combination
        #It is tempting to do things one step at a time (finding local optimums) because it is fast/easy, but no guarantee that it will work.



#This problem is INHERENTLY EXPONENTIAL; no matter what we do the worst case will be that we cannot no matter what find global optimum without this order









###MACHINE LEARNING: we've seen lesser examples of this (like a program 'learning' what the square root of a number is
    #Algorithms that allow computers to evolve behaviors based on empircal data
    #Recognize complex patterns and make intelligent decisions based upon it

    # INDUCTIVE INFERENCE: program observes examples representing incomplete data, tries to fit data and predict information about unseen data

    #1) Supervised Learning: associate a label with each example in a training set
            #Discrete label; classification problem (ex. credit card either does or does not belong to the owner)
            #Real-regression; real number, requires regression

            #Example: we have a graph with blue and red dots, and are trying to learn something based on their coordinates
                #Question 1: are the labels accurate (in real world often they are wrong)?
                #Question 2: is the past representative of the future?
                #Question 3: do you have enough data to generalize?
                #Question 4: feature abstractions (world is complex: which features are we going to choose for our abstractions?)
                #Question 5: how tight should the fit be?

            #There are many ways that data can be divided:
                #You can classify them all by colour and its good because minimizes training error (perfect classification of points)
                #Alternatively you can have training error > many factors (mislabelled, outlier) >>> we're looking for predictions
                    #If you over generalize your training data it might not fit well and give you false answers moving forward


    #2) Unsupervised Learning: have data but no labels; generally learning about regularities of the data (discover structure of data) > Optimization problem
            #Dominate form is clustering: organizing data into groups with similar features (which features are we interested in?)

            #Features we want:
                #Low intra-cluster dissimilarity (in same cluster are similar)
                #High inter-cluster dissimilarity (different clusters are very different)

            #Variance of cluster c = sum ((mean(c) - x)**2) >>> how far is each point from the mean, use it to find similarity within and between clusters

            #We can't just optimize for the two features above; every element will be put into it's own cluster of length 1
                #We need to add constraints to prevent a trivial answer

            #Constraints:
                #Maximum number of clusters
                #Maximum distance between clusters

            #People often use greedy algorithms: k-means, and hierarchical clustering



### Hierarchical clustering:
    #We have a set of n items to be clustered,  and an (n x n) distance matrix (telling how far points are from each other)

    #Assign each item to it's own cluster (we now have n clusters)
    #Find the most similar pair of clusters and merge them
    #Continue process until all items are in one cluster >>> AGGLOMERATIVE (combining things)

        #What does it mean to find the two most similar clusters? Easy when they have one element, not so obvious with many properties

    #LINKAGE CRITERION:
        #1) Single linkage: distance between a pair of clusters = shortest distance from any two members of the clusters (best case)
        #2) Complete linkage: distance between a pair of clusters = longest distance from any two members of the clusters (worst case)
        #3) Average linkage: distance between a pair of clusters = average distance from any two members of the clusters (medium case)

    #Complexity is at least O(n^2), very time consuming, and isn't guaranteed to find the optimal clustering
        #Making locally optimal decisions



    #Need to understand our features, most important factor to clustering.

    #Need to construct a FEATURE VECTOR incorporating multiple features
        # Ex. a city can be defined by <gps, population>