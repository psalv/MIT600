# __author__ = 'paulsalvatore57'

                        # 5 - OBJECTS IN PYTHON

# What if we want to collect items?
# 1) Tuples           #ordered sequences of objects
# 2) Lists            #ordered sequences of objects
# 3) Dictionaries     #not ordered



        ### 1) COLLECTING IN TUPLES

#Notice the REGULAR BRACKETS that signify a tuple

# Test = (1, 2, 3, 4, 5)          #sequence of ints, can look at various elements
# print Test[0]
# print Test[1]
# print Test[-1]                  #last element
# print len(Test)                 #length

#Slices of a tuple
t = 'abcde'
print t[2:]

#Finds divisors and collects them into a tuple
# x = 100
# divisors = ()
# for i in range(1,x):
#     if x%i == 0:                      #This function computes remainders
#         divisors = divisors + (i,)    #########Need to include (i,) to say it is a tuple of length one
#     # else:
#         # print 'Remainder:', float(x%i), 'Divisor:', i
#
# print divisors               #can take slices

#Tuples are immutable, therefore you can not change the value of a tuple (can create a new tuples
#but can't change the value of an old tuple; LISTS ARE MUTABLE, therefore more useful.









        ### 2) LISTS

#Need not be homogeneous, can have strings, ints, and lists of lists even
#Notice the SQUARE BRACKETS that signify a list

# Techs = ['MIT', 'Cal Tech']
# Ivys = ['Harvard', 'Yale', 'Brown']
# Univs = [1]
# Univs.append(Techs)             #Notice syntax, append is a METHOD, alternative syntax for a function >>> List.append(element),
# print 'Univs =', Univs              #actually mutates the list, has a side effect, want this side effect (modification on the list

#Univs becomes a list of length 1, and the element in it is in itself a list






# #Various mutations that can be applied to lists:
# Techs = ['MIT', 'Cal Tech']
# # Ivys = ['Harvard', 'Yale', 'Brown']
# Univs = []
# Univs.append(Techs)
# # print 'Univs =', Univs
# # Univs.append(Ivys)
# print 'Univs =', Univs          #Can append multiple lists to a list
# for e in Univs:                 #this will do something to every element in the list
#     print 'e =', e
#
# flat = Techs + Ivys             #Concatination takes the elements of the two lists and combines them into one
# print 'flat =', flat
#
# artSchools = ['RISD', 'Harvard']
# for u2 in artSchools:
#     if u2 in flat:              #This removes elements from the list
#         flat.remove(u2)
# print 'flat =', flat
#
# flat.sort()                     #Alphabetical or numerical sorting
# print 'flat =', flat
#
# flat[1] = 'UMass'               #Can change elements of lists
# print 'flat =', flat





#Various mutations to lists to show how the elements are affected, notice binding of one element can change while another does not
# L1 = [2]
# L2 = [L1, L1]
# print 'L2 =', L2
# L1[0] = 3
# print 'L2 =', L2
# L2[0] = 'a'
# print 'L2 =', L2
#
# L1 = [2]
# print 'L2 =', L2    #binding of L1 was changed, however this list is still pointing to the old object
# L2 = L1
# L2[0] = 'a'         #this is changing the object at this position, therefore L1 is affected
# print 'L1 =', L1
# print 'L2 =', L2
#
# L1 = [2]
# L2 = L1[:]
# L2[0] = 'a'
# print 'L1 =', L1





##Using a function to append lists:

# def CopyList(LSource, LDest):
#     for e in LSource:
#         LDest.append(e)
#         print 'LDest =', LDest
#
# L1 = []
# L2 = [1, 2, 3]
# CopyList(L2, L1)
# print L1
# print L2

##CopyList(L1, L1)        #L1 has been appended by L2 making it [1, 2, 3], now it is appended with itself
#This creates an infinite loop because there are an ever increasing number of e values in L1
#LSource and LDest are pointing to the same object, so modifying one, modifies the other:
    #This is the example of an ALIAS; one object with multiple names
        #Aliasing is perfectly fine wth immutable objects because you cannot change what the object means





#If you wanted to add only a certain number of elements to the list:
# def CopyList(LSource, LDest):
#     x = 0
#     for e in LSource:
#         x += 1
#         # print x
#         if x < 4:               #Number of elements that you want to add +1
#             LDest.append(e)
#             # print 'LDest =', LDest
#         else:
#             break
#
# L1 = []
# L2 = [1, 2, 3]
# CopyList(L2, L1)
# CopyList(L1, L1)
# print 'Appended L1 =', L1








        ### 3) DICTIONARY

#1) Elements are not ordered
#2) Indices need not be integers; are called KEYS (can be any immutable type)

# A dict is a set of key-value pairs (keys must be immutable)





#Example of a dictionary, notice a dictionary is INDICATED BY SET BRACES {}, to remind us that the contents are not ordered

# D = {1: 'one', 'deux': 'two', 'pi': 3.14159}        #can have string, int, and float objects; objects can be bound to other objects
# print D['pi']           #gives value with which the key is bound
# # assert False            #used to stop the program (for testing purposes)
#
# D1 = D
# print D1
#
# D[1] = 'uno'              #elements have mutability, can change what the key 1 is bound to
# print D1
# print D                   #since D1 is bound to D, when any element D changes what it is bound to, so does D1
#
# for k in D1.keys():
#     print k, '=', D1[k]   #this allows you to list every key in your dictionary and what it is bound to







# EtoF = {'bread': 'du pain', 'wine': 'du vin',\
#         'eats': 'mange', 'drinks': 'bois',\
#         'likes': 'aime', 1: 'un',\
#         '6.00':'6.00'}
# print EtoF          #prints the keys and their assignment
                        #order by which the keys are printed is not defined by python (non-predicatable)
                        #makes sense because dictionaries are not ordered, are sets rather than sequences

# print EtoF.keys()   #just prints the keys
# print EtoF.keys     #does not work, the () is necessary
# del EtoF['eats']    #removes select keys from the dictionary
# print EtoF









###USING DICTIONARIES WITH FUNCTIONS:

# EtoF = {'bread': 'du pain', 'wine': 'du vin', 'eats': 'mange', 'drinks': 'bois',\
#         'likes': 'aime', 1: 'un', '6.00':'6.00'}
#
# #FXN TO TRANSLATE WORDS:
# def translateWord(word, dictionary):
#     if word in dictionary:
#         return dictionary[word]
#     else:
#         return word
#
# #FXN TO TRANSLATE ENTIRE SENTENCES:
# def translate(sentence):
#     translation = ''
#     word = ''
#     for c in sentence:
#         if c != ' ':
#             word = word + c                                     #collects all of the words until there is a blank
#             # print word
#         else:
#             translation = translation + ' '\
#                           + translateWord(word, EtoF)           #calls the translation function, defining the dictionary to use
#             word = ''                                           #this resets the word so as to prepare for the next word to translate
#     return translation[1:] + ' ' + translateWord(word, EtoF)
# #
# print translate('John eats bread')
# print translate('Steve drinks wine')
# print translate('John likes 6.00')