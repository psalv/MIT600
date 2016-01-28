
import numpy as np
import random
import matplotlib.pylab as pylab
from ps7 import *


# PROBLEM 1

class ResistantVirus(SimpleVirus):
    """
    Representation of a virus which can have drug resistance.
    """
    def __init__(self, maxBirthProb, clearProb, resistances, mutProb):
        """
        Initialize a ResistantVirus instance, saves all parameters as attributes
        of the instance.

        maxBirthProb: Maximum reproduction probability (a float between 0-1)        
        clearProb: Maximum clearance probability (a float between 0-1).

        resistances: A dictionary of drug names (strings) mapping to the state
        of this virus particle's resistance (either True or False) to each drug.
        e.g. {'guttagonol':False, 'grimpex',False}, means that this virus
        particle is resistant to neither guttagonol nor grimpex.

        mutProb: Mutation probability for this virus particle (a float). This is
        the probability of the offspring acquiring or losing resistance to a drug.
        """
        self.maxBirthProb = maxBirthProb
        self.clearProb = clearProb
        self.resistances = resistances
        self.mutProb = mutProb

    def isResistantTo(self, drug):
        """
        Get the state of this virus particle's resistance to a drug. This method
        is called by getResistPop() in Patient to determine how many virus
        particles have resistance to a drug.    

        drug: The drug (a string)
        returns: True if this virus instance is resistant to the drug, False
        otherwise.
        """
        return self.resistances[drug]

    def reproduce(self, popDensity):
        """
        Stochastically determines whether this virus particle reproduces at a
        time step. Called by the update() method in the Patient class.

        If the virus particle is not resistant to any drug in activeDrugs,
        then it does not reproduce. Otherwise, the virus particle reproduces
        with probability:       
        
        self.maxBirthProb * (1 - popDensity).                       
        
        If this virus particle reproduces, then reproduce() creates and returns
        the instance of the offspring ResistantVirus (which has the same
        maxBirthProb and clearProb values as its parent). 

        For each drug resistance trait of the virus (i.e. each key of
        self.resistances), the offspring has probability 1-mutProb of
        inheriting that resistance trait from the parent, and probability
        mutProb of switching that resistance trait in the offspring.        

        For example, if a virus particle is resistant to guttagonol but not
        grimpex, and `self.mutProb` is 0.1, then there is a 10% chance that
        that the offspring will lose resistance to guttagonol and a 90% 
        chance that the offspring will be resistant to guttagonol.
        There is also a 10% chance that the offspring will gain resistance to
        grimpex and a 90% chance that the offspring will not be resistant to
        grimpex.

        popDensity: the population density (a float), defined as the current
        virus population divided by the maximum population        

        activeDrugs: a list of the drug names acting on this virus particle
        (a list of strings). 
        
        returns: a new instance of the ResistantVirus class representing the
        offspring of this virus particle. The child should have the same
        maxBirthProb and clearProb values as this virus. Raises a
        NoChildException if this virus particle does not reproduce.

        Drug resistance can only occur to drugs that are currently being administered (hence the active drug list).
        """
        if random.random() <= self.maxBirthProb*(1 - popDensity):
            new_resist = {}
            for i in self.resistances:
                if self.resistances[i] == True:
                    if random.random() >= (1 - self.mutProb):
                        new_resist[i] = False
                    else:
                        new_resist[i] = True
                else:
                    if random.random() <= (self.mutProb):
                        new_resist[i] = True
                    else:
                        new_resist[i] = False
        else:
            return None
        return ResistantVirus(self.maxBirthProb, self.clearProb, new_resist, self.mutProb)

