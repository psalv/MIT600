__author__ = 'paulsalvatore57'


            #12 - Simulation and Random Walks


#First part dealt with code from last lecture:


class Person(object):
    import datetime
    def __init__(self, name):
        #create a person with name name
        self.name = name
        try:
            firstBlank = name.rindex(' ')
            self.lastName = name[firstBlank+1:]
        except:
            self.lastName = name
        self.birthday = None
    def getLastName(self):
        #return self's last name
        return self.lastName
    def setBirthday(self, birthDate):
        #assumes birthDate is of type datetime.date
        #sets self's birthday to birthDate
        assert type(birthDate) == datetime.date
        self.birthday = birthDate
    def getAge(self):
        #assumes that self's birthday has been set
        #returns self's current age in days
        assert self.birthday != None
        return (datetime.date.today() - self.birthday).days
    def __lt__(self, other):
        #return True if self's name is lexicographically greater
        #than other's name, and False otherwise
        if self.lastName == other.lastName:
            return self.name < other.name
        return self.lastName < other.lastName
    def __str__(self):
        #return self's name
        return self.name

class MITPerson(Person):
    nextIdNum = 0
    def __init__(self, name):
        Person.__init__(self, name)
        self.idNum = MITPerson.nextIdNum
        MITPerson.nextIdNum += 1
    def getIdNum(self):
        return self.idNum
    def __lt__(self, other):
        return self.idNum < other.idNum
    def isStudent(self):
        return type(self)==UG or type(self)==G

class UG(MITPerson):
    def __init__(self, name):
        MITPerson.__init__(self, name)
        self.year = None
    def setYear(self, year):
        if year > 5:
            raise OverflowError('Too many')
        self.year = year
    def getYear(self):
        return self.year
#
# class G(MITPerson):
#     pass
#
# class CourseList(object):
#     def __init__(self, number):                         #when we create an instance of course list, we define the course number and an empty list of students
#         self.number = number
#         self.students = []
#     def addStudent(self, who):
#         if not who.isStudent():                         #uses the isStudent() code from MIT class to check if this person actually goes here (defensive programming, DP)
#             raise TypeError('Not a student')
#         if who in self.students:                        #checks to see if they have already been added (DP)
#             raise ValueError('Duplicate student')
#         self.students.append(who)                       #if not they are added
#     def remStudent(self, who):
#         try:
#             self.students.remove(who)
#         except:
#             print str(who) + ' not in ' + self.number   #DP
#     def allStudents(self):
#         for s in self.students:
#             yield s                                     #Not directly accumulating a list
#     def ugs(self):
#         indx = 0
#         while indx < len(self.students):
#             if type(self.students[indx]) == UG:         #This will tell you all of the students that are UG, doesn't stop when it has found just one
#                 yield self.students[indx]                   #Up until this point I have been collecting answers such as this in a list, this simplifies that process
#             indx += 1
#
#
# m1 = MITPerson('Barbara Beaver')
# ug1 = UG('Jane Doe')
# ug2 = UG('John Doe')
# g1 = G('Mitch Peabody')
# g2 = G('Ryan Jackson')
# g3 = G('Sarina Canelake')
# SixHundred = CourseList('6.00')
# SixHundred.addStudent(ug1)
# SixHundred.addStudent(g1)
# SixHundred.addStudent(ug2)

# try:
#     SixHundred.addStudent(m1)       #Not an UG or G, therefore cannot be added
# except:
#     print 'Whoops'

# print SixHundred                      #Perhaps not what one expected
# print SixHundred.students             #Gives instances of the list, but this is bad programming (using the instance, which couuld be changed)






# for i in SixHundred.students:         #For reason above, don't want to work with internal variables, this is bad
#     print i

# for i in SixHundred.allStudents():    #This is a better way to do above, define a method within the class rather than reaching into the instances
#     print i

#allStudents() method uses YIELD, which is apart of a GENERATOR, it is like a return but it does not finish at yield
    #A generator is a function that REMEMBERS the point in the body where it was (point in fxn body where it last returned, plus all local variables)
    #Gives you a way to decide how to create something you can use in a loop

    #Generator keeps track of state of computation so it can go back to what is was doing



# for i in SixHundred.allStudents():
#     for j in SixHundred.allStudents():
#         print i, j                      #Hangs on to the first element, and iterates through the list

# for i in SixHundred.ugs():
#     print i











###HOW DO WE BUILD COMPUTATIONAL MODELS TO SOLVE REAL PROBLEMS?

#For much of science people have tried to make ANALYTICAL METHODS (mathematical model), predict behaviour given initial predictions and some parameters
    #Doesn't always work

#Better with SIMULATION METHODS
    #Some systems are not mathematically tractable (hard to build mathematical models)
    #Better off successively refining a series of simulations (a lot of effort to try to make a predictive model, we can just refine instead)
    #Often easier to extract useful intermediate results
    #Computers have made it feasible

#Simulations are doing experiments and seeing what will happen to a system under certain conditions, rather than trying to predict it


#Want ot build a model:
    #Gives useful information about the behavior of a system >>> Analytical tries to exactly predict this
        #Result won't be exactly correct, but will be some approximation
    #Simulation models are descriptive >>> Analytical is prescriptive
        #Given a particular scenario, can give a guess of what will happen, but can run the same simulation many times and get slightly different answers


