# 6.00 Problem Set 9: Intelligent Course Advisor


SUBJECT_FILENAME = "subjects.txt"

SHORT_SUBJECT_FILENAME = "shortened_subjects.txt"
VALUE, WORK = 0, 1


import itertools


# Problem 1: Building A Subject Dictionary

def loadSubjects(filename):
    """
    Returns a dictionary mapping subject name to (value, work), where the name
    is a string and the value and work are integers. The subject information is
    read from the file named by the string filename. Each line of the file
    contains a string of the form "name,value,work".

    returns: dictionary mapping subject name to (value, work)
    """
    inputFile = open(filename)
    dictionary = {}
    for line in inputFile:
        temp = line.replace(',', ' ')
        temp = temp.split()
        dictionary[temp[0]] = (int(temp[1]), int(temp[2]))
        # print dictionary
    return dictionary

# loadSubjects('subjects.txt')


def printSubjects(subjects):
    """
    Prints a string containing name, value, and work of each subject in
    the dictionary of subjects and total value and work of all subjects
    """
    totalVal, totalWork = 0,0
    if len(subjects) == 0:
        return 'Empty SubjectList'
    res = 'Course\tValue\tWork\n======\t====\t=====\n'
    subNames = subjects.keys()
    subNames.sort()
    for s in subNames:
        val = subjects[s][VALUE]
        work = subjects[s][WORK]
        res = res + s + '\t' + str(val) + '\t' + str(work) + '\n'
        totalVal += val
        totalWork += work
    res = res + '\nTotal Value:\t' + str(totalVal) +'\n'
    res = res + 'Total Work:\t' + str(totalWork) + '\n'
    print res










# Problem 2: Subject Selection By Greedy Optimization


def cmpValue(subInfo1, subInfo2):
    """
    Returns True if value in (valure, work) tuple subInfo1 is GREATER than
    value in (value, work) tuple in subInfo2
    """
    return int(subInfo1[0]) > int(subInfo2[0])

def cmpWork(subInfo1, subInfo2):
    """
    Returns True if work in (value, work) tuple subInfo1 is LESS than than work
    in (value, work) tuple in subInfo2
    """
    return int(subInfo1[1]) < int(subInfo2[1])

def cmpRatio(subInfo1, subInfo2):
    """
    Returns True if value/work in (value, work) tuple subInfo1 is 
    GREATER than value/work in (value, work) tuple in subInfo2
    """
    return float(subInfo1[0])/int(subInfo1[1]) > float(subInfo2[0])/int(subInfo2[1])


#My comparators:
def getVal(course):
    return int(course[1][0])
def getWork(course):
    return int(course[1][1])
def getRatio(course):
    return float(course[1][0])/int(course[1][1])

def getRatio1(course):
    return float(course[0])/int(course[1])


def greedyAdvisor_mySol(subjects, maxWork, comparator):
    """
    Returns a dictionary mapping subject name to (value, work) which includes
    subjects selected by the algorithm, such that the total work of subjects in
    the dictionary is not greater than maxWork.  The subjects are chosen using
    a greedy algorithm.  The subjects dictionary should not be mutated.

    subjects: dictionary mapping subject name to (value, work)
    maxWork: int >= 0
    comparator: function taking two tuples and returning a bool
    returns: dictionary mapping subject name to (value, work)
    """
    if comparator == getWork:
        rev=False
    else:
        rev=True
    ordered = sorted(subjects.items(), key=comparator, reverse=rev)
    taken = {}
    work = 0
    for i in ordered:
        work += int(i[1][1])
        if work > maxWork:
            work -= int(i[1][1])
        else:
            taken[i[0]] = i[1]

    fvalue = 0
    fwork = 0
    ftaken = []
    for i in taken:
        fvalue += int(taken[i][0])
        fwork += int(taken[i][1])

        ftaken += [i,]
    return ftaken, fvalue, fwork
    # return taken
#My way of greedy used the comparators directly above rather than the true/false statements, it will give the desired answer but differently

# subjects = loadSubjects('shortened_subjects.txt')

