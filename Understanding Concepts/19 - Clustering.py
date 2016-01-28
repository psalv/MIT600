__author__ = 'paulsalvatore57'


#Unsupervised Learning: have data but no labels; generally learning about regularities of the data (discover structure of data) > Optimization problem
    #Dominate form is clustering: organizing data into groups with similar features (which features are we interested in?)

    #Features we want:
        #Low intra-cluster dissimilarity (in same cluster are similar)
        #High inter-cluster dissimilarity (different clusters are very different)


    #Variance of cluster c = sum ((mean(c) - x)**2) >>> how far is each point from the mean, use it to find similarity within and between clusters


    #We can't just optimize for the two features above; every element will be put into it's own cluster of length 1
        #We need to add CONSTRAINTS to prevent a trivial answer

            #Constraints:
                #Maximum number of clusters
                #Maximum distance between clusters

    #People often use greedy algorithms: k-means, and hierarchical clustering






#Hierarchical clustering:
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