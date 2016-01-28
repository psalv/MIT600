__author__ = 'paulsalvatore57'



# def buildCodeBook():
#     letters ='.abcdefghijklnopqrstuvwxyz'
#     codeBook = {}
#     key = 0
#     for c in letters:
#         codeBook[key] = c
#         key += 1
#     return codeBook
# #should make a dictionary with a key representing every letter and a period (keys will range 1 - 25)
# # print buildCodeBook()
#
# def decode(cypherText, codeBook):
#     plainText = ''
#     for e in cypherText:
#         if e in codeBook:
#             plainText += codeBook[e]
#         else:
#             plainText += ' '
#     return plainText
#
# codeBook = buildCodeBook()
# msg = (3,2,41,1,0)
# print decode(msg, codeBook)
# #expected cb a.
# #needs to go through the codebook (unchanging, multiplier) n times, where n represents leg(cyphertext)
# #O(n)









# def addVectors(v1, v2):
#     """ assumes v1 and v2 are lists of ints. Returns a list containing
#        the pointwise sum of the elements in v1 and v2. E.g.,
#        addVectors([4,5], [1,2,3]) returns [5,7,3],and
#        addVectors([], []) returns []. Does not modify inputs."""
#     result = []
#     i = 0
#     while i < min(len(v1), len(v2)):
#         result = result + [v1[i] + v2[i],]
#         i += 1
#         # print result
#     if len(v1) > len(v2):
#         for x in v1[len(v2):]:
#             result.append(x)
#     else:
#           for x in v2[len(v1):]:
#             result.append(x)
#     return result
#
#
# v1 = [1, 1, 1, 1, 1, 1]
# v2 = [2, 2, 2, 2, 2, 2, 2]
# print addVectors(v1, v2)











# def getLines():
#     inputs = []
#     while True:
#         line = int(raw_input('Enter a positive integer, -1 to quit: '))
#         if line == -1:
#             break
#         inputs.append(line)
#     return inputs
#
# total = 0
# for e in getLines():
#     total += e
# print total







# def f(s):
#     """Assumes type(s) == str
#     returns the most abundant letter in the string"""
#     d = {}
#     for c in s:
#         if c in d.keys():
#             d[c] += 1
#         else:
#             d[c] = 1
#     x = None
#     for k in d.keys():
#         if x == None:
#             x = d[k]
#             y = k
#         elif d[k] > x:
#             x = d[k]
#             y = k
#     print d
#     return y
#
# print f('abbc')
# print f('aabbc')







# def f(L):
#     result = []
#     for e in L:
#         if type(e) != list:
#             result.append(e)
#         else:
#             return f(e)
#     return result

# print f('2')
# print f(3)          #for in statement would need to be in range


# print f([1, [[2, 'a'], ['a','b']], (3, 4)])
# print f(['3', 43, [[43, [42, [32]], 4, 2, '2']], 2])
        #returns the list of the deepest scope which comes first

