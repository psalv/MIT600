__author__ = 'paulsalvatore57'


                        #20 - More Clustering



#From last lecture, we need to remember that linkage criteria selection is important for clustering to give useful results
    #Adding more features makes clustering complex


#Feature Vector: represents features (typically a vector of numbers)
    #Can look at euclidean distance between vectors now to determine relation

    #This can be misleading though, because different measurements are defined as different by different amplitudes (ex. distance vs temperature)
        #How are we going to SCALE the elements of the vectors? >>> Even same units must you must scale
        #Look at the DYNAMIC RANGE of the data
            #Need to think about how you scale, will have dramatic effect on outcome



#CRITICAL STEP: Feature selection and scaling (where most of the work is done)
    #Domain knowledge: We have to think about the objects that we are trying to learn about, and what the objective of the learning process is



#Scaling often done with MINKOWSKI METRIC:
    #Distance between two vectors  (X1 and X2, p), where p is degree:

            # Take the absolute difference between each vector, raise it to the p of p
            # Do this for all elements, sum them, and then raise it to the power of 1/p (the pth root)

                #If p = 1 this is the Manhattan distance (grid-like degree)
                    #This is often used for genes
                #If p = 2 we have already done this, we are getting th euclidean distance




#Often have to compare nominal categories (non-numeric)
    #Typical we convert these nominal categories to a number and then have a way to relate these numbers:

    #Ex. Blue = 0.0, Green = 0.5, Brown = 1.0 indicated that we think blue eyes are closer to green eyes than they are to brown eyes
        #Requires knowledge of the domain (not mathematically difficult, but difficult judgment calls)

    #Scaling-normalization: often we want every feature to be normalized between 0 and 1
        #Not necessarily always true because some features may have increased importance, and therefore increased weight





#Clustering of mammals example
    #What features do we want? Well what are we trying to do
    #We are trying to cluster mammals based upon how they eat
        #This needs to be done without any direct information about what they eat
        #Often machine learning is done with limited or no data about what we are trying to discover

    #Starting with the hypothesis that you can infer eating habits based on dental morphology

    #Our data has types of teeth, and how much of each tooth given mammals have


import matplotlib.pylab as pylab
import random, copy, string


#This is a useful class for various clustering problems, not just this one:
    #He didn't include this code and said not to worry about it but I feel retyping it reinforces elements about classes for me

#I copied it all out like an idiot when he provides lecture code in two different formats, this is the second time I've learned this lesson.





#An abstraction of things to be clustered, this is a set of classes that will be used for various aspects of clustering
class Point(object):
    def __init__(self, name, originalAttrs, normalizedAttrs = None):
        """normalizedAttrs and originalAttrs are both arrays"""
        self.name = name
        self.unNormalized = originalAttrs
        if normalizedAttrs == None:
            self.attrs = originalAttrs
        else:
            self.attrs = normalizedAttrs
    def dimensionality(self):
        return len(self.attrs)
    def getAttrs(self):
        return self.attrs
    def getOriginalAttrs(self):
        return self.unNormalized
    def distance(self, other):
        #Euclidean distance metric
        result = 0.0
        for i in range(self.dimensionality()):
            result += (self.attrs[i] - other.attrs[i])**2
        return result**0.5
    def getName(self):
        return self.name
    def toStr(self):
        return self.name + str(self.attrs)
    def __str__(self):
        return self.name


class Cluster(object):
    def __init__(self, points, pointType):
        self.points = points
        self.pointType = pointType
        self.centroid = self.computeCentroid()
    def singleLinkageDist(self, other):
        minDist = self.points[0].distance(other.points[0])
        for p1 in self.points:
            for p2 in other.points:
                if p1.distance(p2) < minDist:
                    minDist = p1.distance(p2)
        return minDist
    def maxLinkageDist(self, other):
        maxDist = self.points[0].distance(other.points[0])
        for p1 in self.points:
            for p2 in other.points:
                if p1.distance(p2) > maxDist:
                    maxDist = p1.distance(p2)
        return maxDist
    def averageLinkageDist(self, other):
        totDist = 0.0
        for p1 in self.points:
            for p2 in other.points:
                totDist += p1.distance(p2)
        return totDist/(len(self.points)*len(other.points))
    def update(self, points):
        oldCentroid = self.centroid
        self.points = points
        if len(points) > 0:
            self.centroid = self.computeCentroid()
            return oldCentroid.distance(self.centroid)
        else:
            return 0.0
    def members(self):
        for p in self.points:
            yield p
    def isIn(self, name):
        for p in self.points:
            if p.getName() == name:
                return True
        return False
    def toStr(self):
        result = ''
        for p in self.points:
            result = result + p.toStr() + ', '
        return result[:-2]
    def __str__(self):
        names = []
        for p in self.points:
            names.append(p.getName())
        names.sort()
        result = ''
        for p in names:
            result = result + p + ', '
        return result[:-2]
    def getCentroid(self):
        return self.centroid
    def computeCentroid(self):
        dim = self.points[0].dimensionality()
        totVals = pylab.array([0.0]*dim)
        for p in self.points:
            totVals += p.getAttrs()
        centroid = self.pointType('mean',
                                   totVals/float(len(self.points)),
                                   totVals/float(len(self.points)))
        return centroid