def testfirst():
    temp = greedyAdvisor_mySol(subjects, 100, getVal)
    print 'VALUE'
    print 'Classes taken: ', temp[0]
    print 'Value: ', temp[1]
    print 'Work: ', temp[2]
    print "------------"
    temp = greedyAdvisor_mySol(subjects, 100, getWork)
    print 'WORK'
    print 'Classes taken: ', temp[0]
    print 'Value: ', temp[1]
    print 'Work: ', temp[2]
    print "------------"
    temp = greedyAdvisor_mySol(subjects, 100, getRatio)
    print "RATIO"
    print 'Classes taken: ', temp[0]
    print 'Value: ', temp[1]
    print 'Work: ', temp[2]

# testfirst()








#I am going to attempt to solve the problem the way it was intended:


#These two functions (from previous problem sets) will be used to recursively sort the list:
    #Using the divide and conquer method, in which a list of size 1 is always sorted
    #This is a technique that I need to understand better since it was immensely helpful in this problem set

def merge(left, right, lt, dictionary):
    """Assumes left and right are sorted lists.
     lt defines an ordering on the elements of the lists.
     Returns a new sorted(by lt) list containing the same elements
     as (left + right) would contain."""
    result = []
    i, j = 0, 0
    while i < len(left) and j < len(right):
        if lt(dictionary[left[i]], dictionary[right[j]]):
            result.append(left[i])
            i += 1
        else:
            result.append(right[j])
            j += 1
    while (i < len(left)):
        result.append(left[i])
        i += 1
    while (j < len(right)):
        result.append(right[j])
        j += 1
    return result

def sort(L, comp, dictionary):
    """Returns a new sorted list containing the same elements as L"""
    if len(L) < 2:
        return L[:]
    else:
        middle = int(len(L) / 2)
        left = sort(L[:middle], comp, dictionary)
        right = sort(L[middle:], comp, dictionary)
        return merge(left, right, comp, dictionary)


def greedyAdvisor(subjects, maxWork, comparator):
    """
    Returns a dictionary mapping subject name to (value, work) which includes
    subjects selected by the algorithm, such that the total work of subjects in
    the dictionary is not greater than maxWork.  The subjects are chosen using
    a greedy algorithm.  The subjects dictionary should not be mutated.

    subjects: dictionary mapping subject name to (value, work)
    maxWork: int >= 0
    comparator: function taking two tuples and returning a bool
    returns: dictionary mapping subject name to (value, work)
    """
    keys = []
    for i in subjects:
        keys += [i,]
    sorted = sort(keys, comparator, subjects)
    work = 0
    taken = {}
    for i in sorted:
        work += int(subjects[i][1])
        if work > maxWork:
            work -= int(subjects[i][1])
        else:
            taken[i] = subjects[i]
    return taken














subjects = loadSubjects('shortened_subjects.txt')

# Problem 3: Subject Selection By Brute Force

#We want the best value in our given maxWork

            #1) Represent each item by a pair (value and weight)
            #2) W = max weight that can be carried
            #3) Set of available items is a vector: I
            #4) Another vector representing what has been taken: v

                    #  v[i] = 0 implies I[i] has not been taken
                    #  v[i] = 1 implies I[i] has been taken

            #Maximize: Sum of v[i] * I[i].value (don't take it is 0*value, you do take it's 1*value)
            #Constraint: (Sum of v[i] * I[i].weight) <= W



def bruteForceAdvisor(subjects, maxWork):
    """
    Returns a dictionary mapping subject name to (value, work), which
    represents the globally optimal selection of subjects using a brute force
    algorithm.

    subjects: dictionary mapping subject name to (value, work)
    maxWork: int >= 0
    returns: dictionary mapping subject name to (value, work)
    """
    n = len(subjects)
    available = []
    poss = list(itertools.product([0, 1], repeat=n))
    for i in subjects:
        available += [i,]

    maxVal = 0
    best_pos = []
    trial = 0

    for i in poss:

        value = 0
        work = 0
        for j in range(len(i)):
            work += i[j]*subjects[available[j]][1]
            value += i[j]*subjects[available[j]][0]
        if value > maxVal and work <= maxWork:
            maxVal = value
            best_pos = i[:]
        trial += 1
        if trial%100000 == 0:
            print 'Attempted: ', trial, ' out of ', 2**len(subjects), 'possible solutions.'

    answer = {}
    for i in range(len(best_pos)):
        if best_pos[i] == 1:
            answer[available[i]] = subjects[available[i]]

    return answer



print bruteForceAdvisor(subjects, 30)



