__author__ = 'paulsalvatore57'

        #Class 11 - Object-Oriented Programming and Inheritance



#Abstract data type > adding user defined types
    #Define an INTERFACE for each type, which explains what the methods do (at the level of the user, not how they do it)

#SPECIFICATION of a type or method tells us what it does (difference between specficiation and implementation)

class intSet(object):                                           #New abstract type, it is saying that every instance of intSet is an object, but everything is an object
    #An intSet is a set of integers
    def __init__(self):                                         #Whenever you see two underbars it indicates an elgant status in python (innate attributes)
        """Create an empty set of integers"""                   #Everytime you create a new object of intSet, this will be executed on that object
        self.numBuckets = 47                                        #I this case two attributes of the object are introduced (numBuckets and vals), vals will be initialized
        self.vals = []                                              #NumBuckets and val are now attributes of s
        for i in range(self.numBuckets):                                #Example: If s = intSet(), s.numBuckets() will give us the value 47
            self.vals.append([])

    def hashE(self, e):
        #Private function, should not be used outside of class
        return abs(e)%len(self.vals)

    def insert(self, e):
        """Assumes e is an integer and inserts e into self"""
        for i in self.vals[self.hashE(e)]:
            if i == e: return
        self.vals[self.hashE(e)].append(e)

    def member(self, e):
        """Assumes e is an integer
           Returns True if e is in self, and False otherwise"""
        return e in self.vals[self.hashE(e)]

    def __str__(self):                                          #Code is returning a string representation of the set (this is a conventional way of denoting a set)
        """Returns a string representation of self"""
        elems = []
        for bucket in self.vals:
            for e in bucket: elems.append(e)
        elems.sort()
        result = ''
        for e in elems: result += str(e) + ','
        return '{' + result[:-1] + '}'

def test1():
    s = intSet()
    for i in range(40):
        s.insert(i)             #Looks like we are calling insert with only one argument, but s before the dot is the first arguement to the method insert
                                    #Implicit first argument is always called self in python (not enforced, but a convention)
    print s.member(14)
    print s.member(41)
    print s                     #Knows to convert s to a string (__str__ method is automatically envoked)
    print s.vals #Evil
#Make no attributes to data attributes of the class, this is evil (shouldn't do this)
    #Programs don't depend on the way people chose to implement the types, depends on the specification of the types
    #If implementation is changed your program might break (can go back and change variable numBuckets, so don't want to depend on it)

    #DATA HIDING (most important element that makes abstract data types useful, when you ignore this, do this at peril)
        #Hiding the instance variables (variables associated with each instance of the class) > get a new copy each time we get a new instance of the set
        #Should also hide class variables (haven't seen these yet) > associated with class itself, get a the same copy each time

# test1()


#NEXT EXAMPLE: How we use classes and abstract data types to design programs
    #Keeping track of students/faculty at MIT


#Want to think about what abstracts would be useful for the program we want to write before just writing it
#Think about types that woudl make it easy to write the code
    #Can be done without classes (using pythons built in classes) , but will not be elegant

#Want to be thinking at a different level of abstraction, not thinking about lists, dicts and floats

#Set up inheritance to be thinking about this (want to be able to share code)
    #There will be similarity between students and faculty
    #Only want to implement things once, so you can reuse that code for similarities


#Abstraction, everyone is a person

import datetime
#Class someone else wrote dealing with dates and time

class Person(object):

    def __init__(self, name):
        #create a person with name: name
        self.name = name
        try:
            firstBlank = name.rindex(' ')           #This is finding where the space is (the index) > r signifies the right side
            # print firstBlank
            self.lastName = name[firstBlank+1:]     #Used for just having the last name, we will probably need this at some point
        except:
            self.lastName = name
        self.birthday = None                        #Initializing birthday to None

    def getLastName(self):                          #Already have the last name, already have it, but don't want user to know you have the attribute self.lastName (implementation)
        #return self's last name                        #Often have things called get returning some implementation of an instance of the class
        return self.lastName

    def setBirthday(self, birthDate):
        #assumes birthDate is of type datetime.date
        #sets self's birthday to birthDate
        assert type(birthDate) == datetime.date     #Datetime is a built in class, so we are ensuring that this is the correct type, then assigning birthday to this value
        self.birthday = birthDate

    def getAge(self):
        #assumes that self's birthday has been set
        #returns self's current age in days
        assert self.birthday != None
        return (datetime.date.today() - self.birthday).days         #Allows you to return age (allows subtract of dates)

    def __lt__(self, other):                                        #Less than, used to order names
        #return True if self's name is lexicographically greater
        #than other's name, and False otherwise
        if self.lastName == other.lastName:                         #Accounting for same last name, go to first name
            return self.name < other.name                               #Can write P1 < P2, and python will turn it into double underbar lt
        return self.lastName < other.lastName                           #Can use built in sort operator and it will use double underbar lt

    def __str__(self):
       #return self's name
        return self.name

