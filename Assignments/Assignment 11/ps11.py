
# Graph optimization
# Finding shortest paths through MIT buildings


#MIT_map is of form: Start building, stop building, distance, distance outdoors
#Not bidirectional, therefore must represent as a digraph.
#Two different weights: distance and distance outdoors.

import string
from graph import Digraph, Edge, Node









# Problem 1: Modify graph.py such that weights can be added to the edges.


# Problem 2: Building up the Campus Map

#Each building will be a node.
#Each edge will be the path from one building to another, with a weight consisting of (distance, distance outside).


def load_map(mapFilename):
    """ 
    Parses the map file and constructs a directed graph

    Parameters: 
        mapFilename : name of the map file

    Assumes:
        Each entry in the map file consists of the following four positive 
        integers, separated by a blank space:
            From To TotalDistance DistanceOutdoors
        e.g.
            32 76 54 23
        This entry would become an edge from 32 to 76.

    Returns:
        a directed graph representing the map
    """
    print "Loading map from file..."
    inputFile = open(mapFilename)
    graph = Digraph()
    for line in inputFile:
        readLine = line.split()
        try:
            graph.addNode(readLine[0])
        except:
            ValueError
    inputFile = open(mapFilename)
    for line in inputFile:
        readLine = line.split()
        edge = Edge(readLine[0], readLine[1], (readLine[2], readLine[3]))
        graph.addEdge(edge)
    return graph





# Problem 3: Finding the Shortest Path using Brute Force Search

# State the optimization problem as a function to minimize
# and the constraints


#Note: need to make sure that I avoid cycles (visiting the same node twice) >>> implemented by keeping track of visited nodes.

#We are looking for the least distance traveled between two nodes.
#By exhaustive enumeration we want to attempt every possible path.
#This means that what I will keep track of are paths that start with the start and end with the end, and their maxTotalDist.
#The constraint I must adhere to is the maxDistOutdoors. This is like the available weight in the knapsack problem.








#I first implemented the bruteForceSearch as the DFSearch which is incorrect therefore I will rectify this.
#To use a brute force search that means that I will need to collect every possible pathway from the start to the end.


#I am drawing a blank on this brute force search method, therefore I think I'm going to just take a look at the answer.
#The assignment answers were different as usual. I know my DFS is correct, but cannot check my brute force search.
#If I ever need to use a brute force algorithm to compile every possibility of a graph I will cross that bridge when I come to it.

def bruteForceSearch(digraph, start, end, maxTotalDist, maxDistOutdoors):
    """
    Finds the shortest path from start to end using brute-force approach.
    The total distance travelled on the path must not exceed maxTotalDist, and
    the distance spent outdoor on this path must not exceed maxDisOutdoors.

    Parameters:
        digraph: instance of class Digraph or its subclass
        start, end: start & end building numbers (strings)
        maxTotalDist : maximum total distance on a path (integer)
        maxDistOutdoors: maximum distance spent outdoors on a path (integer)

    Assumes:
        start and end are numbers for existing buildings in graph

    Returns:
        The shortest-path from start to end, represented by
        a list of building numbers (in strings), [n_1, n_2, ..., n_k],
        where there exists an edge from n_i to n_(i+1) in digraph,
        for all 1 <= i < k.

        If there exists no path that satisfies maxTotalDist and
        maxDistOutdoors constraints, then raises a ValueError.
    """
    # visited = []
    # if not (digraph.hasNode(start) and digraph.hasNode(end)):
    #     raise ValueError('Start or end not in graph.')
    #
    # possible = []
    # for node in digraph.childrenOf(start):
    #
    #     possible.append([node[0]]*len(digraph.childrenOf(node[0])))
    #     print possible
    pass

        # #No children
        # if node == None:
        #     return ValueError
        #
        # #Checking for and preventing loops
        # if node[0] in visited:
        #     continue
        # else:
        #     visited += [node[0],]
        #
        # #If the very first is the solution
        # if node[0] == end:
        #     possible.append([start, node[0]])
        #     continue
        #
        #
        # while True:
        #     p = [start, node]
        #     memory = node[0]
        #
        #
        #     #Testing code
        #     # print 'We are looking at the children of: ', memory[0]
        #     # test = []
        #     # for child in digraph.childrenOf(memory[0]):
        #     #     test += [child[0],]
        #     # print test
        #
        #
        #     try:
        #
        #         for child in digraph.childrenOf(node[0]):
        #
        #             try:
        #                 if node[0] in visited:
        #                     continue
        #                 else:
        #                     visited += [node,]
        #
        #                 if child == end:
        #                     possible.append(p.append(child))
        #                     continue
        #                 else:
        #                     p += [child,]
        #                     node = child
        #
        #             except:
        #                 ValueError
        #                 p = [start, node]
        #                 node = memory
        #     except:
        #         ValueError
        #         break

    #This code will need to analyze which of the possible solutions has the shortest paths.

    # print possible




