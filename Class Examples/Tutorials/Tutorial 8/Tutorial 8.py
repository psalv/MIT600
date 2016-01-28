__author__ = 'paulsalvatore57'


#The yield operator:
    #A generator object, this is used in the xrange function and it useful for memory considerations.
    #Rather than holding all of the values in memory, it will generate them one at a time and then discard them.

    #d.iterkeys() will do the same type of function but for keys in a dictionary (d)
    #also itervalues and iteritems
    #for (k, v) in d:    will generate the key and associated value

#Euclidean distance:
    #Generalizes to higher orders, therefore euclidean distance in three dimensions is sqrt(x**2 + y**2 + z**2), and so forth.

#Taking a random sample:
    #This piece of code will take a random sample of size 2 from the given list: random.sample([1, 2, 3, 4, 5,], 2)

                #8 - CLUSTERING

#Hierarchial clustering:
    #1) Assign each item to it's own cluster
    #2) Find the most similar clusters and merge them

        #This is based on linkage criteria:
            #Single (shortest distance between two members of clusters)
            #Complete (furthest distance between two members of clusters)
            #Average (average distance between between two members of clusters)

    #3) Continue until either you have your desired number of clusters, or until everything is in one cluster (agglomerative)

#K-means clustering:
    #1) Determine how many clusters you want to have initially, or k
    #2) Assign k points to k clusters, arbitrarily
    #3) Assign the remainder of the points to the most similar cluster
    #4) Assign k new clusters defined by the average of the already established (arbitrarily chosen) clusters
    #5) Repeat steps 3 and 4, monitoring how much change occurs (centroid movement) until it is sufficiently small

#K-means clustering is much more efficient on each iteration for a large number of points (advantage)
#K-means clustering is also random, or non-deterministic (disadvantage)
    #Hierarchial clustering will always yield the same results unlike K-means, therefore it is more reliable
    #This makes it necessary to perform multiple k-means clustering trials (do not rely on one trial)
#K-means has a degenerative condition (if you have a k value equal to n than the centroids will never move)


import string, random
import matplotlib.pylab as pylab


###HIERARCHIAL CLUSTERING:

#This creates the point, it contains information about the point such as how to calculate distance from another point.
#It also has supports normalization, wherein the attributes of the points (which define the point) may be altered.
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

#Contains linkage criteria (the metrics of the clusters)
#Has the ability to update and compute the centroid (used for k-mean clustering, the average).
#This class holds a set of points and knows what typ eof point it is holding.
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


    #This takes the new points of the cluster, sets them equal to self.points,
    #And computes the distance between the old and new centroid.
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


    #Totalling up all the points and taking the average
    #The array is first initialized to the correct length and then the attributes are added
    def computeCentroid(self):
        dim = self.points[0].dimensionality()
        totVals = pylab.array([0.0]*dim)
        for p in self.points:
            totVals += p.getAttrs()
        centroid = self.pointType('mean',
                                   totVals/float(len(self.points)),
                                   totVals/float(len(self.points)))
        return centroid

#-----------------------------------------------------------------------------------------------------------------------

#Key step is merging clusters (uses find closest to find which two to merge).
#The key methods are the mergeOne and mergeN (actually implements clustering) methods.
class ClusterSet(object):
    def __init__(self, pointType):
        self.members = []
    def add(self, c):
        if c in self.members:
            raise ValueError
        self.members.append(c)
    def getClusters(self):
        return self.members[:]


    #Takes the two clusters, adds the points from each cluster to a new cluster, newC.
    #It then removes the old clusters from members-the existing clusters-and adds the new cluster object.
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


    #Merges dependent on number of clusters:
    #1 = None, 2 = Merge, >2 = Merge based on distance metric
    #Return value will be the two merged clusters.
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


    #While we have more clusters than the number we desire we continue to iterate the mergeOne function.
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

#-----------------------------------------------------------------------------------------------------------------------

#This is a case-specific subclass of point, inheriting the properties of point,
#However also implementing scale features for normalization unique to this data set.
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

#This is a simple function to read the mammal datafile
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

#This function utilizes readMammalData and the mammal class to build the initial points of which will be clustered.
def buildMammalPoints(fName, scaling):
    nameList, featureList = readMammalData(fName)
    points = []
    for i in range(len(nameList)):
        point = Mammal(nameList[i], pylab.array(featureList[i]))
        point.scaleFeatures(scaling)                                #This allows us to do some scaling, will call the scaling fxn from the mammal class
        points.append(point)
    return points

#Using hierarchical clustering for the data set.
#The points are built, and then cluster objects are added to the ClusterSet object cS.
def test0(numClusters = 2, scaling = 'identity', printSteps = False,
          printHistory = True):
    points = buildMammalPoints('mammalTeeth.txt', scaling)
    cS = ClusterSet(Mammal)
    for p in points:
        cS.add(Cluster([p], Mammal))
    history = cS.mergeN(Cluster.maxLinkageDist, numClusters, toPrint = printSteps)
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





###K-MEANS:

def kmeans(points, k, cutoff, pointType, maxIters = 100, toPrint = False):
    #Get k randomly chosen initial centroids
    initialCentroids = random.sample(points, k)
    clusters = []
    #Create a singleton cluster for each centroid
    for p in initialCentroids:
        clusters.append(Cluster([p], pointType))
    numIters = 0
    biggestChange = cutoff
    #Maxiters is used in case the cutoff will never be reached, shoudl ensure both cutoff and maxIters are appropriate.
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
            #Add p to the list of points for the appropriate cluster (correct cluster is denoted by the index)
            newClusters[index].append(p)
        #Update each cluster and record how much the centroid has changed
        biggestChange = 0.0
        #This uses the update function which returns the change between the centroids
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



#Filters for the clusters, telling what should be used in the clustering criteria
#Different features will give different clustering
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
            #Choosing best clustering as the smallest max distance from a point to a centroid (want the clusters to be compact)
            bestDistance = maxSmallest
            bestClustering = copy.deepcopy(clusters)
        if printClusters:
            print 'Clusters:'
        for i in range(len(clusters)):
            if printClusters:
                print '  C' + str(i) + ':', clusters[i]
    for c in bestClustering:
        #Drawing a histogram of the average income of each cluster
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


test(k = 5, filterName = 'all', printClusters = False)
pylab.title('All Features')
pylab.figure()

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