class Patient(SimplePatient):
    """
    Representation of a patient. The patient is able to take drugs and his/her
    virus population can acquire resistance to the drugs he/she takes.
    """
    def __init__(self, viruses, maxPop):
        """
        Initialization function, saves the viruses and maxPop parameters as
        attributes. Also initializes the list of drugs being administered
        (which should initially include no drugs).               

        viruses: the list representing the virus population (a list of
        SimpleVirus instances)
        
        maxPop: the  maximum virus population for this patient (an integer)
        """
        self.viruses = viruses
        self.maxPop = maxPop
        self.drugs = []

    def addPrescription(self, newDrug):
        """
        Administer a drug to this patient. After a prescription is added, the 
        drug acts on the virus population for all subsequent time steps. If the
        newDrug is already prescribed to this patient, the method has no effect.

        newDrug: The name of the drug to administer to the patient (a string).

        postcondition: list of drugs being administered to a patient is updated
        """
        if newDrug not in self.drugs:
            self.drugs.append(newDrug)

    def getPrescriptions(self):
        """
        Returns the drugs that are being administered to this patient.
        returns: The list of drug names (strings) being administered to this
        patient.
        """
        return self.drugs

    def getResistPop(self, drugResist):
        """
        Get the population of virus particles resistant to the drugs listed in 
        drugResist.        

        drugResist: Which drug resistances to include in the population (a list
        of strings - e.g. ['guttagonol'] or ['guttagonol', 'grimpex'])

        returns: the population of viruses (an integer) with resistances to all
        drugs in the drugResist list.
        """
        resistant = 0
        for virus in self.viruses:
            num_resist = 0
            for drug in drugResist:
                if virus.isResistantTo(drug):
                    num_resist +=1
            if num_resist == len(drugResist):
                resistant += 1
        return resistant

    def update(self):
        """
        Update the state of the virus population in this patient for a single
        time step. update() should execute these actions in order:
        
        - Determine whether each virus particle survives and update the list of 
          virus particles accordingly          
        - The current population density is calculated. This population density
          value is used until the next call to update().

        -Virion that are not resistant to all drugs do not reproduce

        - Determine whether each virus particle should reproduce and add
          offspring virus particles to the list of viruses in this patient. 
          The list of drugs being administered should be accounted for in the
          determination of whether each virus particle reproduces. 

        returns: the total virus population at the end of the update (an
        integer)
        """
        newvirion = []
        for i in self.viruses:
            if i.doesClear():
                self.viruses.remove(i)
        popDensity = len(self.viruses)/float(self.maxPop)
        for virus in self.viruses:
            num_resist = 0
            for drug in self.drugs:
                if virus.isResistantTo(drug):
                    num_resist +=1
            if num_resist == len(self.drugs):
                temp = virus.reproduce(popDensity)
                if temp != None:
                    newvirion += [temp,]
        for i in newvirion:
            self.viruses += [i,]


# PROBLEM 2

def simulationWithDrug(trials):
    """
    Runs simulations and plots graphs for problem 4.
    Instantiates a patient, runs a simulation for 150 timesteps, adds
    guttagonol, and runs the simulation for an additional 150 timesteps.
    total virus population vs. time and guttagonol-resistant virus population
    vs. time are plotted
    """
    mean_num_virion = [100]
    mean_num_resist = [0]
    for i in range(300):
        mean_num_virion += [0,]
        mean_num_resist += [0,]
    res = {'gu':False}
    for i in range(trials):
        virion = []
        while len(virion) < 100:
            virion.append(ResistantVirus(0.1, 0.05, res, 0.005))
        simPatient = Patient(virion, 1000)
        call = 0
        while call < 150:
            call += 1
            simPatient.update()
            mean_num_virion[call] += simPatient.getTotalPop()/float(trials)
            mean_num_resist[call] += simPatient.getResistPop(['gu'])/float(trials)
        simPatient.addPrescription('gu')
        while call < 300:
            call += 1
            simPatient.update()
            mean_num_virion[call] += simPatient.getTotalPop()/float(trials)
            mean_num_resist[call] += simPatient.getResistPop(['gu'])/float(trials)
        print 'Trial ', i + 1, " complete."
    print "Producing plot"
    pylab.figure()
    pylab.plot(mean_num_virion)
    pylab.title('Virus Population in a Patient')
    pylab.xlabel('Timesteps')
    pylab.ylabel('Number of virion')
    pylab.savefig('Total Virion Population, 1 Drug')
    pylab.figure()
    pylab.plot(mean_num_resist)
    pylab.title('Resistant Virus Population in a Patient')
    pylab.xlabel('Timesteps')
    pylab.ylabel('Number of resistant virion')

# simulationWithDrug(50)
# pylab.show()


# PROBLEM 3

def simulationDelayedTreatment(trials):
    """
    Runs simulations and make histograms for problem 5.
    Runs multiple simulations to show the relationship between delayed treatment
    and patient outcome.
    Histograms of final total virus populations are displayed for delays of 300,
    150, 75, 0 timesteps (followed by an additional 150 timesteps of
    simulation).    
    """
    plots = []
    steps = [300, 150, 75, 0]
    for step in steps:
        final_virion = []
        res = {'gu':False}
        for i in range(trials):
            virion = []
            while len(virion) < 100:
                virion.append(ResistantVirus(0.1, 0.05, res, 0.005))
            simPatient = Patient(virion, 1000)
            call = 0
            while call < step:
                call += 1
                simPatient.update()
            simPatient.addPrescription('gu')
            while call < (step + 150):
                call += 1
                simPatient.update()
            final_virion += [simPatient.getTotalPop(),]
            print 'Trial ', i + 1, " for delay: ", step, " complete."
        plots.append(final_virion)
        print "Producing plot..."
    fig = pylab.figure()
    fig.add_subplot(111)
    pylab.hist(plots, 10, normed=1)                                 #Could use range= in this line to specify size of bins
    pylab.legend(['300', '150', '75', '0'], loc='best')
    fig.canvas.draw()
    pylab.show()


# simulationDelayedTreatment(20)



# PROBLEM 4

