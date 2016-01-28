__author__ = 'paulsalvatore57'
import random
from ps7 import *
import matplotlib.pylab as pylab

class ResistantVirus(SimpleVirus):
    def __init__(self, maxBirthProb, clearProb, resistances, mutProb):
        self.maxBirthProb = maxBirthProb
        self.clearProb = clearProb
        self.resistances = resistances
        self.mutProb = mutProb

    def isResistantTo(self, drug):
        return self.resistances[drug]

    def reproduce(self, popDensity):
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
    def __init__(self, viruses, maxPop):
        self.viruses = viruses
        self.maxPop = maxPop
        self.drugs = []

    def addPrescription(self, newDrug):
        if newDrug not in self.drugs:
            self.drugs.append(newDrug)

    def getPrescriptions(self):
        return self.drugs

    def getResistPop(self, drugResist):
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

def simulationWithDrug(trials):

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
    pylab.title('Virus Population in a Simple Patient')
    pylab.xlabel('Timesteps')
    pylab.ylabel('Number of virion')
    pylab.savefig('Total Virion Population, 1 Drug')
    pylab.figure()
    pylab.plot(mean_num_resist)
    pylab.title('Resistant Virus Population in a Simple Patient')
    pylab.xlabel('Timesteps')
    pylab.ylabel('Number of resistant virion')
    pylab.savefig('Resistant Virion Population, 1 Drug')



def simulationDelayedTreatment(trials):
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
    pylab.hist(plots, 10, normed=1)
    pylab.legend(['300', '150', '75', '0'], loc='best')
    fig.canvas.draw()
    pylab.show()
    # pylab.savefig('Virion Simulation with Variable Drug Delay Time')


# simulationDelayedTreatment(10)











#OLD CODE BEFORE I ADDED VARIABLE DRUG TREATMENT TIME (also bulky)
def simulationTwoDrugsVirusPopulations(trials):
    """
    Run simulations and plot graphs examining the relationship between
    administration of multiple drugs and patient outcome.
    Plots of total and drug-resistant viruses vs. time are made for a
    simulation with a 300 time step delay between administering the 2 drugs and
    a simulations for which drugs are administered simultaneously.
    """
    mean_num_virion = [100]
    mean_num_resist1 = [0]
    mean_num_resist2 = [0]
    mean_num_resist3 = [0]
    for i in range(450):
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
        while call < 150:
            call += 1
            simPatient.update()
            mean_num_virion[call] += simPatient.getTotalPop()/float(trials)
            mean_num_resist1[call] += simPatient.getResistPop(['gu'])/float(trials)
            mean_num_resist2[call] += simPatient.getResistPop(['gr'])/float(trials)
            mean_num_resist3[call] += simPatient.getResistPop(['gu', 'gr'])/float(trials)
        while call < 300:
            call += 1
            simPatient.update()
            mean_num_virion[call] += simPatient.getTotalPop()/float(trials)
            mean_num_resist1[call] += simPatient.getResistPop(['gu'])/float(trials)
            mean_num_resist2[call] += simPatient.getResistPop(['gr'])/float(trials)
            mean_num_resist3[call] += simPatient.getResistPop(['gu', 'gr'])/float(trials)
        simPatient.addPrescription('gr')
        while call < 450:
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
    pylab.title('Virus Population in a Patient, 2 Drugs')
    pylab.xlabel('Timesteps')
    pylab.ylabel('Number of virion')
    # pylab.savefig('Total Virion Population, 2 Drug')
    pylab.figure()
    pylab.plot(mean_num_resist1)
    pylab.title('Gu: Resistant Virus Population in a Patient, 2 Drugs')
    pylab.xlabel('Timesteps')
    pylab.ylabel('Number of resistant virion')
    # pylab.savefig('First: Total Resistant Virion Population, 2 Drug')
    pylab.figure()
    pylab.plot(mean_num_resist2)
    pylab.title('Gr: Resistant Virus Population in a Patient, 2 Drugs')
    pylab.xlabel('Timesteps')
    pylab.ylabel('Number of resistant virion')
    # pylab.savefig('Second: Total Resistant Virion Population, 2 Drug')
    pylab.figure()
    pylab.plot(mean_num_resist3)
    pylab.title('Gu + Gr: Resistant Virus Population in a Patient, 2 Drugs')
    pylab.xlabel('Timesteps')
    pylab.ylabel('Number of resistant virion')
    # pylab.savefig('Both: Total Resistant Virion Population, 2 Drug')
    pylab.show()