# me = Person('Paul Salvatore')
# him = Person('Barack Johnson Obama')
# her = Person('Cher')

# print him
# print him.getLastName()

# him.setBirthday(datetime.date(1961, 8, 4))
# her.setBirthday(datetime.date(1958, 8, 16))

#him.birthday = '8/4/61' > tried to directly access an instance variable, this is not correct
# print him.birthday

# print "Cher:", her.getAge(), 'days'
# print "Obama:", him.getAge(), 'days'
# print her.getAge()/365, "years and", her.getAge()%365, "days"

# print him > her
# print him < her
# print me < her      #Haven't definied an age for me, so I have None value

# pList = [me, him, her]

# pList.sort()       #Pythons built in sort fxn

# print 'The people in the list are:'
# for p in pList:
#     print ' ' + str(p)

#VERY EASY WRITING CODE USING DATA ABSTRACTIONS




#Starting to use a HIERARCHY:

#Now we are looking at what makes people different
    #It is a subclass of a person, so it hs all of the properties of a person (uses person isntead of object)
        #INHERITS PROPERTIES OF SUPERCLASS, and ADDS A PROPERTY

class MITPerson(Person):

    nextIdNum = 0                           #Not associated with an instance of a person, but the class itself > CLASS VARIABLE
                                            #Every time you get a new instance of this class, can assign a unique ID (similar ot global variables)

    def __init__(self, name):               #Assigning ID numbers
        Person.__init__(self, name)
        self.idNum = MITPerson.nextIdNum
        MITPerson.nextIdNum += 1

    def getIdNum(self):
        return self.idNum

    def __lt__(self, other):                #Changed the definition of __lt__, comparing people basis of ID number rather than names
        return self.idNum < other.idNum

    def isStudent(self):                     #After G has been implemented bounce back and add ANOTHER method to the class MIT person
        return type(self) == UG or type(self) == G


# me2 = MITPerson('Barbara Beaver')
# print me2.getIdNum()
# me3 = MITPerson('Sue Yuan')
# print me3.getIdNum()
# me4 = MITPerson('Sue Yuan')
# print me4.getIdNum()
# me5 = Person('Sue Yuan')
# print me5.getIdNum()

# # print me3 < me2

# print 'me2 < me3 =', me2 < me3
# print 'me3 < me2 =', me3 < me2
# print '__lt__(me2, me3) =', Person.__lt__(me2, me3)
# print 'me2 == me5 =', me2 == me5

# print 'me4 < me5', me4 < me5            #Person isn't in MIT so does not have an ID number
                                            #Attribute error, trying to compare an attribute that does not exist





#Next subclass in the hierarchy:

class UG(MITPerson):

    def __init__(self, name):
        MITPerson.__init__(self, name)    #Gives UG an ID number and a name
        self.year = None

    def setYear(self, year):              #Introduces a new attibute, year
        if year > 5:
            raise OverflowError('Too many')
        self.year = year

    def getYear(self):
        return self.year


# ug1 = UG('John Doe')
# ug2 = UG('John Doe')
# p3 = MITPerson('Sue Yan')
# print ug1
# print ug1 < p3      #Both will have ID numebrs
# print ug1 == ug2    #Will have different ID numbers

class G(MITPerson):        #MIT person with no special properties, why introduce the type? Lets you do type checking > Can check if a graduate student
    pass

# g1 = G('Ronald Reagan')
# print type(g1)              #Class defined at outermost level (main), and it is called G
# print type(g1) == G




#Another class, a subclass of objects

class CourseList(object):

    def __init__(self, number):
        self.number = number
        self.students = []

    def addStudent(self, who):
        if not who.isStudent():
            raise TypeError('Not a student')
        if who in self.students:
            raise ValueError('Duplicate student')
        self.students.append(who)

    def remStudent(self, who):
        try:
            self.students.remove(who)
        except:
            print str(who) + ' not in ' + self.number

    def allStudents(self):
        for s in self.students:
            yield s

    def ugs(self):
        indx = 0
        while indx < len(self.students):
            if type(self.students[indx]) == UG:
                yield self.students[indx]
            indx += 1

    def __str__(self):
        """
        To make this code callable as a string it must be defined as such, as is done in this code
        """
        elems = []
        for e in self.students:
            elems.append(e)
        elems.sort()
        result = ''
        for e in elems: result += str(e) + ','
        return '{' + result[:-1] + '}'

me2 = UG('Barbara Beaver')
me3 = G('Sue Yuan')
me4 = G('Sue Yuan')
me5 = Person('Sue Yuan')

c = CourseList(2326)
c.addStudent(me3)
c.addStudent(me2)

print c