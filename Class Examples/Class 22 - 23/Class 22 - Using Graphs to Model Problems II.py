__author__ = 'paulsalvatore57'



                #22 - Using Graphs to Model Problems II



import random

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

#So what we have above is the tools to make a graph containing nodes connected by edges.
#The connections are stored in a dictionary (self.edges) that contains each node as a key, and the edges as elements of a list assigned to that key.

#To summarize: edges connected nodes are stored in dictionaries with nodes as keys, can add nodes or edges between nodes to this dictionary that logs connections.

def test1(kind):
    nodes = []
    for name in range(10):
        nodes.append(Node(str(name)))
    g = kind()
    for n in nodes:
        g.addNode(n)
    g.addEdge(Edge(nodes[0],nodes[1]))
    g.addEdge(Edge(nodes[1],nodes[2]))
    g.addEdge(Edge(nodes[2],nodes[3]))
    g.addEdge(Edge(nodes[3],nodes[4]))
    g.addEdge(Edge(nodes[3],nodes[5]))
    g.addEdge(Edge(nodes[0],nodes[2]))
    g.addEdge(Edge(nodes[1],nodes[1]))
    g.addEdge(Edge(nodes[1],nodes[0]))
    g.addEdge(Edge(nodes[4],nodes[0]))
    print 'The graph:'
    print g


# test1(Digraph)
# test1(Graph)


#Graph problems:

    #1) Shortest path: shortest sequence of edges connecting any two nodes
    #2) Shortest weighted path: want to find shortest sequence of weights (edges will have different weights so can have more edges but a lower weight)

        #Ex. Google maps, can use different types of weights (such as a time or distance).

    #3) Finding cliques: find a set of node such that there exists a path connecting each node in the set,
                            # Guarantees each member is connected by some amount of edges to all others in the clique (can get from any one to any other)

    #4) Minimum cut problem (Min-cut): Given a graph and given two sets of nodes,
                            # Want to fo find minimum number of edges such that if the edges are removed that the sets are disconnected
                            # I.e. that you cannot get from one set to another set







#Tuberculosis example:
     # Represents a relatively complicated example as a graph.
     # People that have been exposed to tuberculosis represent one type of node, ones that have tested positive represent another type.
     # The edges are weighted based on the type of exposure (close exposure such as family, mild exposure such as same office building).

     # A question for this graph would be to find the index patient (the one who started the outbreak).
        # Can be answered by having a node with TB and is connected to every other TB node

     # If no such node exists than it can be inferred that there is not a single source of disease in this community

     # In this specific example all of the people were found to be connected with the exception of a small node,
     # Upon further investigation they found an edge was missing so there was a single source of this outbreak.


    # A related graph theory problem would involve vaccinations: If you want to stop the spread of a disease but only have so many vaccines, who should ge them?
        # This is a min-cut problem. Take infected as one set of nodes, uninfected on the other and find the edges that need be cut for separation.




# Six degrees of separation problem:
    # He gave the example of Facebook, which has symmetric edges (although we could imagine an asymmetric model where my being your friend doesn't make you mine necessarily).
    # What is the shortest path from one person to another? This is information that can be sold by Facebook.




#The shortestPath function is recursive termed: Recursive Depth First Search (DFS) algorithm

#Imagine a graph of nodes. The algorithm starts at a particular start node.
#It first visits on child of the node, and explores every possible path. It then explores another child fo the source node and does the same.

#Recursion ends when start == end
#Recursion starts by choosing one child,
#Continues until it reaches a node with no children, it reaches the node you are looking for, or it reaches a node it has already seen (avoid loops)..



def shortestPath(graph, start, end, toPrint = False, visited = []):
    global numCalls
    numCalls += 1
    if toPrint: #for debugging
        print start, end
    if not (graph.hasNode(start) and graph.hasNode(end)):
        raise ValueError('Start or end not in graph.')
    path = [str(start)]
    if start == end:
        return path
    shortest = None
    for node in graph.childrenOf(start):
        if (str(node) not in visited): #avoid cycles
            visited = visited + [str(node)] #new list
            newPath = shortestPath(graph, node, end, toPrint, visited)
            if newPath == None:
                continue
            if (shortest == None or len(newPath) < len(shortest)):
                shortest = newPath
    if shortest != None:
        path = path + shortest
    else:
        path = None
    return path

def test2(kind, toPrint = False):
    nodes = []
    for name in range(10):
        nodes.append(Node(str(name)))
    g = kind()
    for n in nodes:
        g.addNode(n)
    g.addEdge(Edge(nodes[0],nodes[1]))
    g.addEdge(Edge(nodes[1],nodes[2]))
    g.addEdge(Edge(nodes[2],nodes[3]))
    g.addEdge(Edge(nodes[3],nodes[4]))
    g.addEdge(Edge(nodes[3],nodes[5]))
    g.addEdge(Edge(nodes[0],nodes[2]))
    g.addEdge(Edge(nodes[1],nodes[1]))
    g.addEdge(Edge(nodes[1],nodes[0]))
    g.addEdge(Edge(nodes[4],nodes[0]))
    print 'The graph:'
    print g
    shortest = shortestPath(g, nodes[0], nodes[4], toPrint)
    print 'The shortest path:'
    print shortest

