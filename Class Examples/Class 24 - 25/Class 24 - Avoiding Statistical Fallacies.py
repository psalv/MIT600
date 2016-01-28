__author__ = 'paulsalvatore57'


            #24 - Avoiding Statistical Fallacies



#1) Statisitcal measures do not tell the whole story.

    #In anscombe's example there are multiple datasets that have very similar conclusions that can be drawn:
        #i.e. mean, median, linear regressional fit, variance, etc.

    #The code below reads in the datasets and plots a few things (in which the graphs will all be identical).

    #Is it true that the data is identical? We can answer this question by plotting the actual datapoints.
        #When this is done we see fairly dramatic differences between the datasets.


    #Don't have the dataset used:

import random
import matplotlib.pylab as pylab
def anscombe(plotPoints):
    dataFile = open('anscombe.txt', 'r')
    X1,X2,X3,X4,Y1,Y2,Y3,Y4 = [],[],[],[],[],[],[],[]
    for line in dataFile:
        x1,y1,x2,y2,x3,y3,x4,y4 = line.split()
        X1.append(float(x1))
        X2.append(float(x2))
        X3.append(float(x3))
        X4.append(float(x4))
        Y1.append(float(y1))
        Y2.append(float(y2))
        Y3.append(float(y3))
        Y4.append(float(y4))
    dataFile.close()
    xVals = pylab.array(range(21))
    if plotPoints: pylab.plot(X1, Y1, 'o')
    a, b = pylab.polyfit(X1, Y1, 1)
    yVals = a*xVals + b
    pylab.plot(xVals, yVals)
    pylab.xlim(0, 20)
    mean = sum(Y1)/float(len(Y1))
    median = Y1[len(Y1)/2 + 1]
    pylab.title('Mean = ' + str(mean) + ', Median = ' + str(median))
    pylab.figure()
    if plotPoints: pylab.plot(X2, Y2, 'o')
    a, b = pylab.polyfit(X2, Y2, 1)
    yVals = a*xVals + b
    pylab.plot(xVals, yVals)
    pylab.xlim(0, 20)
    mean = sum(Y1)/float(len(Y1))
    median = Y1[len(Y1)/2 + 1]
    pylab.title('Mean = ' + str(mean) + ', Median = ' + str(median))
    pylab.figure()
    if plotPoints: pylab.plot(X3, Y3, 'o')
    a, b = pylab.polyfit(X3, Y3, 1)
    yVals = a*xVals + b
    pylab.plot(xVals, yVals)
    pylab.xlim(0, 20)
    mean = sum(Y1)/float(len(Y1))
    median = Y1[len(Y1)/2 + 1]
    pylab.title('Mean = ' + str(mean) + ', Median = ' + str(median))
    pylab.figure()
    if plotPoints: pylab.plot(X4, Y4, 'o')
    a, b = pylab.polyfit(X4, Y4, 1)
    yVals = a*xVals + b
    pylab.plot(xVals, yVals)
    pylab.xlim(0, 20)
    mean = sum(Y1)/float(len(Y1))
    median = Y1[len(Y1)/2 + 1]
    pylab.title('Mean = ' + str(mean) + ', Median = ' + str(median))
    pylab.show()
##anscombe(True)

    #The point is that you can never ignore the data: must find a way to analyze the datapoints themselves.



#2) Pictures can be deceiving.

    #The axes are of particular importance to this, since something such as a logarithmic scale could conceal results.
    #Both the x and y axes are important in these considerations.



#3) Garbage in, garbage out (GIGO)

    #Example given was slavery and insanity where free blacks were 10 times more likely to go insane.
        #The point he made to try and unjustify this is that if measurement errors are UNBIASED and independent of each other,
        #then they are expected to be almost identically distributed on either side othe mean.

        #The big assumption made is that they are independent of each other when in this scenario this is not true.



#4) Cum hoc ergo propter hoc fallacy

    # "With this, therefore the cause of this"

    #We like to assume causality but correlation does not mean causality
        #Gave example of people who go to class getting higher grades, but hat may be because people who come to class also do the problem sets.

    #LURKING VARIABLE: is there a variable related to the other two that has not been considered
        #Ex. of flu cases correlating with people goign back to school, but school season is off during summer (flu virus less active in summer)


#4) Non-response bias, non-representative sample

    #Sampling a subset of a population allows us to infer things about the population as a whole: only true for samples representative of the whole population.

    #Many psychological sampling uses convenience sampling (whatever is easiest, often use undergraduates).

    #Non-response bias occurs when you do some form of survey and a group does not respond.
        #Gave WWII example of reinforcing planes based on where they were hit, but they only sample the planes that were not destroyed (therefore biasing the sample).




#Internet usage in the US as a percent of the population:

def internet(points):
    years = pylab.array(range(1994, 2001))
    percent = [4.9,9.4,16.7,22,30.7, 36.6, 43.9]
    pylab.plot(years,percent)
    a, b = pylab.polyfit(years, percent, 1)
    yvals = a*pylab.array(years) + b
    pylab.plot(years, yvals)
    pylab.title('Internet Usage in the United States')
    pylab.xlabel('Year')
    pylab.ylabel('% of Population')
    if points:
        pylab.figure()
        pylab.plot(years, percent, 'o')
        xvals = pylab.array(range(1994, 2011))
        yvals = a*xvals + b
        pylab.plot(xvals, yvals)
        pylab.title('Projected Internet Usage in the United States')
        pylab.xlabel('Year')
        pylab.ylabel('% of Population')
    pylab.show()

# internet(True)

#Used this to extrapolate internet usage going forward, just doesn't make sense to do this (linear data won't necessarily continue it's trend).

#5) Texas sharp shooter fallacy

    #Driving in Texas and find a barn with 6 targets, each with a bullet hold dead center in it.
    #You say "you're good", his wife says "he is with a paint gun".
    #He shot first, then painted the targets around them afterwards.

    #Example of this: team studies 447 women diagnosed as anorexic.
        # On average 37 should be born each month.
        # In June there were 48, so how likely is this? The code below checks this.

def juneProb(numTrials):
    june48 = 0.0
    for trial in range(numTrials):
        june = 0.0
        for i in range(446):
            if random.choice(range(1,13)) == 6:
                june += 1.0
        if june >= 48:
            june48 += 1
    juneProb = str(june48/numTrials)
    print 'Probability of at least 48 births in June = ' + juneProb

# juneProb(1000)

    #The probability of this happening by chance turns out to be pretty low.

    #The thing is, that the researchers did not start with the hypothesis that more anorexic women are born in June and conducted a prospective study.
    #They instead looked at the data and found a hypothesis that matches the data.

    #What they should actually be asking is not what the probability of 48 of the anorexics being born in June, but in at least one of the 12 months.
    #Therefor we should run the below simulation:

def anyProb(numTrials):
    anyMonth = 0.0
    for trial in range(numTrials):
        months = [0.0]*13
        for i in range(446):
            months[random.choice(range(1,13))] += 1
        if max(months) >= 48:
            anyMonth += 1
    aProb = str(anyMonth/numTrials)
    print 'Probability of at least 48 births in some Month = ' + aProb

# anyProb(1000)

    #This returns a much higher probability (over 40% rather than 4%). This makes the data unmeaningful.