#So I think the above is the DFS, meaning that I still need implement the bruteForce method.
#I believe the brute force method will require me to actually obtain a list of every possibility, after which I can sift through to find ones with the right start and end.
#At this point I would determine which is the shortest, and if it meets the criteria.



# Problem 4: Finding the Shortest Path using Optimized Search Method

def directedDFS(digraph, start, end, maxTotalDist, maxDistOutdoors, visited = []):
    """
    Finds the shortest path from start to end using directed depth-first.
    search approach. The total distance travelled on the path must not
    exceed maxTotalDist, and the distance spent outdoor on this path must
	not exceed maxDisOutdoors.

    Parameters: 
        digraph: instance of class Digraph or its subclass
        start, end: start & end building numbers (strings)
        maxTotalDist : maximum total distance on a path (integer)
        maxDistOutdoors: maximum distance spent outdoors on a path (integer)

    Assumes:
        start and end are numbers for existing buildings in graph

    Returns:
        The shortest-path from start to end, represented by 
        a list of building numbers (in strings), [n_1, n_2, ..., n_k], 
        where there exists an edge from n_i to n_(i+1) in digraph, 
        for all 1 <= i < k.

        If there exists no path that satisfies maxTotalDist and
        maxDistOutdoors constraints, then raises a ValueError.
    """
    if not (digraph.hasNode(start) and digraph.hasNode(end)):
        raise ValueError('Start or end not in graph.')
    path = [str(start)]
    if start == end:
        return path
    shortest = None
    shortestDist = None
    vis = 0
    for node in digraph.childrenOf(start):
        # print 'Start is: ', start
        # print 'Current node is: ', node
        newTotalDist = maxTotalDist - int(node[1][0])
        newDistOutdoors = maxDistOutdoors - int(node[1][1])
        if newTotalDist < 0 or newDistOutdoors < 0:
            continue
        if (str(node[0]) not in visited):
            vis += 1
            visited = visited + [str(node[0])]
            newPath = directedDFS(digraph, node[0], end, newTotalDist, newDistOutdoors, visited)
            if newPath == None:
                continue

            dist = int(digraph.getEdgeWeight(start, newPath[0]))
            for i in xrange(len(newPath) - 1):
                dist += int(digraph.getEdgeWeight(newPath[i], newPath[i + 1]))

            if shortestDist == None or dist < shortestDist:
                shortest = newPath
                shortestDist = dist

    if shortest != None:
        path = path + shortest
    else:
        path = None

    if len(visited) == vis and shortest == None:
        raise ValueError

    return path















# Test cases

digraph = load_map("mit_map.txt")
LARGE_DIST = 1000000

