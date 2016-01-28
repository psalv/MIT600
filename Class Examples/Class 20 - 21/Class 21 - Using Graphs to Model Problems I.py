__author__ = 'paulsalvatore57'


                #21 - Using Graphs to Model Problems I



#Code shared across examples
import random, string, copy
import matplotlib.pylab as pylab

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

#Mammal's teeth example
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
        point.scaleFeatures(scaling)
        points.append(point)
    return points

#Use hierarchical clustering for mammals teeth
def test0(numClusters = 2, scaling = 'identity', printSteps = False, printHistory = True):
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


#Max iters since there is no gaurentee that the points will converge
def kmeans(points, k, cutoff, pointType, maxIters = 100, toPrint = False):
    #Get k randomly chosen initial centroids
    initialCentroids = random.sample(points, k)
    clusters = []
    #Create a singleton cluster for each centroid
    for p in initialCentroids:
        clusters.append(Cluster([p], pointType))
    numIters = 0
    biggestChange = cutoff
    #Iterate until change is smaller than cutoff
    while biggestChange >= cutoff and numIters < maxIters:
        #Create a list containing k empty lists
        newClusters = []
        for i in range(k):
            newClusters.append([])
        for p in points:
            #Find the centroid closest to p
            smallestDistance = p.distance(clusters[0].getCentroid())
            index = 0

            #This is finding which cluster that the point is closest to (shortest distance) and indexing the cluster so the point may be added
            for i in range(k):
                distance = p.distance(clusters[i].getCentroid())
                if distance < smallestDistance:
                    smallestDistance = distance
                    index = i
            #Add p to the list of points for the appropriate cluster
            newClusters[index].append(p)
        #Upate each cluster and record how much the centroid has changed
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
    if toPrint:
        print 'Number of iterations =', numIters, 'Max Diameter =', maxDist
    return clusters, maxDist

def test1(k = 2, cutoff = 0.0001, numTrials = 1, printSteps = False, printHistory = False):
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
            #Using the minimum length of the maximum length cluster to try and find the best clustering (smallest largest cluster).
            #This is done to choose the best clustering over a number of trials.
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

# test1(printHistory=True)

##test1(numTrials = 100)
##test1(numTrials = 100)

#US Counties example

#We have added the notion of a filter to the counties.
#Each filter supplies a weight (in this case 0 or 1) to a feature.
#Filternames is just a dictionary to make running tests easier.
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
                    ('Prcnt Female', '1'), ('Prcent HS Grad', '0'),
                    ('Prcnt College', '0'), ('Unemployed', '0'),
                    ('Prcent Below 18', '1'), ('Life Expect', '1'),
                    ('Farm Acres', '1'))
    gender = (('HomeVal', '0'), ('Income', '0'), ('Poverty', '0'),
                    ('Population', '0'), ('Pop Change', '0'),
                    ('Prcnt 65+', '0'), ('Below 18', '0'),
                    ('Prcnt Female', '1'), ('Prcent HS Grad', '0'),
                    ('Prcnt College', '0'), ('Unemployed', '0'),
                    ('Prcent Below 18', '0'), ('Life Expect', '0'),
                    ('Farm Acres', '0'))
    income = (('HomeVal', '0'), ('Income', '1'), ('Poverty', '0'),
                    ('Population', '0'), ('Pop Change', '0'),
                    ('Prcnt 65+', '0'), ('Below 18', '0'),
                    ('Prcnt Female', '0'), ('Prcent HS Grad', '0'),
                    ('Prcnt College', '0'), ('Unemployed', '0'),
                    ('Prcent Below 18', '0'), ('Life Expect', '0'),
                    ('Farm Acres', '0'))
    allFeatures = (('HomeVal', '1'), ('Income', '1'), ('Poverty', '1'),
                    ('Population', '1'), ('Pop Change', '1'),
                    ('Prcnt 65+', '1'), ('Below 18', '1'),
                    ('Prcnt Female', '1'), ('Prcent HS Grad', '1'),
                    ('Prcnt College', '1'), ('Unemployed', '1'),
                    ('Prcent Below 18', '1'), ('Life Expect', '1'),
                    ('Farm Acres', '1'))
    filterNames = {'all': allFeatures, 'education': education,
                   'noEducation': noEducation, 'income': income,
                   'wealthOnly': wealthOnly,'noWealth': noWealth,
                   'gender': gender}
    attrFilter = None
    #Override Point to construct subset of features

    #Need to remember to normalize features so one feature doesn't predominate the clustering.
    #If filter is None then we have to fit it up with the filter that we care about.
    def __init__(self, name, originalAttrs, normalizedAttrs = None, filterName = 'all'):
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
    dataFile.close()
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

