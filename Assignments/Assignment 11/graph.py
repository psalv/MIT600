
# A set of data structures to represent graphs


class Node(object):
   def __init__(self, name):
       self.name = str(name)
   def getName(self):
       return self.name
   def __str__(self):
       return self.name
   def __repr__(self):
      return self.name
   def __eq__(self, other):
      return self.name == other.name
   def __ne__(self, other):
      return not self.__eq__(other)

class Edge(object):
   def __init__(self, src, dest, weight):
       self.src = src
       self.dest = dest
       self.weight = weight  #tuple
   def getSource(self):
       return self.src
   def getDestination(self):
       return self.dest
   def getWeight(self):
       return self.weight
   def __str__(self):
       return str(self.src) + '->' + str(self.dest), 'Weight (total, outside): ' + str(self.weight)

class Digraph(object):
   """
   A directed graph
   """
   def __init__(self):
       self.nodes = set([])
       self.edges = {}
   def addNode(self, node):
       if node in self.nodes:
           raise ValueError('Duplicate node')
       else:
           self.nodes.add(node)
           self.edges[node] = []
   def addEdge(self, edge):
       src = edge.getSource()
       dest = edge.getDestination()
       weight = edge.getWeight()
       if not(src in self.nodes and dest in self.nodes):
           raise ValueError('Node not in graph')
       self.edges[src].append((dest, weight))
   def childrenOf(self, node):
       return self.edges[node]
   def hasNode(self, node):
       return node in self.nodes

   def getEdgeWeight(self, source, end):
       # print 'Looking for:', end
       for child in self.edges[source]:
           # print 'Child:', child[0]
           if child[0] == str(end):
               return child[1][0]

   def __str__(self):
       res = ''
       for k in self.edges:
           for d in self.edges[k]:
               res = res + str(k) + '->' + str(d[0]) + " Weight: " + str(d[1]) + '\n'
       return res[:-1]


