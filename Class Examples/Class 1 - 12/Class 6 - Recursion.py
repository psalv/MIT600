__author__ = 'paulsalvatore57'


            # 6 - RECURSION



#can use a list to store things if dictionaries did not exist
#must search through the entire list, very inefficient
    #dictionary retrieval is constant, independent of dictionary size
    #some data structures are easier to implement but less efficient

# def keySearch(L, k):
#     for elem in L:
#         if elem[0] == k: return elem[1]
#     return None






#DICTIONARIES

# EtoF = {'bread': 'du pain', 'wine': 'du vin',\
#         'eats': 'mange', 'drinks': 'bois',\
#         'likes': 'aime', 1: 'un',\
#         '6.00':'6.00'}
#
# def translateWord(word, dictionary):
#     if word in dictionary:                  #search dictionary to see if the word is key in the dictionary
#         return dictionary[word]             #returns what the key is bound to
#     else:
#        return word
#
# def translate(sentence):
#     translation = ''
#     word = ''
#     for c in sentence:
#         if c != ' ':                #finding when the end of a word is (building a word) > assumption words end in spaces, also assumes only 1 space between words
#             word = word + c
#         else:
#             translation = translation + ' ' + translateWord(word, EtoF)
#             word = ''
#     return translation[1:] + ' ' + translateWord(word, EtoF)   #last word won't be translated, can add a space at end alternatively
#
# print translate('John eats bread')
# print translate('Eric drinks wine')
# print translate('Everyone likes 6.00')



#Fxns valuable because it saves sapce and only needs to be debugged once.

    #MODULAR ABSTRACTION: if you use a code multiple times you only need to change the function,
    #don't need to search through code, this eases implementing changes (isolating where something is)



#DIVIDE AND CONQUER: break up a complicatd problem into smaller pieces
    #smaller problems are:
    # 1) easier to solve
    # 2) solutions of small problems can be easily combined to solve the big problem


#RECURSION: way of characterizing a problem, and designing solution (divide and conquer)

#BASECASE: typically gives us a direct answer
#INDUCTIVE/RECURSIVE CASE: reduce to a simpler version of same problem plus other simple operations



#CASE 1 > want to compute integer exponents, can only do multiplcation

#Things that we know about exponents:
# 1) If exponent is 0, than answer = 1
# 2) Answer is = b * b**(n-1)

# def simpleExp(b, n):
#     if n == 0:
#         return 1
#     else:
#         return b * simpleExp(b, n - 1)    #solving a smaller version of the same procedure
#                                             #will stop because it will eventually reach the base case
# print simpleExp(5, 4)

#when you get a problem don't immediately start to write code:
#tryr to think of how you an break the problem down to the base case







#HANOI STACK EXAMPLE:

#Know that to solve it we need a stack of n-1 on the unused (spare stack),
#a stack of 1 on the 'from stack',
#nothing on the 'to stack'

# def Hanoi(n, f, t, s):
#     """n = number of pieces
#         f = from stack
#             t = to stack
#                 s = spare stack"""
#     # print n
#     if n == 1:
#         print "move from", f,  "to", t
#     else:
#         Hanoi(n - 1, f, s, t)           #move a stack of n-1 onto the 'spare' stack, the stacks are being assigned different element names
#         Hanoi(1, f, t, s)                   #in the first for instance we want n - 1 on 'spare', so this is actually the 'to' stack
#         Hanoi(n - 1, s, t, f)               #conversely at the end we need them on the 'to' stack so we change this element again
#
# print Hanoi(4, 'From', 'To', 'Spare')

#w

#exponential problem







#PALINDROME:

#Things that we know about a palindrome:
# 1) Letter 0 == letter n
# 2) Letter i == letter n - i


# def palindrome(word, length):
#     """input: word, length of word (int)"""
#     lw = word.lower()
#     if length == 0:
#         print "Is a palindrome"
#     elif lw[len(word) - length] != lw[length - 1]:
#         print "Is not a palindrome"
#         return False
#     else:
#         palindrome(word, length - 1)
#     return True
#
# print palindrome('aa', 2)

#my solution forces the user to input the length of the word that they want to check to see if it is a palindrome




#HIS SOLUTION:

# 1) BASE CASE: If len(word) <= 1, than it is definitely a palindrome
            #my solution did not consider the base case, it only looked at various factors that are true



#
# def toChars(s):
#     import string
#     s = string.lower(s)
#     ans = ''
#     for c in s:
#         if c in string.lowercase:
#             ans = ans + c
#     return ans
# #this piece of code is removing all of the spaces/punctuation to check if sentences are palindromes (only leaves lower case letters)
# #seperating out things that we only need to do once, this is useful in general in programming
#
#
# def isPal(s):
#     if len(s) <= 1:                 #basecase
#         return True
#     else:
#         return s[0] == s[-1] and isPal(s[1:-1])
# #will be true if the first and last character are identical (false if they are not), and will also return a shortened by 1 on each side string
# #this is a notable piece of code: s[1:-1], because for a string "abcde" it will return "bcd" which is crucial for this operation
#
#
# def isPalindrome(s):
#     """Returns True if s is a palindrome and False otherwise"""
#     return isPal(toChars(s))
# #this function will first create a string of just lower case letters, and then run it through isPal,
# #isPal will sequentially remove letters form the end until the string is <= 1 in length, at which case it is definitely a palindrome
# #if at any point s[0] != s[-1], or rather the first and last positions aren't equal, returns False since the string does not meet palindromic criteria
#
#
# print isPalindrome('Guttag')
# print isPalindrome('Guttug')
# print isPalindrome('Able was I ere I saw Elba')
# print isPalindrome('Are we not drawn onward, we few, drawn onward to new era?')






#FIBINOCCI NUMBERS:

#start with 1 M, 1 F rabbit (0 months old)
#can mate at age of 1 month
#produces a new pair every 1 month after maturation
#never die
#how many female rabbits at the end of 12 months


#INDUCTIVE CASE: this pattern can be worked out to: n(i) = n(i - 1) - n (i - 2)
#BASECASE: when i <= 1 , n == 1


def fib(i):
    """Assumes x is an int, returns Fibonacci of i"""
    assert type(i) == int and i >= 0
    if i <= 1:
        return 1
    else:
        return fib(i - 1) + fib(i - 2)


def testFib(n):
    for i in range(n+1):
        print ('fib of', i, '=', fib(i))

testFib(20)