#Key step is merging clusters (uses find closest to find which two to merge)
class ClusterSet(object):
    def __init__(self, pointType):
        self.members = []
    def add(self, c):
        if c in self.members:
            raise ValueError
        self.members.append(c)
    def getClusters(self):
        return self.members[:]
    def mergeClusters(self, c1, c2):
        points = []
        for p in c1.members():
            points.append(p)
        for p in c2.members():
            points.append(p)
        newC = Cluster(points, type(p))
        self.members.remove(c1)
        self.members.remove(c2)
        self.add(newC)
        return c1, c2
    def findClosest(self, metric):
        minDistance = metric(self.members[0], self.members[1])
        toMerge = (self.members[0], self.members[1])
        for c1 in self.members:
            for c2 in self.members:
                if c1 == c2:
                    continue
                if metric(c1, c2) < minDistance:
                    minDistance = metric(c1, c2)
                    toMerge = (c1, c2)
        return toMerge
    def mergeOne(self, metric, toPrint = False):
        if len(self.members) == 1:
            return None
        if len(self.members) == 2:
            return self.mergeClusters(self.members[0],
                                      self.members[1])
        toMerge = self.findClosest(metric)
        if toPrint:
            print 'Merged'
            print '  ' + str(toMerge[0])
            print 'with'
            print '  ' + str(toMerge[1])
        self.mergeClusters(toMerge[0], toMerge[1])
        return toMerge
    def mergeN(self, metric, numClusters = 1, history = [],
               toPrint = False):
        assert numClusters >= 1
        while len(self.members) > numClusters:
            merged = self.mergeOne(metric, toPrint)
            history.append(merged)
        return history
    def numClusters(self):
        return len(self.members) + 1
    def __str__(self):
        result = ''
        for c in self.members:
            result = result + str(c) + '\n'
        return result




#Mammal's teeth example, this is a subclass of point since these are the points that we will be clustering
class Mammal(Point):
    def __init__(self, name, originalAttrs, scaledAttrs = None):
        Point.__init__(self, name, originalAttrs, originalAttrs)
    def scaleFeatures(self, key):
        scaleDict = {'identity': [1,1,1,1,1,1,1,1],
                     '1/max': [1/3.0,1/4.0,1.0,1.0,1/4.0,1/4.0,1/6.0,1/6.0]}
        scaledFeatures = []
        features = self.getOriginalAttrs()
        for i in range(len(features)):
            scaledFeatures.append(features[i]*scaleDict[key][i])
        self.attrs = scaledFeatures

def readMammalData(fName):
    dataFile = open(fName, 'r')
    teethList = []
    nameList = []
    for line in dataFile:
        if len(line) == 0 or line[0] == '#':
            continue
        dataLine = string.split(line)
        teeth = dataLine.pop(-1)
        features = []
        for t in teeth:
            features.append(float(t))
        name = ''
        for w in dataLine:
            name = name + w + ' '
        name = name[:-1]
        teethList.append(features)
        nameList.append(name)
    return nameList, teethList

def buildMammalPoints(fName, scaling):
    nameList, featureList = readMammalData(fName)
    points = []
    for i in range(len(nameList)):
        point = Mammal(nameList[i], pylab.array(featureList[i]))
        point.scaleFeatures(scaling)                                #This allows us to do some scaling, will call the scaling fxn from the mammal class
        points.append(point)
    return points