# test2(Graph)
# test2(Digraph)

#Finds two different answers dependant on the type fo graph.
#A normal graph can get from 0 to 4 by one edge. A digraph takes longer, since its edges are unidirectional.





#bigTest generates edges at random to perform a test.

def bigTest1(kind, numNodes = 25, numEdges = 200):
    nodes = []
    for name in range(numNodes):
        nodes.append(Node(str(name)))
    g = kind()
    for n in nodes:
        g.addNode(n)
    for e in range(numEdges):
        src = nodes[random.choice(range(0, len(nodes)))]
        dest = nodes[random.choice(range(0, len(nodes)))]
        g.addEdge(Edge(src, dest))
    print g
    print shortestPath(g, nodes[0], nodes[4])

# bigTest1(Digraph)
#This worked but took a long time since it had to explore every possibility. It also found a short path since we have a high number of edges/node.
#This is an exponential order program.


# test2(Graph, toPrint = True)


#Since we are doing work that we have already done before when we look at the same path multiple times, we want a way to store pathways.
#This way, when we get to a node we can look up the shortest path that we have already found from that node to the end.

#This technique is called MEMOIZATION: remembering answers and looking them up rather than recalculating them (table look up).
#This is at the heart of dynamic programming.



#This program accounts for memoization.
#The lecture states that there is a bug in the code that won't work for all graphs.

def dpShortestPath(graph, start, end, visited = [], memo = {}):
    global numCalls
    numCalls += 1
    if not (graph.hasNode(start) and graph.hasNode(end)):
        raise ValueError('Start or end not in graph.')
    path = [str(start)]
    if start == end:
        return path
    shortest = None
    for node in graph.childrenOf(start):
        if (str(node) not in visited):
            visited = visited + [str(node)]
            try:
                newPath = memo[node, end]           #First question is do we already have the shortest path from the node to the end stored.
            except:
                newPath = dpShortestPath(graph, node, end, visited, memo)
            if newPath == None:
                continue
            if (shortest == None or len(newPath) < len(shortest)):
                shortest = newPath
                memo[node, end] = newPath
    if shortest != None:
        path = path + shortest
    else:
        path = None
    return path

def test3(kind):
    nodes = []
    for name in range(10):
        nodes.append(Node(str(name)))
    g = kind()
    for n in nodes:
        g.addNode(n)
    g.addEdge(Edge(nodes[0],nodes[1]))
    g.addEdge(Edge(nodes[1],nodes[2]))
    g.addEdge(Edge(nodes[2],nodes[3]))
    g.addEdge(Edge(nodes[3],nodes[4]))
    g.addEdge(Edge(nodes[3],nodes[5]))
    g.addEdge(Edge(nodes[0],nodes[2]))
    g.addEdge(Edge(nodes[1],nodes[1]))
    g.addEdge(Edge(nodes[1],nodes[0]))
    g.addEdge(Edge(nodes[4],nodes[0]))
    print 'The graph:'
    print g
    shortest = shortestPath(g, nodes[0], nodes[4])
    print 'The shortest path:'
    print shortest
    shortest = dpShortestPath(g, nodes[0], nodes[4])
    print 'The shortest path:'
    print shortest

# test3(Digraph)




def bigTest2(kind, numNodes = 25, numEdges = 200):
    global numCalls
    nodes = []
    for name in range(numNodes):
        nodes.append(Node(str(name)))
    g = kind()
    for n in nodes:
        g.addNode(n)
    for e in range(numEdges):
        src = nodes[random.choice(range(0, len(nodes)))]
        dest = nodes[random.choice(range(0, len(nodes)))]
        g.addEdge(Edge(src, dest))
    print g
    numCalls = 0
    # print shortestPath(g, nodes[0], nodes[4])
    # print 'Number of calls to shortest path =', numCalls
    numCalls = 0
    print dpShortestPath(g, nodes[0], nodes[4])
    print 'Number of calls to dp shortest path =', numCalls

bigTest2(Digraph)


# Dynamic programming is extremely important for providing solutions to optimization problems that at the surface level appear impractical (exponential).
# The ability to solve exponential problems very quickly is the appeal of dynamic programming.


# We can use dynamic programming on problems which meet the criteria:

    #1) Optimal substructure:
        # Can find a globally optimal solution by combining locally optimal solutions >>> This property tells us if finding the solution is possible.

    #2) Requires overlapping sub-problems:
        # Finding solution to the same subproblem multiple times >>> This property tells us how much faster we can find an answer