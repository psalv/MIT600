__author__ = 'paulsalvatore57'


            #14 - Sampling and Monte Carlo Simulation



import random
import matplotlib.pylab


#Roll a pair of dice 24 times, what is the probability of getting two sixes
#Probably of  rolling a 6 on first die is 1/6, same with the second, so probability on first roll is 1/36

#Proabablity of not getting it is 35/36 > probability of not getting it 24 times in a row is (35/36)^24 = 0.51




def rollDie():
    """returns a random int between 1 and 6"""
    return random.choice([1,2,3,4,5,6])

# def testRoll(n = 10):
#     result = ''
#     for i in range(n):
#         result += str(rollDie())
#     print result

def checkPascal(numTrials = 100000):
    yes = 0.0
    for i in range(numTrials):
        for j in range(24):
            d1 = rollDie()
            d2 = rollDie()
            if d1 == 6 and d2 == 6:
                yes += 1
                break
    print 'Probability of losing = ' + str(1.0 - yes/numTrials)

# checkPascal()       #Close to prediction (not exact but exact isn't expected)



#We wrote a simulation to test this principle, but need to think is it easier to run a simulation or compute the probabilities?
#In practice we can do both (verify our probability with simulation, if no tin the ballpark then you need to investigate)



#MONTE CARLO SIMULATION: seeing how things will play out by running simulations
    #Inferential statistics: Based on principle that a random sample tends to exhibit same properties as the population from which it is drawn
        #IS THIS TRUE? Or do we have a biased sample causing this assumption to not hold?

    #If you get results distant from null hypothesis (assumes total randomness in many cases) than we can begin to make inferences about the system


def flip(numFlips):
    heads = 0
    for i in range(numFlips):
        if random.random() < 0.5:
            heads += 1
    return heads/float(numFlips)

# print flip(100000)
# print random.random()             #Gives a random number where 0.0 < n < 1.0


#LAW OF LARGE NUMBERS; Bernoullis Law: in repeated independent tests with the same actual probability of an outcome for each test,\
                                    #  the chance that the fraction of times that outcome occurs (of probability t) converges to p as num trials approaches infinity


def flipPlot(minExp, maxExp):
    ratios = []
    diffs = []
    xAxis = []
    for exp in range(minExp, maxExp + 1):
        xAxis.append(2**exp)
    for numFlips in xAxis:
        numHeads = 0
        for n in range(numFlips):
            if random.random() < 0.5:
                numHeads += 1
        numTails = numFlips - numHeads
        ratios.append(numHeads/float(numTails))
        diffs.append(abs(numHeads - numTails))
    matplotlib.pylab.title('Difference Between Heads and Tails')
    matplotlib.pylab.xlabel('Number of Flips')
    matplotlib.pylab.ylabel('Abs(#Heads - #Tails')
    matplotlib.pylab.plot(xAxis, diffs)
    matplotlib.pylab.figure()
    matplotlib.pylab.plot(xAxis, ratios)
    matplotlib.pylab.title('Heads/Tails Ratios')
    matplotlib.pylab.xlabel('Number of Flips')
    matplotlib.pylab.ylabel('Heads/Tails')
    matplotlib.pylab.figure()
    matplotlib.pylab.title('Difference Between Heads and Tails')
    matplotlib.pylab.xlabel('Number of Flips')
    matplotlib.pylab.ylabel('Abs(#Heads - #Tails')
    matplotlib.pylab.plot(xAxis, diffs, 'bo')
    matplotlib.pylab.semilogx()                     #Makes the axis logarithmic
    matplotlib.pylab.semilogy()
    matplotlib.pylab.figure()
    matplotlib.pylab.plot(xAxis, ratios, 'bo')      #b indicates colour, o indicates to not connect (no line)
    matplotlib.pylab.title('Heads/Tails Ratios')
    matplotlib.pylab.xlabel('Number of Flips')
    matplotlib.pylab.ylabel('Heads/Tails')
    matplotlib.pylab.semilogx()                     #No need to make y scale logarithmic in this scenario


flipPlot(4, 20)
matplotlib.pylab.show()



#How can we make statements of certainty within a degree of certainty? (Can never be 100% certain)








def flipSim(numFlipsPerTrial, numTrials):
    fracHeads = []
    for i in range(numTrials):
        fracHeads.append(flip(numFlipsPerTrial))
    mean = sum(fracHeads)/float(len(fracHeads))
    return (mean)

def stdDev(X):
    mean = sum(X)/float(len(X))
    tot = 0.0
    for x in X:
        tot += (x - mean)**2
    return math.sqrt(tot/len(X))