#Use hierarchical clustering for mammals teeth
def test0(numClusters = 2, scaling = 'identity', printSteps = False,
          printHistory = True):
    points = buildMammalPoints('mammalTeeth.txt', scaling)
    cS = ClusterSet(Mammal)
    for p in points:
        cS.add(Cluster([p], Mammal))
    history = cS.mergeN(Cluster.maxLinkageDist, numClusters,
                        toPrint = printSteps)
    if printHistory:
        print ''
        for i in range(len(history)):
            names1 = []
            for p in history[i][0].members():
                names1.append(p.getName())
            names2 = []
            for p in history[i][1].members():
                names2.append(p.getName())
            print 'Step', i, 'Merged', names1, 'with', names2
            print ''
    clusters = cS.getClusters()
    print 'Final set of clusters:'
    index = 0
    for c in clusters:
        print '  C' + str(index) + ':', c
        index += 1

# test0()
# The way this is gives us poor clustering, why?
#         Some teeth have different DYNAMIC RANGES than others >>> we have scaling set to identity
#         Because of this we may be skewing our clustering

# test0(scaling = '1/max')        #Used string for scalings so you can remember what they represent, this is useful
    #By dividing by the max we have normalized the data

    #This will gives us better clustering
    #We have been able to use machine learning to infer a new fact, something similar within clusters and different between










def kmeans(points, k, cutoff, pointType, maxIters = 100,
           toPrint = False):
    #Get k randomly chosen initial centroids
    initialCentroids = random.sample(points, k)
    clusters = []
    #Create a singleton cluster for each centroid
    for p in initialCentroids:
        clusters.append(Cluster([p], pointType))
    numIters = 0
    biggestChange = cutoff
    while biggestChange >= cutoff and numIters < maxIters:
        #Create a list containing k empty lists
        newClusters = []
        for i in range(k):
            newClusters.append([])
        for p in points:
            #Find the centroid closest to p
            smallestDistance = p.distance(clusters[0].getCentroid())
            index = 0
            for i in range(k):
                distance = p.distance(clusters[i].getCentroid())
                if distance < smallestDistance:
                    smallestDistance = distance
                    index = i
            #Add p to the list of points for the appropriate cluster
            newClusters[index].append(p)
        #Update each cluster and record how much the centroid has changed
        biggestChange = 0.0
        for i in range(len(clusters)):
            change = clusters[i].update(newClusters[i])
            biggestChange = max(biggestChange, change)
        numIters += 1
    #Calculate the coherence of the least coherent cluster
    maxDist = 0.0
    for c in clusters:
        for p in c.members():
            if p.distance(c.getCentroid()) > maxDist:
                maxDist = p.distance(c.getCentroid())
    print 'Number of iterations =', numIters, 'Max Diameter =', maxDist
    return clusters, maxDist





# #US Counties example
class County(Point):
    #Interesting subsets of features
    #0=don't use, 1=use
    noWealth = (('HomeVal', '0'), ('Income', '0'), ('Poverty', '0'),
                    ('Population', '1'), ('Pop Change', '1'),
                    ('Prcnt 65+', '1'), ('Below 18', '1'),
                    ('Prcnt Female', '1'), ('Prcent HS Grad', '1'),
                    ('Prcnt College', '1'), ('Unemployed', '0'),
                    ('Prcent Below 18', '1'), ('Life Expect', '1'),
                    ('Farm Acres', '1'))
    wealthOnly = (('HomeVal', '1'), ('Income', '1'), ('Poverty', '1'),
                    ('Population', '0'), ('Pop Change', '0'),
                    ('Prcnt 65+', '0'), ('Below 18', '0'),
                    ('Prcnt Female', '0'), ('Prcent HS Grad', '0'),
                    ('Prcnt College', '0'), ('Unemployed', '1'),
                    ('Prcent Below 18', '0'), ('Life Expect', '0'),
                    ('Farm Acres', '0'))
    education = (('HomeVal', '0'), ('Income', '0'), ('Poverty', '0'),
                    ('Population', '0'), ('Pop Change', '0'),
                    ('Prcnt 65+', '0'), ('Below 18', '0'),
                    ('Prcnt Female', '0'), ('Prcent HS Grad', '1'),
                    ('Prcnt College', '1'), ('Unemployed', '0'),
                    ('Prcent Below 18', '0'), ('Life Expect', '0'),
                    ('Farm Acres', '0'))
    noEducation = (('HomeVal', '1'), ('Income', '0'), ('Poverty', '1'),
                    ('Population', '1'), ('Pop Change', '1'),
                    ('Prcnt 65+', '1'), ('Below 18', '1'),
                    ('Prcnt Female', '1'), ('Prcent HS Grad', '1'),
                    ('Prcnt College', '0'), ('Unemployed', '0'),
                    ('Prcent Below 18', '1'), ('Life Expect', '1'),
                    ('Farm Acres', '1'))
    allFeatures = (('HomeVal', '1'), ('Income', '0'), ('Poverty', '1'),
                    ('Population', '1'), ('Pop Change', '1'),
                    ('Prcnt 65+', '1'), ('Below 18', '1'),
                    ('Prcnt Female', '1'), ('Prcent HS Grad', '1'),
                    ('Prcnt College', '1'), ('Unemployed', '1'),
                    ('Prcent Below 18', '1'), ('Life Expect', '1'),
                    ('Farm Acres', '1'))
    filterNames = {'all': allFeatures, 'education': education,
                   'noEducation': noEducation,
                   'wealthOnly': wealthOnly,'noWealth': noWealth}
    attrFilter = None
    #Override Point to construct subset of features
    def __init__(self, name, originalAttrs, normalizedAttrs = None,
                 filterName = 'all'):
        if County.attrFilter == None:
            County.attrFilter = ''
            filterSpec = County.filterNames[filterName]
            for f in filterSpec:
                County.attrFilter += f[1]
        Point.__init__(self, name, originalAttrs, normalizedAttrs)
        features = []
        for i in range(len(County.attrFilter)):
            if County.attrFilter[i] == '1':
                features.append((self.getAttrs()[i]))
        self.features = features
    #Override Point.distance to use only subset of features
    def distance(self, other):
        result = 0.0
        for i in range(len(self.features)):
            result += (self.features[i] - other.features[i])**2
        return result**0.5

