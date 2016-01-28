__author__ = 'paulsalvatore57'
import random

class SimpleVirus(object):

    def __init__(self, maxBirthProb, clearProb):
        self.maxBirthProb = maxBirthProb
        self.clearProb = clearProb

    def doesClear(self):
        return random.random() <= self.clearProb

    def reproduce(self, popDensity):
        if random.random() <= self.maxBirthProb*(1 - popDensity):
            return SimpleVirus(self.maxBirthProb, self.clearProb)

class SimplePatient(object):

    def __init__(self, viruses, maxPop):
        self.viruses = viruses
        self.maxPop = maxPop

    def getTotalPop(self):
        return len(self.viruses)

    def update(self):
        newvirion = []
        for i in self.viruses:
            if i.doesClear():
                self.viruses.remove(i)
        popDensity = (len(self.viruses))/float(self.maxPop)

        for i in self.viruses:
            temp = i.reproduce(popDensity)
            if temp != None:
                newvirion += [temp,]
        for i in newvirion:
            self.viruses += [i,]
        return len(self.viruses)


# x = SimplePatient([SimpleVirus(0.9, 0.05)], 300)
# calls = 0
# while x.getTotalPop() < 200:
#     x.update()
#     calls += 1
# print calls


def simulationWithoutDrug(trials):
    """
    Doesn't account for multiple trials, this is a single simulation.
    """
    virion = []
    while len(virion) < 100:
        virion += [SimpleVirus(0.1, 0.05),]
    patient = SimplePatient(virion, 1000)
    num_virion = []
    num_virion += [len(virion),]
    call = 0
    while call < 300:
        patient.update()
        num_virion += [patient.getTotalPop(),]
        call += 1
    matplotlib.pylab.plot(num_virion)
    matplotlib.pylab.title('Virus Population in a Simple Patient')
    matplotlib.pylab.xlabel('Timesteps')
    matplotlib.pylab.ylabel('Number of virion')
    matplotlib.pylab.show()