def simulationTwoDrugsDelayedTreatment(trials):
    """
    Runs simulations and make histograms for problem 6.
    Runs multiple simulations to show the relationship between administration
    of multiple drugs and patient outcome.
   
    Histograms of final total virus populations are displayed for lag times of
    150, 75, 0 timesteps between adding drugs (followed by an additional 150
    timesteps of simulation).
    """
    plots = []
    steps = [300, 150, 75, 0]
    for step in steps:
        final_virion = []
        res = {'gu':False, 'gr':False}
        for i in range(trials):
            virion = []
            while len(virion) < 100:
                virion.append(ResistantVirus(0.1, 0.05, res, 0.005))
            simPatient = Patient(virion, 1000)
            call = 0
            while call < 150:
                call += 1
                simPatient.update()
            simPatient.addPrescription('gu')
            while call < (step + 150):
                call += 1
                simPatient.update()
            simPatient.addPrescription('gr')
            while call < (step + 300):
                call += 1
                simPatient.update()
            final_virion += [simPatient.getTotalPop(),]
            print 'Trial ', i + 1, " for delay: ", step, " complete."
        plots.append(final_virion)
        print "Producing plot..."
    fig = pylab.figure()
    fig.add_subplot(111)
    pylab.hist(plots, 10, normed=1)
    pylab.legend(['300', '150', '75', '0'], loc='best')
    fig.canvas.draw()
    pylab.show()
    pylab.savefig('2 Drug: Virion Simulation with Variable Drug Delay Time')

# simulationTwoDrugsDelayedTreatment(30)


# PROBLEM 5


def simulationTwoDrugsVirusPopulations(trials, one, two):
    """
    Run simulations and plot graphs examining the relationship between
    administration of multiple drugs and patient outcome.
    Plots of total and drug-resistant viruses vs. time are made for a
    simulation with a 300 time step delay between administering the 2 drugs and
    a simulations for which drugs are administered simultaneously.

    one: represents timestep Gu is administered
    two: represents timestep Gr is administered
    trials: how many trials will be average to give the result
    """
    mean_num_virion = [100]
    mean_num_resist1 = [0]
    mean_num_resist2 = [0]
    mean_num_resist3 = [0]
    for i in range(two + 150):
        mean_num_virion += [0,]
        mean_num_resist1 += [0,]
        mean_num_resist2 += [0,]
        mean_num_resist3 += [0,]
    res = {'gu':False, 'gr':False}
    for i in range(trials):
        virion = []
        while len(virion) < 100:
            virion.append(ResistantVirus(0.1, 0.05, res, 0.005))
        simPatient = Patient(virion, 1000)
        call = 0
        n = 450
        while call < n:
            if call == one:
                simPatient.addPrescription('gu')
            if call == two:
                simPatient.addPrescription('gr')
                n = call + 150
            call += 1
            simPatient.update()
            mean_num_virion[call] += simPatient.getTotalPop()/float(trials)
            mean_num_resist1[call] += simPatient.getResistPop(['gu'])/float(trials)
            mean_num_resist2[call] += simPatient.getResistPop(['gr'])/float(trials)
            mean_num_resist3[call] += simPatient.getResistPop(['gu', 'gr'])/float(trials)
        print 'Trial ', i + 1, " complete."
    print "Producing plot"
    pylab.figure()
    pylab.plot(mean_num_virion)
    pylab.title('Virus Population in a Patient, 2 Drugs Gu/Gr Administered:' + str(one) + ', ' + str(two))
    pylab.xlabel('Timesteps')
    pylab.ylabel('Number of virion')
    # pylab.savefig('Total Virion Population, 2 Drug Gu/Gr')
    pylab.figure()
    pylab.plot(mean_num_resist1)
    pylab.title('Gu: Resistant Virus Population in a Patient, 2 Drugs Gu/Gr Administered:' + str(one) + ', ' + str(two))
    pylab.xlabel('Timesteps')
    pylab.ylabel('Number of resistant virion')
    # pylab.savefig('First: Total Resistant Virion Population, 2 Drug Gu/Gr')
    pylab.figure()
    pylab.plot(mean_num_resist2)
    pylab.title('Gr: Resistant Virus Population in a Patient, 2 Drugs Gu/Gr Administered:' + str(one) + ', ' + str(two))
    pylab.xlabel('Timesteps')
    pylab.ylabel('Number of resistant virion')
    # pylab.savefig('Second: Total Resistant Virion Population, 2 Drug Gu/Gr')
    pylab.figure()
    pylab.plot(mean_num_resist3)
    pylab.title('Gu + Gr: Resistant Virus Population in a Patient, 2 Drugs Gu/Gr Administered:' + str(one) + ', ' + str(two))
    pylab.xlabel('Timesteps')
    pylab.ylabel('Number of resistant virion')
    # pylab.savefig('Both: Total Resistant Virion Population, 2 Drug Gu/Gr')
    # pylab.show()

# simulationTwoDrugsVirusPopulations(500, 150, 300)
# simulationTwoDrugsVirusPopulations(500, 150, 150)
# pylab.show()



#6 Non-compliance:

    #If they forget to take their drugs than you would have to add a segment to the code based on an estimate of how often this happens
    #Every so often, therefore, cells that do not have resistance to the forgotten drug would replicate (cells that are normally in stasis)