def readCountyData(fName, numEntries = 14):
    dataFile = open(fName, 'r')
    dataList = []
    nameList = []
    maxVals = pylab.array([0.0]*numEntries)
    #Build unnormalized feature vector
    for line in dataFile:
        if len(line) == 0 or line[0] == '#':
            continue
        dataLine = string.split(line)
        name = dataLine[0] + dataLine[1]
        features = []
        #Build vector with numEntries features
        for f in dataLine[2:]:
            try:
                f = float(f)
                features.append(f)
                if f > maxVals[len(features)-1]:
                    maxVals[len(features)-1] = f
            except ValueError:
                name = name + f
        if len(features) != numEntries:
            continue
        dataList.append(features)
        nameList.append(name)
    return nameList, dataList, maxVals

def buildCountyPoints(fName, filterName = 'all', scale = True):
    nameList, featureList, maxVals = readCountyData(fName)
    points = []
    for i in range(len(nameList)):
        originalAttrs = pylab.array(featureList[i])
        if scale:
            normalizedAttrs = originalAttrs/pylab.array(maxVals)
        else:
            normalizedAttrs = originalAttrs
        points.append(County(nameList[i], originalAttrs,
                             normalizedAttrs, filterName))
    return points

def getAveIncome(cluster):
    tot = 0.0
    numElems = 0
    for c in cluster.members():
        tot += c.getOriginalAttrs()[1]
        numElems += 1
    if numElems > 0:
        return tot/numElems
    return 0.0

def test(k = 50, cutoff = 0.01, numTrials = 1, myHome = 'MAMiddlesex',
         filterName = 'all', printPoints = False,
         printClusters = True):
    #Build the set of points
    points = buildCountyPoints('counties.txt', filterName)
    if printPoints:
        print 'Points'
        for p in points:
            attrs = p.getAttrs()
            for i in range(len(attrs)):
                attrs[i] = round(attrs[i], 2)
            print '  ', p, attrs
    numClusterings = 0
    bestDistance = None
    #Run k-means multiple times and choose best
    while numClusterings < numTrials:
        print 'Starting clustering number', numClusterings
        clusters, maxSmallest = kmeans(points, k, cutoff, County)
        numClusterings += 1
        if bestDistance == None or maxSmallest < bestDistance:
            bestDistance = maxSmallest
            bestClustering = copy.deepcopy(clusters)
        if printClusters:
            print 'Clusters:'
        for i in range(len(clusters)):
            if printClusters:
                print '  C' + str(i) + ':', clusters[i]
    for c in bestClustering:
        incomes = []
        for i in range(len(bestClustering)):
            incomes.append(getAveIncome(bestClustering[i]))
            if printClusters:
                print '  C' + str(i) + ':', bestClustering[i]
        pylab.hist(incomes)
        pylab.xlabel('Ave. Income')
        pylab.ylabel('Number of Clusters')
        if c.isIn(myHome):
            print '\nHome Cluster:', c
            print 'Ave. income =', round(getAveIncome(c),0)