def test(k = 50, cutoff = 0.01, numTrials = 2, myHome = 'MAMiddlesex',
         filterName = 'all', printPoints = False,
         printClusters = True):
    #Build the set of points
    County.attrFilter = None
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
            print 'Ave. income of home cluster =', round(getAveIncome(c),0)

# print 'Cluster on education level only'
# test(k = 20, filterName = 'education', numTrials = 5, printClusters = False)
# pylab.title('Education Level')
##pylab.figure()
##print 'Cluster on gender only'
##test(k = 20, filterName = 'gender', numTrials = 1, printClusters = False)
##pylab.title('Gender')
# pylab.show()




#Reiteration of the take aways from machine learning:


    #1) Supervised learning: training set with labels
        #Try to infer relationship between the features and labels

    #2) Unsupervised learning: training set is unlabelled data
        #Try to infer relationships between points (how the point relate to one and other)
        #Try to fit curves to data

    #Be wary of overfitting: if training data is small may learning things thigns true for training that aren't true for other data sets

    #Features matter:
        #Normalized
        #Weighted (different importance)
        #Relevence to what you are trying to learn (domain knowledge)
















###Graph Theoretic Models

#Ex. bridge problem: If you were to traverse the 7 bridges exactly once than each node (except the first and last) must have an even number of edges
    #None of the nodes in this problem have an even number of edges, therefore you cannot do it
    #First example of taking the map and formulating it as a graph



#Ex. suppose you had a list of all the airline flights in the US, and also that to get from a > b > c costs the flight ab + bc

#Can ask different questions such as what is the least number of stops between cities, or the cheapest, least expensive with <= 2 stops
#These problems are visualized as graphs > graphs are used in situations where there are interesting relationships amongst the parts


#A graph is a set of nodes (vertices) that are connected by a set of edges (arcs)
    #If edges are unidirectional, called a digraph (directed graph)
    #Edges can have weights (for example in the airline situation number of miles between cities, or perhaps cost)

    #World wide web is modelled in this manner (how often people go from one site to another will result in a weighted directed graph)








#This gives an information content to the node, this class gives the potential to give more information to each node
class Node(object):
    def __init__(self, name):
        self.name = name
    def getName(self):
        return self.name
    def __str__(self):
        return self.name

#The most general form of the  an edge, has all the properties one may need
class Edge(object):
    def __init__(self, src, dest, weight = 0):
        self.src = src
        self.dest = dest
        self.weight = weight
    def getSource(self):
        return self.src
    def getDestination(self):
        return self.dest
    def getWeight(self):
        return self.weight
    def __str__(self):
        return str(self.src) + '->' + str(self.dest)

class Digraph(object):
    def __init__(self):
        self.nodes = set([])
        self.edges = {}
    def addNode(self, node):
        if node.getName() in self.nodes:
            raise ValueError('Duplicate node')
        else:
            self.nodes.add(node)
            self.edges[node] = []
    def addEdge(self, edge):
        src = edge.getSource()
        dest = edge.getDestination()
        if not(src in self.nodes and dest in self.nodes):
            raise ValueError('Node not in graph')
        self.edges[src].append(dest)
    def childrenOf(self, node):
        return self.edges[node]
    def hasNode(self, node):
        return node in self.nodes
    def __str__(self):
        res = ''
        for k in self.edges:
            for d in self.edges[k]:
                res = res + str(k) + '->' + str(d) + '\n'
        return res[:-1]

#Graph is a subclass of digraphs: relation of graphs to digraphs is that digraphs are more generalized.
#Since graphs are more specialized they must be lower in the hierarchy (graph is a special form of digraph).
    #Graph is more specialized because it is not unidirectional, can get from a > b and b > a along the same edge.
    #Anything you can do with a digraph you can do with a graph, but there are thigns you can do with graphs you cannot do with digraphs.
class Graph(Digraph):
    def addEdge(self, edge):
        Digraph.addEdge(self, edge)
        rev = Edge(edge.getDestination(), edge.getSource())
        Digraph.addEdge(self, rev)




    #1) Adjacency matrix:
        #If you have N nodes: you have NxN matrix
            #In the case of weighted digraph, each entry gives weight connecting nodes on the edges.
            #In the case of graph, entry gives true or false pertaining to if you can go between two nodes.

        #There may be multiple pathways between nodes: Each element of the matrix may in itself be more complicated (multiple edges connected two nodes)

    #2) Adjacency list:
        #For every node you list all of the edges emanating from that node

#Adjacency matrix is often better when connections are dense (everything is connected to everything else).
#Alternatively, if the connections are sparse an adjacency matrix is very wasteful (most entries will be empty in this case).

#In the above implementation we are using an adjacency list, as seen in the addNode function which shows the self.edges dict containing empty lists for each node.
#Alternatively this can also be seen by the childrenOf function that gives all the edges of a particular node.
