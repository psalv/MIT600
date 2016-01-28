
#THIS ASSIGNMENT WAS DONE INCORRECTLY

#What I should have done was clustered the training set, taken the clusters and gotten the positions of all of the centroids.
#From this point I would find which centroid points in the holdout set were closest to, and they would be assigned to that cluster.





#Code shared across examples
import random, string, copy, math, pickle
import matplotlib.pylab as pylab

class Point(object):
    def __init__(self, name, originalAttrs, normalizedAttrs = None):
        """normalizedAttrs and originalAttrs are both arrays"""
        self.name = name
        self.unNormalized = originalAttrs
        self.attrs = normalizedAttrs
    def dimensionality(self):
        return len(self.attrs)
    def getAttrs(self):
        return self.attrs
    def getOriginalAttrs(self):
        return self.unNormalized
    def distance(self, other):
        #Euclidean distance metric
        difference = self.attrs - other.attrs
        return sum(difference * difference) ** 0.5
    def getName(self):
        return self.name
    def toStr(self):
        return self.name + str(self.attrs)
    def __str__(self):
        return self.name

class County(Point):
    weights = pylab.array([1.0] * 14)
    weights[2] = 0
    # Override Point.distance to use County.weights to decide the
    # significance of each dimension
    def distance(self, other):
        difference = self.getAttrs() - other.getAttrs()
        return sum(County.weights * difference * difference) ** 0.5
    
class Cluster(object):
    def __init__(self, points, pointType):
        self.points = points
        self.pointType = pointType
        self.centroid = self.computeCentroid()
    def getCentroid(self):
        return self.centroid
    def computeCentroid(self):
        dim = self.points[0].dimensionality()
        totVals = pylab.array([0.0]*dim)
        for p in self.points:
            totVals += p.getAttrs()
        meanPoint = self.pointType('mean',
                                   totVals/float(len(self.points)),
                                   totVals/float(len(self.points)))
        return meanPoint
    def update(self, points):
        oldCentroid = self.centroid
        self.points = points
        if len(points) > 0:
            self.centroid = self.computeCentroid()
            return oldCentroid.distance(self.centroid)
        else:
            return 0.0
    def getPoints(self):
        return self.points
    def contains(self, name):
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
        result = ''
        for p in self.points:
            result = result + str(p) + ', '
        return result[:-2]
        

    
def kmeans(points, k, cutoff, pointType, minIters = 3, maxIters = 100, toPrint = False):
    """ Returns (Cluster list, max dist of any point to its cluster) """
    #Uses random initial centroids
    initialCentroids = random.sample(points,k)
    clusters = []
    for p in initialCentroids:
        clusters.append(Cluster([p], pointType))
    numIters = 0
    biggestChange = cutoff
    while (biggestChange >= cutoff and numIters < maxIters) or numIters < minIters:
        print "Starting iteration " + str(numIters)
        newClusters = []
        for c in clusters:
            newClusters.append([])
        for p in points:
            smallestDistance = p.distance(clusters[0].getCentroid())
            index = 0
            for i in range(len(clusters)):
                distance = p.distance(clusters[i].getCentroid())
                if distance < smallestDistance:
                    smallestDistance = distance
                    index = i
            newClusters[index].append(p)
        biggestChange = 0.0
        for i in range(len(clusters)):
            change = clusters[i].update(newClusters[i])
            #print "Cluster " + str(i) + ": " + str(len(clusters[i].points))
            biggestChange = max(biggestChange, change)
        numIters += 1
        if toPrint:
            print 'Iteration count =', numIters
    maxDist = 0.0
    for c in clusters:
        for p in c.getPoints():
            if p.distance(c.getCentroid()) > maxDist:
                maxDist = p.distance(c.getCentroid())
    print 'Total Number of iterations =', numIters, 'Max Diameter =', maxDist
    print biggestChange
    return clusters, maxDist

#US Counties example
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
    
def buildCountyPoints(fName):
    """
    Given an input filename, reads County values from the file and returns
    them all in a list.
    """
    nameList, featureList, maxVals = readCountyData(fName)
    points = []
    for i in range(len(nameList)):
        originalAttrs = pylab.array(featureList[i])
        normalizedAttrs = originalAttrs/pylab.array(maxVals)
        points.append(County(nameList[i], originalAttrs, normalizedAttrs))
    return points

def randomPartition(l, p):
    """
    Splits the input list into two partitions, where each element of l is
    in the first partition with probability p and the second one with
    probability (1.0 - p).
    
    l: The list to split
    p: The probability that an element of l will be in the first partition
    
    Returns: a tuple of lists, containing the elements of the first and
    second partitions.
    """
    l1 = []
    l2 = []
    for x in l:
        if random.uniform(0, 1.0) < p:
            l1.append(x)
        else:
            l2.append(x)
    return (l1,l2)

def getAveIncome(cluster):
    """
    Given a Cluster object, finds the average income field over the members
    of that cluster.
    
    cluster: the Cluster object to check
    
    Returns: a float representing the computed average income value
    """
    tot = 0.0
    numElems = 0
    for c in cluster.getPoints():
        tot += c.getOriginalAttrs()[1]

    return float(tot) / len(cluster.getPoints())




def test(points, k = 200, cutoff = 0.1):
    """
    A sample function to show you how to do a simple kmeans run and graph
    the results.
    """
    incomes = []
    print ''
    clusters, maxSmallest = kmeans(points, k, cutoff, County)

    for i in range(len(clusters)):
        if len(clusters[i].points) == 0: continue
        incomes.append(getAveIncome(clusters[i]))

    pylab.hist(incomes)
    pylab.xlabel('Ave. Income')
    pylab.ylabel('Number of Clusters')
    pylab.show()

        
