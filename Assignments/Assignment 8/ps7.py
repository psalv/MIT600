__author__ = 'paulsalvatore57'
# Problem Set 7: Simulating the Spread of Disease and Virus Population Dynamics
# Name:
# Collaborators:
# Time:

import numpy
import random
import matplotlib.pylab

'''
Begin helper code
'''

class NoChildException(Exception):
    """
    NoChildException is raised by the reproduce() method in the SimpleVirus
    and ResistantVirus classes to indicate that a virus particle does not
    reproduce. You can use NoChildException as is, you do not need to
    modify/add any code.
    """

'''
End helper code
'''


# PROBLEM 1

class SimpleVirus(object):
    """
    Representation of a simple virus (does not model drug effects/resistance).
    """

    def __init__(self, maxBirthProb, clearProb):
        """
        Initialize a SimpleVirus instance, saves all parameters as attributes
        of the instance.
        maxBirthProb: Maximum reproduction probability (a float between 0-1)
        clearProb: Maximum clearance probability (a float between 0-1).
        """
        self.maxBirthProb = maxBirthProb
        self.clearProb = clearProb

    def doesClear(self):
        """
        Stochastically determines whether this virus particle is cleared from the
        patient's body at a time step.
        returns: True with probability self.clearProb and otherwise returns
        False.
        """
        return random.random() <= self.clearProb


    def reproduce(self, popDensity):
        """
        Stochastically determines whether this virus particle reproduces at a
        time step. Called by the update() method in the SimplePatient and
        Patient classes. The virus particle reproduces with probability
        self.maxBirthProb * (1 - popDensity).

        If this virus particle reproduces, then reproduce() creates and returns
        the instance of the offspring SimpleVirus (which has the same
        maxBirthProb and clearProb values as its parent).

        popDensity: the population density (a float), defined as the current
        virus population divided by the maximum population.

        returns: a new instance of the SimpleVirus class representing the
        offspring of this virus particle. The child should have the same
        maxBirthProb and clearProb values as this virus. Raises a
        NoChildException if this virus particle does not reproduce.
        """
        if random.random() <= self.maxBirthProb*(1 - popDensity):               #Did not implement no child, decided that None argument was just as good
            return SimpleVirus(self.maxBirthProb, self.clearProb)                   #This may need to change with the next assignment if it uses the exception


class SimplePatient(object):
    """
    Representation of a simplified patient. The patient does not take any drugs
    and his/her virus populations have no drug resistance.
    """

    def __init__(self, viruses, maxPop):
        """
        Initialization function, saves the viruses and maxPop parameters as
        attributes.

        viruses: the list representing the virus population (a list of
        SimpleVirus instances)

        maxPop: the  maximum virus population for this patient (an integer)
        """
        self.viruses = viruses
        self.maxPop = maxPop

    def getTotalPop(self):
        """
        Gets the current total virus population.
        returns: The total virus population (an integer)
        """
        return len(self.viruses)

    def update(self):
        """
        Update the state of the virus population in this patient for a single
        time step. update() should execute the following steps in this order:

        - Determine whether each virus particle survives and updates the list
        of virus particles accordingly.
        - The current population density is calculated. This population density
          value is used until the next call to update()
        - Determine whether each virus particle should reproduce and add
          offspring virus particles to the list of viruses in this patient.

        returns: The total virus population at the end of the update (an
        integer)
        """
        newvirion = []
        for i in self.viruses:
            if i.doesClear():
                self.viruses.remove(i)
        popDensity = len(self.viruses)/float(self.maxPop)
        for i in self.viruses:
            temp = i.reproduce(popDensity)                  #Could have used the try operator here rather than having a temp
            if temp != None:
                newvirion += [temp,]
        for i in newvirion:
            self.viruses += [i,]
        return len(self.viruses)




# # PROBLEM 2

def simulationWithoutDrug(trials):
    """
    Run the simulation and plot the graph for problem 2 (no drugs are used,
    viruses do not have any drug resistance).
    Instantiates a patient, runs a simulation for 300 timesteps, and plots the
    total virus population as a function of time.
    """
    mean_num_virion = []
    for i in range(300):
        mean_num_virion += [0,]
    for i in range(trials):
        virion = []
        while len(virion) < 100:
            virion += [SimpleVirus(0.1, 0.05),]
        patient = SimplePatient(virion, 1000)
        mean_num_virion[0] = len(virion)
        call = 0
        while call < 299:
            call += 1
            patient.update()
            mean_num_virion[call] += patient.getTotalPop()/float(trials)       #I am adding the fractional amount that each trial would add to the mean, and plotting the mean
        print "Trial", i + 1, 'complete.'
    # print mean_num_virion
    print "Producing plot"
    matplotlib.pylab.plot(mean_num_virion)
    matplotlib.pylab.title('Virus Population in a Simple Patient, 200 Trials')
    matplotlib.pylab.xlabel('Timesteps')
    matplotlib.pylab.ylabel('Number of virion')
    matplotlib.pylab.savefig('Simple Virion Simulation')
    matplotlib.pylab.show()

# simulationWithoutDrug(100)



            #In the solutions they used a helper code to run one simulation, however my code works just fine doing the entire simulation at once

                #Interesting operator I found in the solutions was /=, I assume there is also *= which could prove to be useful

                #Another interesting pylab feature i found was: matplotlib.pylab.legend(loc = best); until now I was unsure how to input legends
















#Question 3 - Probablity


#Flip 3 coins:
#1 a) HHH:       2^3 options, therefore a 1/8 chance
#1 b) HTH:       Same as above, 1/8
#1 c) 2H and 1T: Can't have TTT, TTH, THT, HTT or HHH, therefore what remains are the possibilities: 3/8 chance
#1 d) #H >= #T:  Can't have TTT, TTH, THT, HTT, therefore probability is 4/8




#2 Rolling a Yatzhee on the first roll (all numbers the same, 5 six sided die):
    #There are six possible rolls of this type, and 6**5 options, therefore the probability is 6/6**5, or 1/6**4

# print 'Calculated Probability:', 1/float(6**4)




#3 Write a Monte Carlo Simulation to prove answer from 2

def rollD():
    return random.choice([1, 2, 3, 4, 5, 6])

def testYat(trials):
    yat = 0
    for i in range(trials):
        a = rollD()
        b = rollD()
        c = rollD()
        d = rollD()
        e = rollD()
        if a == b == c == d == e:
            yat += 1
    return yat/float(trials)

n = 500000
# print 'Simulated Probability:', testYat(n), "-", n, 'Trials'
