__author__ = 'paulsalvatore57'

# T = (0.1, 0.1)
# x = 0.0
# for i in range(len(T)):
#     for j in T:
#         x += i + j
#         print x
# print i
#
#
# q = 'qwe'
# print q[1:]






# def f(s):
#     print s
#     if len(s) <= 1:
#         return s
#     return f(f(s[1:])) + s[0] #Note double recursion
#
# print f('mat')
# print f('math')







# def findAll(wordList, lStr):
#     """assumes: wordList is a list of words in lowercase.
#                 lStr is a str of lowercase letters.
#                 No letter occurs in lStr more than once
#        returns: a list of all the words in wordList that contain
#                 each of the letters in lStr exactly once and no
#                 letters not in lStr."""
#     dstr = {}
#     key = 0
#     for i in lStr:
#         dstr[i] = key
#         key += 1
#     answer = []
#     i = 0
#     while i < len(wordList):            #cycles through words
#         d = {}                              #resets dict
#         for e in wordList[i]:
#             if e in dstr and e not in d:
#                 d[e] = 1
#             else:
#                 break
#         if len(d) == len(dstr) == len(wordList[i]):
#             answer = answer + [wordList[i],]
#         i += 1
#     return answer
#
#
# wlist = ['hat', 'hatt', 'hate', 'etha', 'reta', 'athe']
# wstr = 'thae'
# print findAll(wlist, wstr)






def addVectors(v1, v2):
    """assumes v1 and v2 are lists of ints.
       Returns a list containing the pointwise sum of
       the elements in v1 and v2.  For example,
       addVectors([4,5], [1,2,3]) returns [5,7,3],and
       addVectors([], []) returns []. Does not modify inputs."""
    if len(v1) > len(v2):
        result = v1[:]
        other = v2[:]
    else:
        result = v2[:]
        other = v1[:]
    for i in range(len(other)):
        result[i] += other[i]
    return result

v1 = [1, 1, 1, 1]
v2 = [2, 3, 4]
print addVectors(v1, v2)