points = buildCountyPoints('counties.txt')
# random.seed(123)
testPoints = random.sample(points, len(points)/10)

part_points = randomPartition(points, 0.8)
# print len(part_points[0])
# print len(part_points[1])





#WHAT I NEED TO DO (finished):
 # Will perform kmeans clustering on given points (partitioned to 80% (training) 20% (holdout)) over a range of 25 <= k <= 150.
 # After each kmeans clustering step I must extract the value of each point from it's centroid.
 # I will then have a list of 126 elements (for each k value) and each element will contain all of the distances from each point to it's respective centroid.

 # From this list I will calculate total error:

 #    Total error is calculated by taking: (sum (distance from points to centroid **2)) / number of points.

 # I will pickle this information such that the pickle will be a dump of 126 elements each representing the total error from their respective k values.
 # This will ensure that I do not need to repeat the lengthy process of calculating total error for each k value.





def find_save_error(points, name):
    """
    Saves a file containing 126 elements, representing kmeans clustering with 25 < k < 150.
    Each element contains a list of the distance from every point to it's respective centroid.
    """
    k = 25
    a_distances = []
    error = []
    while k <= 150:
        c_distance = []
        print k
        clusters = kmeans(points, k, 0.1, County)[0]
        k += 1
        for cluster in clusters:
            cl_points = cluster.getPoints()
            for point in cl_points:
                c_distance.append(point.distance(cluster.getCentroid()))
        a_distances.append(c_distance)
    for i in a_distances:
        er = 0
        for j in i:
            er += j**2
        er = er/len(i)
        error.append(er)
    pickle.dump(error, open(name, 'wb'))


# find_save_error(part_points[1], 'Holdout Set')
# find_save_error(part_points[0], 'Training Set')



# I implemented this differently using the find_save_error function to first compute all of the error values and pickle them into files,
# Therefore the grapgRemovedErr function does not take an arguments in my implementation.

def graphRemovedErr():
    """
    Should produce graphs of the error in training and holdout point sets, and
    the ratio of the error of the points, after clustering for the given values of k.
    For details see Problem 1.
    """

    holdout = pickle.load(open('Holdout Set'))
    training = pickle.load(open('Training Set'))
    x_lab = []
    for i in range(25, 151):
        x_lab.append(i)
    # pylab.plot(x_lab, holdout, label = 'Holdout')
    pylab.plot(x_lab, training, label = 'Training')
    pylab.title('Q3 Graph of Error')
    pylab.xlabel('K value')
    pylab.ylabel('Total Error')
    pylab.legend(loc = 'best')
    pylab.savefig('Q3 Total Error')
    pylab.show()

# graphRemovedErr()









#PROBLEM 2

#Pick a specific county and run the k means clustering three times
#Observe which cluster the county ends up in

#I Will pick TXHamilton

def find_Ham(points):
    clusters = []
    for i in range(3):
        cls = kmeans(points, 50, 0.1, County)[0]
        for cl in cls:
            for cnt in cl.getPoints():
                if str(cnt) == 'TXHamilton':
                    clusters.append(cl)
    results = []
    inc = []
    for cl in clusters:
        inc.append(getAveIncome(cl))
        ans = []
        cnt = cl.getPoints()
        for i in cnt:
            ans.append(str(i))
        results.append(ans)
    return results, inc

# print find_Ham(points)

#With a cutoff of 0.1 the clusters are fairly different, this is a high cutoff value therefore it is unlikely that there has been sufficient convergence.
#When I set the cutoff much lower, to 0.0001, the clustering is better (based on similarity of average incomes), however there are still discrepancies.


#PROBLEM 3

#This code will be ran while poverty is turned off: weight[3] = 0 in the County class.
#This code will cluster the training set, find the average poverty per cluster. I will then graph the difference in poverty computed the same as total error was.


def getAvePoverty(cluster):
    tot = 0.0
    numElems = 0
    for c in cluster.getPoints():
        tot += c.getOriginalAttrs()[3]
    return float(tot) / len(cluster.getPoints())


def find_save_poverty(points, name):

    k = 25
    a_pov = []
    total_pov = []
    while k <= 150:
        ppoverty = []
        print k
        clusters = kmeans(points, k, 0.1, County)[0]
        k += 1
        for cluster in clusters:
            cl_points = cluster.getPoints()
            for point in cl_points:
                # print 'Place: ', str(point), '\nPoverty: ', point.getOriginalAttrs()[2], '\n'
                ppoverty.append(getAvePoverty(cluster) - point.getOriginalAttrs()[2])
        a_pov.append(ppoverty)
    for i in a_pov:
        po = 0
        for j in i:
            po += j**2
        po = po/len(i)
        total_pov.append(po)
    pickle.dump(total_pov, open(name, 'wb'))

find_save_poverty(part_points[1], 'Holdout Set Poverty')
# find_save_poverty(part_points[0], 'Training Set Poverty')


def graphPoverty():

    holdout = pickle.load(open('Holdout Set Poverty'))
    # training = pickle.load(open('Training Set Poverty'))
    x_lab = []
    for i in range(25, 151):
        x_lab.append(i)
    pylab.plot(x_lab, holdout, label = 'Holdout')
    # pylab.plot(x_lab, training, label = 'Training')
    pylab.title('Q3 Graph of Poverty')
    pylab.xlabel('K value')
    pylab.ylabel('Total Poverty')
    pylab.legend(loc = 'best')
    pylab.savefig('Q3 Zero Weight Poverty')
    pylab.show()

graphPoverty()





def graphPredictionErr(points, dimension, kvals = [25, 50, 75, 100, 125, 150], cutoff = 0.1):
    """
    Given input points and a dimension to predict, should cluster on the
    appropriate values of k and graph the error in the resulting predictions,
    as described in Problem 3.
    """

	# Your Code Here
    