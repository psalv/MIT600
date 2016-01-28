__author__ = 'paulsalvatore57'


        #13 - Probability and Plotting Data


#From last lecture (simulation of drunk person) we have an array of places he can end up contingent on number of steps
#The best way to make predictions would be to visualize (plot) this data
    #Plot mean distance vs number of steps for this case

#How much can we infer from the graph?
#Not too much, we get different answers every time, and a big difference between max and min
    #Don't have enough information to interpret it, we need more, so how do we think about the results of programs\
    #when the programs themselves are stochastic (randomly determined)

#Almost everything in the real world is stochastic, therefore it is important to think about it




#Coppenhagen doctrine: at most fundamental level the physical world cannot be predicted
#Can make probabilistic statements, but not certain statements
    #As opposed to Newtonian physics, created a debate in physics

#CAUSAL NON-DETERMINISM: belief that not every event is caused by previous events
    #Einstein argued against this, argued for PREDICTIVE NON-DETERMINISM: inability to make accurate measurements\
    #about the physical words limits our ability to make predictions
    #Things aren't unpredictable, we just don't know enough to make predictions

#Coins example, we have to act as if things are non-deterministic basing our choices on probability
#STOCHASTIC PROCESSES: next state depends on previous state
#So if you have 3 coins on a table and flip one, it depends on the previous state (non-flipped) and a stochastic element (flipped)



#random.choice > implemented using random.random (get a floating point value between 0.0 and 1.0)

def rollDie():
    """returns a random int between 1 and 6"""
    return random.choice([1,2,3,4,5,6])

#Each roll is independent therefore getting 10 1s in a row is equally as likely as getting 10 of mixed specific other values
#In stochastic process if the outcome of one event has no influence on the outcome of another than the events are independent

#There are 6^n possibilities, where n is the number of rolls, wherein each possibilities are equally likely
#Asking for probability: what fraction of possible results have the desired outcome (know probability is between 0 and 1)

#Typically can compute probability two ways:
    #1 - directly
    #2 - probability of something not happening (1 - direct)





#DATA PLOTTING: important to be able to show data in a way in which it can be interpreted
#Easy to make plots in python, someone built pylab for this > uses many of the same features as MATLAB

#Plotting capabilities in pylab are almost identical to MATLAB which is convenient

               #     """    matplotlib.sourceforge.net    """       < gives plotting capabilities, and chapter on course website



def testRoll(n = 10):
    result = ''
    for i in range(n):
        result = result + str(rollDie())
    print result




import matplotlib.pylab
#Take a minute to appreciate what a bitch it was to get pylab working



# matplotlib.pylab.plot([1,2,3,4], [1,2,3,4])        #Corresponds with x and y coordinates, it's imperative the lists are the same length
# matplotlib.pylab.plot([1,4,2,3], [5,6,7,8])
# matplotlib.pylab.show()                            #Necessary for us to show the plot > only execute show() once (should be the last thing) or program will end


# matplotlib.pylab.figure(1)
# matplotlib.pylab.plot([1,2,3,4], [1,2,3,4])
# matplotlib.pylab.figure(2)
# matplotlib.pylab.plot([1,4,2,3], [5,6,7,8])
# matplotlib.pylab.savefig('firstSaved')                #These files will now be saved to the directory
# matplotlib.pylab.figure(1)
# matplotlib.pylab.plot([5,6,7,10])                     #If you only give one set of values it assumes they are the y coordinates\
# matplotlib.pylab.savefig('secondSaved')               #and just makes up values for the x axis (for 4 elements x = 0, 1, 2, 3)
# matplotlib.pylab.show()


principal = 10000  #initial investment
interestRate = 0.05
years = 20
values = []
for i in range(years+1):
    values.append(principal)
    principal += principal*interestRate
matplotlib.pylab.plot(values)
matplotlib.pylab.title('5% Growth, Compounded Annually')    #How to label axes and title
matplotlib.pylab.xlabel('Years of Compounding')
matplotlib.pylab.ylabel('Value of Principal ($)')
matplotlib.pylab.show()



