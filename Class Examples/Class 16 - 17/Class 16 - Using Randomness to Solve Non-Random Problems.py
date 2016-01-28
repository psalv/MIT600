__author__ = 'paulsalvatore57'



                #16 - Using Randomness to Solve Non-Random Problems


#Constructing computational models that model the real world; GAUSIAN distributions are used because they have nice properties
    #If not normally distributed and we assume it is, than our results will be inaccurate


#UNIFORM distributions: each result is equally probable (the range is the only parameter we need)
    #Occur in games made by humans, but rarely in nature

#EXPONENTIAL distributions: memory-less (only continuous distribution that is so)
    #Ex. of Assignment 7 the ability for virions to be cleared (will always be same probability)
    #If probability of virion being cleared is P, then the porbability of the virion still being present is:

            #At time 1: 1 - P
            #At time 2: (1 - P)**2
            #At time n: (1 - P)**n


import matplotlib.pylab
import random

def clear(n, clearProb, steps):
    numRemaining = [n]
    for t in range(steps):
        numRemaining.append(n*((1-clearProb)**t))                       #Append probabili ty of remaining with each new step
    matplotlib.pylab.plot(numRemaining, label = 'Exponential Decay')

# clear(1000, 0.1, 500)
# matplotlib.pylab.semilogy()     #Appears straight due to log axis
# matplotlib.pylab.show()             #Exponential on a log axis gives a STRAIGHT line




def clearSim(n, clearProb, steps):          #This code clears molecules at each step
    numRemaining = [n]
    for t in range(steps):
        numLeft = numRemaining[-1]
        for m in range(numRemaining[-1]):
            if random.random() <= clearProb:
                numLeft -= 1
        numRemaining.append(numLeft)
    matplotlib.pylab.plot(numRemaining, 'r', label = 'Simulation')

# clearSim(1000, 0.1, 500)
# clear(1000, 0.1, 500)         #Adding this one will compare the simulation and analytic
# matplotlib.pylab.show()


#Comparison of analytic and simulation models: very similar
    #Both models show exponential decay, but are not identical: no right answer what is better





#Evaluating a model:
    #1 - FIDELITY, or credibility (do we believe the model that we create), can we convince ourselves thi model is correct
    #2 - UTILITY, or what questions are answerable with the model.
        #Simulations often allow us to ask 'what if' questions (can change the model to account for parameters hard to account for in analytical)
            #Ex. if every 100 time steps the virion cloned themselves (population doubles) > so easy in a simulation to show this, not in analytical models






#Monty Hall Problem:
    #3 doors, only one has a prize
    #You pick door one, door 3 is open to reveal that it does not have a prize
    #Two possible doors now, do you want to switch?


    #When you choose the first time you have a 1/3 probability of having chosen the correct door
    #The probability of the prize being behind the other doors is 2/3, but by eliminating one of them (opening it) the remaining door has a 2/3 probability

    #Choice of door being opened is not independent of the choice of the player (Monte will never open the door the player has picked)


def montyChoose(guessDoor, prizeDoor):
    if 1 != guessDoor and 1 != prizeDoor:
        return 1
    if 2 != guessDoor and 2 != prizeDoor:
        return 2
    return 3

def randomChoose(guessDoor, prizeDoor):
    if guessDoor == 1:
        return random.choice([2,3])
    if guessDoor == 2:
        return random.choice([1,3])
    return random.choice([1,2])



def simMontyHall(numTrials = 100, chooseFcn = montyChoose):
    stickWins = 0
    switchWins = 0
    noWin = 0
    prizeDoorChoices = [1, 2, 3]
    guessChoices = [1, 2, 3]
    for t in range(numTrials):
        prizeDoor = random.choice([1, 2, 3])
        guess = random.choice([1, 2, 3])
        toOpen = chooseFcn(guess, prizeDoor)
        if toOpen == prizeDoor:
            noWin += 1
        elif guess == prizeDoor:
            stickWins += 1
        else:
            switchWins += 1
    return (stickWins, switchWins)



def displayMHSim(simResults):
    stickWins, switchWins = simResults                                      #This is a way of assigning variables from a tuple
    matplotlib.pylab.pie([stickWins, switchWins], colors = ['r', 'g'],      #Application of pie graphs
              labels = ['stick', 'change'], autopct = '%.2f%%')
    matplotlib.pylab.title('To Switch or Not to Switch')



# results = simMontyHall(100000, montyChoose)       #Using fxns as parameters
# displayMHSim(results)
# matplotlib.pylab.figure()
# results = simMontyHall(100000, randomChoose)
# displayMHSim(results)
# matplotlib.pylab.show()

#This example illustrates how having events that are not independent can alter probability








#RANDOMIZATION as a tool to solve nonrandom problems:

    #Pi: historically people have been solving for approximations of pi

    #17th century: Had a circle in a square, and dropped needles in the center
        #Counted number of needles in the circle, and number in square but outside of circle

        #Needles in circle/Needles in square = Area circle/Area square
        #If radius = 1, then pi = area circle = area square * needles in circle/needles in square

        #Couldn't accurately perform the experiment



def stdDev(X):                      #Using SD to determine when we are done dropping (when SD is sufficiently low)
    mean = sum(X)/float(len(X))
    tot = 0.0
    for x in X:
        tot += (x - mean)**2
    return (tot/len(X))**0.5

def throwNeedles(numNeedles):
    inCircle = 0
    estimates = []
    for Needles in xrange(1, numNeedles + 1, 1):
        x = random.random()
        y = random.random()
        if (x*x + y*y)**0.5 <= 1.0:
            inCircle += 1
    return 4*(inCircle/float(Needles))

def estPi(precision = 0.01, numTrials = 20):
    numNeedles = 1000
    numTrials = 20
    sDev = precision
    while sDev >= (precision/4.0):                      #Precision of 0.01: we divide by 4 rather than two because we're looking 2 SDs on either side of curve
        estimates = []
        for t in range(numTrials):
            piGuess = throwNeedles(numNeedles)
            estimates.append(piGuess)
        sDev = stdDev(estimates)
        curEst = sum(estimates)/len(estimates)
        curEst = sum(estimates)/len(estimates)
        print 'Est. = ' + str(curEst) +\
              ', Std. dev. = ' + str(sDev)\
              + ', Needles = ' + str(numNeedles)
        numNeedles *= 2
    return curEst

# print estPi()

#Estimates don't necessarily get better, but the SD will decrease with each estimate
    #Because of normal distribution, we can be sure that the answer given +/- the SD contains pi





#Integrals are the area under some curve: can do the exact same needle method
    #Often ineffective for single integral, but more complex (double and triple) integrals are modelled nicely by Monte Carlo simulation


def integrate(a, b, f, numPins):
    pinSum = 0.0
    for pin in range(numPins):
        pinSum += f(random.uniform(a, b))       #Random uniform returns a random value between the given numbers
    average = pinSum/numPins
    return average*(b - a)


def doubleIntegrate(a, b, c, d, f, numPins):
    pinSum = 0.0
    for pin in range(numPins):
        x = random.uniform(a, b)
        y = random.uniform(c, d)
        pinSum += f(x, y)
    average = pinSum/numPins
    return average*(b - a)*(d - c)

