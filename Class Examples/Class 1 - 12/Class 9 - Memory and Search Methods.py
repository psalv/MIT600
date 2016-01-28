__author__ = 'paulsalvatore57'

        #9 - Memory and Search Methods



#An int will always occupy the same amount of space

#Let's assume an int occupies 4 units of memory
#What is the location-in memory-of L[i]?
    #Start + 4*i
#Correctness of this method depends upon each element of the list being of the same size, but that's not how lists work in python
    #in many languages lists are homogeneous

#Linked list: every element of a list is: <pointer to the next element, value>, end of the list will have None
    #to access the nth element of the list, you must go through n steps (O(n))
    #doesn't help us when doing binary search, changes order O(log(n)) >>> O(n)

#Python uses INDIRECTION; uses list of objects of the same size >>> objects are pointers (seperated in space values and pointers)
    #can use the same trick as first stated (if a each pointer is 4 units long, ith element is 4*i)
    #this method is used in all object oriented programing languages

#Binary search has an assumption: the list is sorted >>> how did it get sorted?
    #1) Sort L              >>> O(?)
    #2) Binary search       >>> O(log(len(L)))
    #OR Iterative search    >>> O(L)

    #is O(?) + O(logL) < O(L) >>> if not it doesn't make sense to sort it first
        #we cannot do this, no organise sorts a list in sublinear time

#AMORTIZED complexity: if we sort the list once, and search it many times
    #the cost of the sort can be allocated to each search

    #If we plan to perform k searches, is O(sort(L)) + k*(log(len(L)) < K*O(L)
        #depends on complexity of sorting, and how big k is




# def selSort(L):`
#     """Assumes that L is a list of elements that can be compared using >.
#        Sorts L in ascending order"""
#     for i in range(len(L) - 1):
#         #Invariant: the list L[:i] is sorted
#         minIndx = i
#         minVal = L[i]
#         j = i + 1
#         while j < len(L):
#             if minVal > L[j]:
#                 minIndx = j
#                 minVal = L[j]
#             j += 1
#         temp = L[i]
#         L[i] = L[minIndx]
#         L[minIndx] = temp

#depends upon establishing an maintaining an INVARIANT (invariantly true)
#in this case we will have a pointer in the list, dividing the list into a prefix and suffix
    #invariant maintained is that prefix is always sorted
    #start prefix empty, and each step increases the prefix size by one element, decrease size of suffix by one element
    #finished when the prefix contains all of the elements
#because we are maintaining the invariant throughout, we know the list is sorted

    #4, 3, 2 >>> 2 is smallest, so gets put in the front
    #2, 4, 3 >>> now only need to look in suffix, find that 3 is smallest
    #2, 3, 4 >>> suffix of 1 now, gets added to the end, list has been sorted

# ex1 = [2, 4, 69, 1, 69, 3736, 21, 64, 0, -1, 42]
# selSort(ex1)

#complexity O(n^2),
#each iteration looks at every element in the suffix, because it is ((n) + (n-1) + (n-2) + (n-i)) >>> n added to itself n times, or n*n






#DIVIDE AND CONQUER:
# 1) Choose a threshold size (n0), which will be the smallest problem
# 2) How many instances at each division; how many are we dividing the problem into?
# 3) Need an algorithm to combine the subsolutions


#Given two sorted lists, you can merge them quickly:
# L1 = [1, 5, 12, 18, 19, 20]
# L2 = [2, 3, 4, 17]

#Start by comparing first element of one list to the first element of the other list
#First look at 1 and 2, then 5 and 2, then 5 an 3, etc., moving up the lists.
#Number of copies O(n), where n represent len(list) >>> can do everything in linear time

#Takes original lists, break them up in to lists of length 1 (all trivially sorted)
#Pairs are merged, now have sorted lists of length 2, and this continues until two list are merged each 1/2 length of original list
#How many times will merge be called?
    #O(log n) where n represent len(L)

#Therefore if we call the merge O(log n) times, and it takes O(n) per merge, then the complexity is:
    #O(n log n)


def merge(left, right, lt):
    """Assumes left and right are sorted lists.
     lt defines an ordering on the elements of the lists.
     Returns a new sorted(by lt) list containing the same elements
     as (left + right) would contain."""
    result = []
    i, j = 0, 0
    while i < len(left) and j < len(right):
        if lt(left[i], right[j]):                       #if this is true, so what lt returned (which side is lower) will determine what is appended
            # print left[i], 'left', right[i], 'right'
            result.append(left[i])
            i += 1
        else:                                           #if it returned false, we  know the right is lower than the left
            result.append(right[j])
            # print 'test'
            j += 1
    while (i < len(left)):
        result.append(left[i])
        i += 1
        # print i
    while (j < len(right)):
        result.append(right[j])
        j += 1
    # print "qqqqq"
    return result


def sort(L, lt = lambda x, y: x < y):                        #used lambda to dynamically build a fxn (can sort based on different criteria) >>> function as an argument
    """Returns a new sorted list containing the same elements as L"""
    if len(L) < 2:
        return L[:]     #returns a copy of L
    else:
        middle = int(len(L) / 2)
        left = sort(L[:middle], lt)                     #this function just splits the list into single elements
        right = sort(L[middle:], lt)                    #calls merge to actaully merge the elements, does so by calling the fxn assigned to lt
        # print left, right
        # print 'about to merge', left, 'and', right
        return merge(left, right, lt)

L = [35, 4, 5, 29, 17, 58, 0]
newL = sort(L)
print 'Sorted list =', newL
# L = [1.0, 2.25, 24.5, 12.0, 2.0, 23.0, 19.125, 1.0]
# newL = sort(L, float.__gt__)                                  #list of different kinds can be sorted >>> less than = __lt__; greater than = __gt__
# print 'Sorted list =', newL





def lastNameFirstName(name1, name2):
    import string
    name1 = string.split(name1, ' ')
    name2 = string.split(name2, ' ')       #splits into list where L[0] = first name, and L[10 = last name
    print '1', name1
    print '2', name2
    if name1[1] != name2[1]:                #if the last names aren't the same, returns the last names
        return name1[1] < name2[1]              #this is an expression that will be returned to the fxn
    else:
        return name1[0] < name2[0]          #else will return the first names (next criteria for sorting)
#the < feature is used in this situation to test for alphebeticity
#F# or instance: 'abc' < 'edf' = True


# def firstNameLastName(name1, name2):
#     import string
#     name1 = string.split(name1, ' ')
#     name2 = string.split(name2, ' ')
#     if name1[0] != name2[0]:
#         return name1[0] < name2[0]
#     else:
#         return name1[1] < name2[1]


# L = ['John Guttag', 'Tom Brady', 'Chancellor Grimson', 'Gisele Brady',\
#      'Big Julie']
# newL = sort(L, lastNameFirstName)
# print 'Sorted list =', newL
# newL = sort(L, firstNameLastName)
# print 'Sorted list =', newL