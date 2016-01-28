__author__ = 'paulsalvatore57'

            #10 - HASHING AND CLASSES


#Hashing is an efficient search, but costly for space (trade space for time)

#Want to find if an integer is in a set:
    #Take an integer i, and hash it
       #converts i to some integer in a range (ex. range 0 - k)

       #hash(i) -> 0 > l

#Indexed into a list of lists, each list is called a bucket (which a bucket itself is a list)
    #know we can find ith element of a list in constant time

#Hash, go to the correct bucket (associated with the integer), and then search lsit at that buket to see if element is present
    #if list is short enough this is very efficient

#hash function is many-to-one, have a set in which you can store any integer
#many integers wil hash to the same bucket
#when two integers hash the same bucket, you have a collision
    #linear rehashing, not actually rehashing, just keeping a list

# numBuckets = 47                     #this is ugly.  We will see a better way soon, don't like to use global variables
#
# def create():
#     global numBuckets
#     hSet = []
#     for i in range(numBuckets):
#         hSet.append([])
#     return hSet
# #creates a list of lists, each element is empty at first
#
# # def hashElem(e):
# #     global numBuckets
# #     # print e
# #     # print e%numBuckets
# #     return e%numBuckets             #modular is the remainder, 47%43 = 4 , 100%43 = 14
#
# def insert(hSet, i):
#     hSet[hashElem(i)].append(i)
# #the insert function is used for inserting elements, first hashes
# # print insert([1], 3)
#
# def remove(hSet, i):
#     newBucket = []
#     for j in hSet[hashElem(i)]:
#         if j != i:
#             newBucket.append(j)
#     hSet[hashElem(i)] = newBucket
# #a little more complicated, insert does not look whether the element is already there (need to remove each element if it is there multiple times)
#
# def member(hSet, i):
#     return i in hSet[hashElem(i)]
# #checking for membership > is i in the list associated with the correct bucket?
# #complexity is the length of the bucket, this will depend on the number of buckets
#
#
# def test1():
#     s = create()
#     #made an empty list of lists, 47 buckets long (global variable)
#     for i in range(40):
#         insert(s, i)
#     #inserting the element i into the list, first hashing it such that everynumber from 0-39 will be added to their own bucket
#     insert(s, 325)
#     insert(s, 325)
#     insert(s, 987654321)
#     print s
#     print member(s, 325)
#     remove(s, 325)
#     print member(s, 325)
#     print member(s, 987654321)
#
# # numBuckets = 3
# # test1()
#
#
#
# #Good hash function has property that it will widely disperse values you hash (want values in different buckets)
# #Get larger buckets (fewer choices), when you have a lower number of buckets
#
# #If number of buckets is large relative to number of elements yo insert, than looking if an element in it is O(1)
#     #Constant time
#         #Generally want enough buckets that it is constant time (this is what python does with dictionaries)
#
# #Alternatively, if number of buckets is small than you have order O(n)
#     #Linear time
#
#
#
# #Any kind of immutable object can be hashed > keys in dict must be immutable so they can be hashed (need immutability to be able to find it)
#
#
#
# def hashElem(e):
#     global numBuckets
#     if type(e) == int:
#         val = e
#     if type(e) == str:
#         #Convert e to an int
#         val = 0
#         shift = 0
#         for c in e:
#             val = val + shift*ord(c)            #ord takes the internal representation (the bits) for the character
#             shift += 1
#     return val%numBuckets
#
#
# def test2():
#     d = create()
#     strs = ['ab', 'ba', '32a',
#             'big dog', 'small bird']
#     for s in strs:
#         insert(d, s)
#     for i in range(40):
#         insert(d, i)
#     print d
#     print member(d, 'small bird')
#     print member(d, 'big bird')
#     remove(d, 'small bird')
#     print d
#
# # test2()




###EXCEPTIONS

#In python errors are exceptions built into the program
#When the program stops (crashes) because of an exception they  are UNHANDLED EXCEPTIONS
    #Once program is debugged this should not happen

#Try/Except blocks
    #Will start to execute the try code, if it completes the code without exception it skips except, if not it goes to the except


# def readVal(valType, requestMsg, errorMsg):     #First arguemnt is a type (everything is an object)
#     numTries = 0
#     while numTries < 4:
#         val = raw_input(requestMsg)             #Tries to convert val to the type, if so it returns it
#         try:
#             val = valType(val)
#             return val
#         except ValueError:                      #If it cannot be converted (get a type error exception)
#             print(errorMsg)
#             numTries += 1
#     raise TypeError('Num tries exceeded')       #If goes through too many times raises type error and gives message
#
#
# # print readVal(int, 'Enter int: ', 'Not an int.')
#
#
# try:
#     readVal(int, 'Enter int: ', 'Not an int.')  #Try readVal function
# except TypeError, s:                            #If there is a typeerror, print the argument > Don't have to crash, can deal with the exception
#     print s                                         #Exception can have a sequence of arguments associated with it

#Can catch exceptions and relay back, example if you try to save something and the file already exists:
    #"Do you really want to overwrite this file?"

#Flow of control mechanism









####CLASSES (Intro)

#MODULE - collection of related functions
    #Code that includes things like import.math (provides access to fxns like math.log)
    #Import makes it convenient to import many things at once, use dot to specify where it was imported from (could import two fxns called member, table.member and set.member)

#Class is like a module, but not jsut a collection of fxns, it is a COLLECTION OF DATA AND FXNS
    #Fxns that operate on that data
    #Bound together so you can pass an object from one part of a program to another
        #When you pass the object, the new part of the program gets access to the fxns associated with that object

        #Key to object-oriented programming

#Data and fxns associated with an object are called that objects ATTRIBUTES (way to associate attributes with objects)
    #Both data and fxns are both objects (everything is an object, even the class is an object)

#Message passing metaphor
    #If you have circle.area(), it would call the area of the object circle
    #This is essentially a fancy way of writing fxns, nothing more

#METHOD is a fxn associated with an object
    #In above case the method area is associated with the object circle


#A class is a collection of objects with identical characteristics that form a type
    #Lists and Dicts are built in classes (don't need to reimplement them)
    #Classes let you add new types into the language every bit as easy to use as the built in types