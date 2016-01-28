__author__ = 'paulsalvatore57'


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

#Therefore if we call the merge O(log n), and it takes O(n) per merge, then the complexity is:
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
            print left[i], 'left', right[i], 'right'
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









def sort(L, lt = lambda x, y: x < y):                   #used lambda to dynamically build a fxn (can sort based on different criteria) >>> function as an argument
    """Returns a new sorted list containing the same elements as L"""
    if len(L) < 2:
        return L[:]     #returns a copy of L
    else:
        middle = int(len(L) / 2)
        left = sort(L[:middle], lt)                     #this function just splits the list into single elements >>> calls sort recursively to break down to length 1
        right = sort(L[middle:], lt)                    #calls merge to actually merge the elements, does so by calling the fxn assigned to lt
        print left, right
        print 'about to merge', left, 'and', right
        return merge(left, right, lt)

# L = [35, 4, 5, 29, 17, 58, 0]
# newL = sort(L)
# print 'Sorted list =', newL
L = [1.0, 2.25, 24.5, 12.0, 2.0, 23.0, 19.125, 1.0]
newL = sort(L, float.__gt__)                                  #list of different kinds can be sorted >>> less than = __lt__; greater than = __gt__
print 'Sorted list =', newL








#This system relies on the list that go into merge already being sorted.
#The recursive call to make the lists of length 1 is to ensure that they are trivially sorted.
#The merge function than uses the lengths of the lists to establish what has been added to the new, sorted list.
#This is accomplished by iterative motion dependent on a lambda factor (less than or greater than).
#Having the lambda factor allows for dynamic programming and to quickly change comparators.
