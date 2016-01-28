__author__ = 'paulsalvatore57'

        #LISTS AND THEIR ELEMENTS, SORTING AND RECURSION


#Tuples can contain lists, as well as other tuples:

# tupA = ("A", 2, "c", [2, 3])
# tupB = (tupA, "Q", [3, 4], 1.0)

# print tupB
#can call various elements of this tuple, and elements of that tuple

# print tupB [-1]
# print tupB[0]
# print (tupB[0])[3]
# print ((tupB[0])[3])[0]




#How to iterate thorough a tuple? Use a "for"  loop
# for item in tupB:
#     print item, 'is type', type(item)

#Or alternatively (top is simpler):
# for i in range(len(tupB)):
#     print tupB[i], 'is type', type(tupB[i])




#Adding an element to a list:
#
# lA = [0, 2, 1]
#
# lA = lA + ['i',]
# #or
# lA.append('ii')
# print lA

#METHODS:
# lA.remove(0)          #will remove first value
# lA.pop()              #removes LAST inserted value
# lA.extend([69, 70])   #adds to the list
# lA.sort()             #sorts list
# print lA

# empty = [[]]*10        #creates a list of ten empty lists (place holders)
# print empty





#Matrix example:

# M = [[0,1], [1,2], [2, 3], [3, 4]]      #creates a 4(rows) x 2(columns) matrix
# print M

#if you want to call the 3 row and second column you call:

# print M[2][1]     #remember that the first column is zero





#Lists and mutability:

# ListA = [1, 2, 3]
# ListB = [4, 5, 6]
# print "Ao", ListA
# print "Bo", ListB
#
# ListB = ListA
# ListA[0] = 'test'   #this changes the object that ListA points to; this is also what ListB is now pointing to (above line)
# print "A", ListA
# print "B", ListB    #ListB is bound to A, so a reassignment in ListA after assignment of B to A changes ListB




#Concatonation of a list into a tuple, and the reverse:

# tupl = ''
# for item in ListA:
#     tupl = tupl + str(item)
#     print tupl
#
# ListC = []
# for item in tupl:
#     ListC = ListC + [item,]
#     print ListC







#Dictionaries:
    #Keys are immutable objects (a list cannot be a key, a tuple or string can be though)

# Dict1 = {2: 'yes', 3: 'no', 4: ListA}
# print Dict1

# Dict1[2] = 'hellyes'        #changing what a key is bound to
# # print Dict1
# Dict1[5] = 'newelement'     #adding elements to a dict
# # print Dict1
# del Dict1[2]                #removing elements
# print Dict1
# if 5 in Dict1:              #searching for keys in a dict >>> this fxn only checks for keys, not values
#     print "we did it"
# if 6 not in Dict1:          #exclusion search
#     print "we didn't"









#Recursion:

#Factorial problem;
    #Basecase: n! = n*((n-1)!)

# def fact(n):
#     assert n >= 0  and type(n) == int
#     if n <= 1:                #can do 0 or 1 here, only need one value for your base case, both works as well
#         return 1
#     else:
#         return n*fact(n - 1)    #don't need to define a variable to be returned, can just return the recursive function
#
# print fact(14)