#test(k = 5, filterName = 'all', printClusters = False)
#pylab.title('All Features')
#pylab.figure()
#test(k = 5, filterName = 'wealthOnly', printClusters = False)
#pylab.title('Home Value, Income, Unemployed')
#pylab.figure()
#test(k = 50, filterName = 'education', numTrials = 5, printClusters = False)
#pylab.title('Education Level')
#pylab.show()
#test(k = 50, filterName = 'all', numTrials = 2, printClusters = False)
#pylab.title('All Features')
#pylab.figure()
#test(k = 50, filterName = 'noEducation', numTrials = 2, printClusters = False)
#pylab.title('All - Education')
#pylab.show()

def test1(k = 2, cutoff = 0.0001, numTrials = 1, printSteps = False,
          printHistory = False):
    points = buildMammalPoints('mammalTeeth.txt', '1/max')
    if printSteps:
        print 'Points:'
        for p in points:
            attrs = p.getOriginalAttrs()
            for i in range(len(attrs)):
                attrs[i] = round(attrs[i], 2)
            print '  ', p, attrs
    numClusterings = 0
    bestDiameter = None
    while numClusterings < numTrials:
        clusters, maxDiameter = kmeans(points, k, cutoff, Mammal)
        if bestDiameter == None or maxDiameter < bestDiameter:
            bestDiameter = maxDiameter
            bestClustering = copy.deepcopy(clusters)
        if printHistory:
            print 'Clusters:'
            for i in range(len(clusters)):
                print '  C' + str(i) + ':', clusters[i]
        numClusterings += 1
    print '\nBest Clustering'
    for i in range(len(bestClustering)):
        print '  C' + str(i) + ':', bestClustering[i]

#Use hierarchical clustering for counties
#It will run for a VERY long time
def test3(fileName, scale = False, filterName = 'all',
          printSteps = False, printHistory = False):
    points = buildCountyPoints(fileName, filterName = filterName,
                               scale = scale)
    cS = ClusterSet(County)
    for p in points:
        cS.add(Cluster([p], County))
    history = cS.mergeN(Cluster.maxLinkageDist, 2, toPrint = printSteps)
    if printHistory:
        print ''
        for i in range(len(history)):
            names1 = []
            for p in history[i][0].members():
                names1.append(p.getName())
            names2 = []
            for p in history[i][1].members():
                names2.append(p.getName())
            print 'Step', i, 'Merged', names1, 'with', names2
            print ''
    clusters = cS.getClusters()
    print ''
    print 'Final set of clusters:'
    index = 0
    for c in clusters:
        print '  C' + str(index) + ':', c
        index += 1

# test3()
# This will take an extremely long time to run, the first step will take 3100**2 trials since this is the size of our sample, the next merge will need to do this again

# test3('newEngland.txt')
#This gives us a strange clustering, however Middlesex is enormous in terms of population compared to everywhere else
    #This skewed the data since it was not normalized so we are getting clustering just dependant on population


#To do scaling instead of doing it by hand what we are doing is keeping track of the maximum of each feature while building the points and do the scaling automatically
# test3('newEngland.txt', scale = True)
#This gives us very different clustering based on different parameters






#k-means clustering: this is a different type of clustering that can be used on large data sets
    #O = n, as we get to larger sets anything above linear order is ineffective

    #Step 1: choose k >>> the total number of clusters that you want when you are done, one of the issue is how do you choose k?

    #Step 2: choose k points as initial centroid, often we chose k points at random, each called a centroid

        #The centroid is the "average" point of all of the points available

    #Step 3: assign each point to the nearest centroid (we usually choose a low number of centroids, such as 50)
        #The initial assignment will be random, therefore not very useful

    #Step 4: for each of the k clusters choose a new centroid
        #Before centroids were choosen at random, however we now have a cluster with a bunch of points in it so we can take the average to compute a centroid

    #Step 5: assign each point to nearest centroid

    #Step 6: repeat steps 4 and 5 until the change is very small
        #We can keep track of how many points are moved from one cluster to another in step 5, a measure of how much change has occurred