#Brownian motion is a historical example of simulation (Einstein used this to prove the existence of atoms)
    #Example of a RANDOM WALK:
    #If I have a system of interacting objects, want to model what happens in the system under assumption that each object will move at each timestep

    #Extremely useful for modelling physical (weather), biological (protein dynamics), and social (stock market) situations



#DRUNK STUDENT:

#We have a student that each second can take one step in one of the four cardinal directions
#After 1000 steps, how far are they from where they started out?

#You want to associate distance with probability of being there:
#So after one step you have a distance 1 and probabilty of 4/4 for all scenarios
    #D0  > D1  = 1

#After two steps, you have:
    #D1  > D0  = 1/4
    #D1  > Dr2 = 1/2
    #D1  > D2  = 1/4

#After three steps, you have:
    #D0  > D1  = 1/4             (same probability as D0 from last step, can only go one way)
    #Dr2 > D1  = 1/2*1/2 = 1/4   (have the time will go back to 1, came from a probability of 1/2)
    #Dr2 > Dr5 = 1/2*1/2 = 1/4   (ones that don't go to 1 will go to r5)
    #D2  > D1  = 1/4*1/4 = 1/16
    #D2  > D3  = 1/4*1/4 = 1/16
    #D2  > Dr5 = 1/2*1/4 = 1/8

#For two steps, average distance is 1.2 (when you multiple all of the distances by probabilities)
#For three steps, average distance is 1.4


#We did this because when we do a simulation we need ot get an idea of what we are to expect
#This is looking like distance form 0 increases with number of steps


#What do I need?
    #1) Drunk
    #2) Field
    #3) Where the drunk is (Location)






#1) Location (where the drunk is)

import random
class Location(object):
    def __init__(self, x, y):                               #Initialization of position when we create an instance
        """x and y are floats"""
        self.x = x
        self.y = y

    def move(self, deltaX, deltaY):                         #Give me a change in x and a change in y, I will give back a new location
        """deltaX and deltaY are floats"""                  #Assumptions: flat ground, but also not restricting to 90 degrees (used floats for deltaX and deltaY)
        return Location(self.x + deltaX, self.y + deltaY)

    def getX(self):
        return self.x

    def getY(self):
        return self.y

    def distFrom(self, other):                              #This method is being used to find out exactly how far away from the starting location we are
        ox = other.x                                        #Needs you to give it another location, will compare to starting
        oy = other.y
        xDist = self.x - ox
        yDist = self.y - oy
        return (xDist**2 + yDist**2)**0.5                   #Use pythagorean to measure distance

    def __str__(self):
        return '<' + str(self.x) + ', ' + str(self.y) + '>'



#2) Field (maps the drunks in relation to the location)
    #collection of drunks, keeping track of where they are

class Field(object):                                                #This field has no limit to size (can go as far as possible), can have multiple drunks (not worrying about collisions)
    def __init__(self):
        self.drunks = {}

    def addDrunk(self, drunk, loc):
        if drunk in self.drunks:                                    #DP, checking to ensure drunk isn't already in the collection
            raise ValueError('Duplicate drunk')
        else:
            self.drunks[drunk] = loc                                #Representation is a dictionary of drunks and where they are

    def moveDrunk(self, drunk):
        if not drunk in self.drunks:                                #DP, check to make sure we actually have a drunk
            raise ValueError('Drunk not in field')
        xDist, yDist = drunk.takeStep()
        self.drunks[drunk] = self.drunks[drunk].move(xDist, yDist)  #Calling the move method from location to alter the location, and then stores it to the dictionary

    def getLoc(self, drunk):
        if not drunk in self.drunks:
            raise ValueError('Drunk not in field')
        return self.drunks[drunk]




#3) Drunk (actually takes the steps)

class Drunk(object):
    def __init__(self, name):
        self.name = name

    def takeStep(self):
        stepChoices = [(0,1), (0,-1), (1, 0), (-1, 0)]
        return random.choice(stepChoices)                           #Picking from random for the stepChoices, these can be easily changed

    def __str__(self):
        return 'This drunk is named ' + self.name

# jon = Drunk('jon')
# origin = Location(0, 0)
# f = Field()
# f.addDrunk(jon, origin)
#Added the drunk to the field at the given origin



def walk(f, d, numSteps):
    """
    Functions walks around for a determined number of steps
    """
    start = f.getLoc(d)
    for s in range(numSteps):
        f.moveDrunk(d)
    return(start.distFrom(f.getLoc(d)))


def simWalks(numSteps, numTrials):
    """
    Will simulate several tries of the walk, returning a list of distances
    """
    jon = Drunk('jon')
    origin = Location(0, 0)
    distances = []
    for t in range(numTrials):
        f = Field()
        f.addDrunk(jon, origin)
        distances.append(walk(f, jon, numSteps))
    return distances


def drunkTest(numTrials):
    """
    Will calculate the mean from various number of steps, returning mean, max and min
    """
    for numSteps in [10, 100, 1000, 10000, 100000]:
    # for numSteps in [0, 1, 2, 3]:
        distances = simWalks(numSteps, numTrials)
        print 'Random walk of ' + str(numSteps) + ' steps'
        print '  Mean =', sum(distances)/len(distances)                         #From the list, can take the sum of it, divided by the number of trials to get the mean
        print '  Max =', max(distances), 'Min =', min(distances)                #More statistics, using min and max built in fxns for lists
        # print '  -----'
        # print '  Percent of max distance walked by mean:', sum(distances)/len(distances)/numSteps*100, "%"
        # print ' '

drunkTest(100)
#More trials will be more accurate, be sure to sure to test with values that you kow the answer to