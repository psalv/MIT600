__author__ = 'paulsalvatore57'


            # Tutorial 9


# Graphs are defined as having vertices and edges; G = (v, E).
    # The vertices (nodes) represent the points and the edges (arcs) the relationship between the points.

# Directed graphs have unidirectional edges, undirected graphs have bidirectional edges.

# A weighted graph will associate values with the edges.




# Recursive Depth First Search:

    # The idea is to grow your shortest path backwards, first randomly searching until you have found your end point.
    # At each point you find the shortest path to the end, therefore at the next step the shortest be one step added to the shortest path.


#Functions for graphing:
class Node(object):
    def __init__(self, name):
        self.name = name
    def getName(self):
        return self.name
    def __str__(self):
        return self.name
class Edge(object):
    def __init__(self, src, dest):
        self.src = src
        self.dest = dest
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
class Graph(Digraph):
    def addEdge(self, edge):
        Digraph.addEdge(self, edge)
        rev = Edge(edge.getDestination(), edge.getSource())
        Digraph.addEdge(self, rev)


# Call this function with a graph object (specifying the type of graph) as well as a start and an end.
# The visited object will keep track of nodes that have already been visited to ensure that we do not get stuck in cycles.
def shortestPath(graph, start, end, toPrint = False, visited = []):

    #This first block is administrative, ensuring the nodes we are looking for are in the graph.
    #Also includes a debugging feature for he recursive call (since start should modify with each new call.
    global numCalls
    numCalls += 1
    if toPrint:
        print start, end
    if not (graph.hasNode(start) and graph.hasNode(end)):
        raise ValueError('Start or end not in graph.')

    #The path that we construct will just contain the start node as it's element.
    #If start == end then we are already at our goal, so we return the path.
    #Use string for comparison purposes, returns a string rather than a node object.
    path = [str(start)]
    if start == end:
        return path


    shortest = None
    for node in graph.childrenOf(start):
        if (str(node) not in visited): #avoid cycles
            visited = visited + [str(node)] #new list (add node so that we know it has been visited).
            newPath = shortestPath(graph, node, end, toPrint, visited)  #Only parameter changing is start node, and given the new list.

            #If nothing is returned than we continue since there is not a path.
            #However if it does return a path there are two checks:
                #1) Is there no current shortest path
                #2) Is the returned newPath shorter than the shortest path
            #If so than this path becomes the shortest path.
            if newPath == None:
                continue
            if (shortest == None or len(newPath) < len(shortest)):
                shortest = newPath

    #The above code will iterate over every possible path until the shortest path has been found.
    #At this point the shortest path (termed newPath) will be added on to the end of the path.
    #The path in every situation will be length 1 and just consist of the start position,
    #Therefore through successive rounds of recursion that shortest path will be built by adding on the starting position starting from the end point.
    if shortest != None:
        path = path + shortest
    else:
        path = None
    return path









# Breadth First Search:

    # Works with the reverse logic of DFS, building and maintaining a list of every possible path from the start.
    # BFS builds all partial paths rather than starting from the end goal and working backwards to find the shortest path.


    # Note on lambda: It is an anonymous function, often used in sorting since it can be used to give values to a function by extracting them.
    # Useful for situations wher eyou have elements without a defined value (you need a value by which to sort elements).
        # For instance the below fxn will square the input x
            # g = lambda x: x**2


def shortestPathBFS(graph, paths, goal, toPrint = False):
    """
    Paths is a list of partial path tuples of the form: ([path nodes], path length)
    """

    # This first piece of code will sort all of the paths that are given to this fxn by their length.
    # Thsi is achieved using the key fxn lambda, which will find and assign length for each path in paths.
    (NODELIST, LENGTH) = (0, 1)
    paths = sorted(paths, key=lambda path: path[LENGTH])

    if toPrint:
        print "Path so far:"
        for path in paths:
            nodeNames = [node.getName() for node in path[NODELIST]]
            print (nodeNames, path[LENGTH])

    newPaths = []
    examiningPath = paths.pop(0)

    #For every child in the last length of this path we want to see if it is a goal.
    #If the path has no children than the for loop does not execute and the path will not be added to newPaths.
    #In this scenario the first path to find with goal will by definition be the shortest so it will be returned as soon as it is found.
        #The reason that we can use the pop function is because when we call shortestpathBFS again the list gets sorted again,
        #This means that the shortest path will be first and that is the one we want to examine, meanwhile newPaths to examine will be added to paths each cycle.
    for node in graph.childrenOf(examiningPath[NODELIST][-1]):
        if node == goal:
            shortest = examiningPath[NODELIST] + [node]
            return [node.getName() for node in shortest]

        #If the child is not the goal, then what we want to do is append a new path with the child and add that to the list of new paths (including length).
        #Since we are iterating over every child of the final node, we will get a list of all possible direction that can be taken.
        if node not in examiningPath[NODELIST]:
            newPaths.append((examiningPath[NODELIST] + [node], examiningPath[LENGTH] + 1))

    paths.extend(newPaths)
    return shortestPathBFS(graph, paths, goal)