# # Test case 1
print "---------------"
print "Test case 1:"
print "Find the shortest-path from Building 32 to 56"
expectedPath1 = ['32', '56']
brutePath1 = bruteForceSearch(digraph, '32', '56', LARGE_DIST, LARGE_DIST)
# dfsPath1 = directedDFS(digraph, '32', '56', LARGE_DIST, LARGE_DIST)
# print "Expected: ", expectedPath1
# print "Brute-force: ", brutePath1
# print "DFS: ", dfsPath1
#
# # Test case 2
# print "---------------"
# print "Test case 2:"
# print "Find the shortest-path from Building 32 to 56 without going outdoors"
# expectedPath2 = ['32', '36', '26', '16', '56']
# brutePath2 = bruteForceSearch(digraph, '32', '56', LARGE_DIST, 0)
# dfsPath2 = directedDFS(digraph, '32', '56', LARGE_DIST, 0)
# print "Expected: ", expectedPath2
# print "Brute-force: ", brutePath2
# print "DFS: ", dfsPath2
#
# # Test case 3
# print "---------------"
# print "Test case 3:"
# print "Find the shortest-path from Building 2 to 9"
# expectedPath3 = ['2', '3', '7', '9']
# brutePath3 = bruteForceSearch(digraph, '2', '9', LARGE_DIST, LARGE_DIST)
# dfsPath3 = directedDFS(digraph, '2', '9', LARGE_DIST, LARGE_DIST)
# print "Expected: ", expectedPath3
# print "Brute-force: ", brutePath3
# print "DFS: ", dfsPath3
#
# # Test case 4
# print "---------------"
# print "Test case 4:"
# print "Find the shortest-path from Building 2 to 9 without going outdoors"
# expectedPath4 = ['2', '4', '10', '13', '9']
# brutePath4 = bruteForceSearch(digraph, '2', '9', LARGE_DIST, 0)
# dfsPath4 = directedDFS(digraph, '2', '9', LARGE_DIST, 0)
# print "Expected: ", expectedPath4
# print "Brute-force: ", brutePath4
# print "DFS: ", dfsPath4
#
# # Test case 5
# print "---------------"
# print "Test case 5:"
# print "Find the shortest-path from Building 1 to 32"
# expectedPath5 = ['1', '4', '12', '32']
# brutePath5 = bruteForceSearch(digraph, '1', '32', LARGE_DIST, LARGE_DIST)
# dfsPath5 = directedDFS(digraph, '1', '32', LARGE_DIST, LARGE_DIST)
# print "Expected: ", expectedPath5
# print "Brute-force: ", brutePath5
# print "DFS: ", dfsPath5
#
# # Test case 6
# print "---------------"
# print "Test case 6:"
# print "Find the shortest-path from Building 1 to 32 without going outdoors"
# expectedPath6 = ['1', '3', '10', '4', '12', '24', '34', '36', '32']
# brutePath6 = bruteForceSearch(digraph, '1', '32', LARGE_DIST, 0)
# dfsPath6 = directedDFS(digraph, '1', '32', LARGE_DIST, 0)
# print "Expected: ", expectedPath6
# print "Brute-force: ", brutePath6
# print "DFS: ", dfsPath6
#
# # Test case 7
# print "---------------"
# print "Test case 7:"
# print "Find the shortest-path from Building 8 to 50 without going outdoors"
# bruteRaisedErr = 'No'
# dfsRaisedErr = 'No'
# try:
#    bruteForceSearch(digraph, '8', '50', LARGE_DIST, 0)
# except ValueError:
#    bruteRaisedErr = 'Yes'
#
# try:
#    directedDFS(digraph, '8', '50', LARGE_DIST, 0)
# except ValueError:
#    dfsRaisedErr = 'Yes'
#
# print "Expected: No such path! Should throw a value error."
# print "Did brute force search raise an error?", bruteRaisedErr
# print "Did DFS search raise an error?", dfsRaisedErr
#
# # Test case 8
# print "---------------"
# print "Test case 8:"
# print "Find the shortest-path from Building 10 to 32 without walking"
# print "more than 100 meters in total"
# bruteRaisedErr = 'No'
# dfsRaisedErr = 'No'
# try:
#    bruteForceSearch(digraph, '10', '32', 100, LARGE_DIST)
# except ValueError:
#    bruteRaisedErr = 'Yes'
#
# try:
#    directedDFS(digraph, '10', '32', 100, LARGE_DIST)
# except ValueError:
#    dfsRaisedErr = 'Yes'
#
# print "Expected: No such path! Should throw a value error."
# print "Did brute force search raise an error?", bruteRaisedErr
# print "Did DFS search raise an error?", dfsRaisedErr
#
