__author__ = 'paulsalvatore57'


                #15 - Statistical Thinking

#How many samples do we need before we can have confidence in the result?

#VARIANCE: measure of how much spread is available in the possible outcomes
    #There needs to be multiple trials with different outcomes (to see the difference between the outcomes)

#STANDARD DEVIATION: the fraction of values that are close to the mean (see bulletin board for formula)
    #If many values are close to the mean, SD is small


def stdDev(X):
    mean = sum(X)/float(len(X))
    tot = 0.0
    for x in X:
        tot += (x - mean)**2
    return (tot/len(X))**0.5


import random
import matplotlib.pylab

def flipPlot(minExp, maxExp, numTrials):
    meanRatios = []
    meanDiffs = []
    ratiosSDs = []
    diffsSDs = []
    xAxis = []
    for exp in range(minExp, maxExp + 1):
        xAxis.append(2**exp)
    for numFlips in xAxis:
        ratios = []
        diffs = []
        for t in range(numTrials):
            numHeads = 0
            for n in range(numFlips):
                if random.random() < 0.5:
                    numHeads += 1
            numTails = numFlips - numHeads
            ratios.append(numHeads/float(numTails))
            diffs.append(abs(numHeads - numTails))
        meanRatios.append(sum(ratios)/numTrials)
        meanDiffs.append(sum(diffs)/numTrials)
        ratiosSDs.append(stdDev(ratios))
        diffsSDs.append(stdDev(diffs))
    matplotlib.pylab.plot(xAxis, meanRatios, 'bo')
    matplotlib.pylab.title('Mean Heads/Tails Ratios ('
                + str(numTrials) + ' Trials)')
    matplotlib.pylab.xlabel('Number of Flips')
    matplotlib.pylab.ylabel('Mean Heads/Tails')
    matplotlib.pylab.semilogx()

    matplotlib.pylab.figure()
    matplotlib.pylab.title('Mean abs(#Heads - #Tails) ('
                + str(numTrials) + ' Trials)')
    matplotlib.pylab.xlabel('Number of Flips')
    matplotlib.pylab.ylabel('Mean abs(#Heads - #Tails')
    matplotlib.pylab.plot(xAxis, meanDiffs, 'bo')
    matplotlib.pylab.semilogx()                             #Looking at different powers so we need semilog scale
    matplotlib.pylab.semilogy()

    matplotlib.pylab.figure()
    matplotlib.pylab.title('SD Heads/Tails Ratios) ('
                + str(numTrials) + ' Trials)')
    matplotlib.pylab.xlabel('Number of Flips')
    matplotlib.pylab.ylabel('Standard Deviation')
    matplotlib.pylab.plot(xAxis, ratiosSDs, 'bo')
    matplotlib.pylab.semilogx()                             #Looking at different powers so we need semilog scale
    matplotlib.pylab.semilogy()

    matplotlib.pylab.figure()
    matplotlib.pylab.title('SD abs(#Heads - #Tails) ('
                + str(numTrials) + ' Trials)')
    matplotlib.pylab.xlabel('Number of Flips')
    matplotlib.pylab.ylabel('Standard Deviation')
    matplotlib.pylab.plot(xAxis, diffsSDs, 'bo')
    matplotlib.pylab.semilogx()                             #Looking at different powers so we need semilog scale
    matplotlib.pylab.semilogy()
    matplotlib.pylab.show()

# flipPlot(4, 20, 20)



#As number of flips increases, the standard deviation is decreasing steadily
#This makes sense because variance is decreasing with an increasing number of trials (more indicative of the truth)
    #Better reason to believe that we have the correct answer with smaller SD

#Is the SD RELATIVELY large or small? Packing around the mean.



#COEFFICIENT OF VARIATION: the SD/mean, this lets us relate different data sets with different means and how much they vary relative to each other
#           <1, low variance

#If mean is NEAR 0, small changes in the mean lead to large change sin coefficient of variation (not meaningful)
#Coefficient of variation cannot be used to construct confidence intervals (unlike SD)






def flip(numFlips):
    heads = 0
    for i in range(numFlips):
        if random.random() < 0.5:
            heads += 1
    return heads/float(numFlips)


def flipSim(numFlipsPerTrial, numTrials):
    fracHeads = []
    for i in range(numTrials):
        fracHeads.append(flip(numFlipsPerTrial))
    return fracHeads


def labelPlot(nf, nt, mean, sd):
    matplotlib.pylab.title(str(nt) + ' trials of '
                + str(nf) + ' flips each')
    matplotlib.pylab.xlabel('Fraction of Heads')
    matplotlib.pylab.ylabel('Number of Trials')
    xmin, xmax = matplotlib.pylab.xlim()
    ymin, ymax = matplotlib.pylab.ylim()
    matplotlib.pylab.text(xmin + (xmax-xmin)*0.02, (ymax-ymin)/2,
               'Mean = ' + str(round(mean, 6))
               + '\nSD = ' + str(round(sd, 6)))


def makePlots(nf1, nf2, nt):
    """nt = number of trials per experiment
       nf1 = number of flips 1st experiment
       nf2 = number of flips 2nd experiment"""
    fracHeads1 = flipSim(nf1, nt)
    mean1 = sum(fracHeads1)/float(len(fracHeads1))
    sd1 = stdDev(fracHeads1)
    matplotlib.pylab.hist(fracHeads1, bins = 20)
    xmin,xmax = matplotlib.pylab.xlim()
    ymin,ymax = matplotlib.pylab.ylim()
#If you call xlim() with no arguments it returns the current minimum x or y value of the current figure/plot
#So we have stored the current minimum values
    labelPlot(nf1, nt, mean1, sd1)
    # matplotlib.pylab.savefig('First flips histogram')

    matplotlib.pylab.figure()
    fracHeads2 = flipSim(nf2, nt)
    mean2 = sum(fracHeads2)/float(len(fracHeads2))
    sd2 = stdDev(fracHeads2)
    matplotlib.pylab.hist(fracHeads2, bins = 20)
    matplotlib.pylab.hist(fracHeads2, bins = 20)
#Plotting a histogram, so we give it a set of values and a number of bins in which to make the histogram
    matplotlib.pylab.xlim (xmin, xmax)
#Setting the x lim to the ones previously saved (so that we can compare the two graphs)
    ymin, ymax = matplotlib.pylab.ylim()
    labelPlot(nf2, nt, mean2, sd2)
    # matplotlib.pylab.savefig('Second flips histogram')




#Indepedent histogram example:
# L = [1, 2, 3, 3, 3, 4]
# L = [1, 2, 3, 3, 3, 4, 60]
# matplotlib.pylab.hist(L, bins = 6)
# matplotlib.pylab.show()


# makePlots(100, 1000, 100000)
# matplotlib.pylab.show()

#When we see the spread in the 1000 flip example being much lower this is because we used xlim()
    #Wouldn't have looked tighter since the blank space wouldn't have been displayed; we maid the axis the same length








        #STATISTICAL INFORMATION


#NORMAL DISTRIBUTION: always peaks at the mean, and falls off symmetrically (essentially); bell curve
    #More trials of our example will converge on the normal distribution


    #1. Have nice mathematical properties
        #Can be completely characterized by two parameters: SD and mean (know the entire distribution)
        #SD and mean can be used to compute confidence intervals

            #CONFIDENCE INTERVALS allow us to estimate unknown parameter by providing a range that that contains the unknown value,
            #and the confidence that the value lies in that range (CONFIDENCE LEVEL)

            #So 56 +/- 4 means that 95% of the time the value will lie between 52 and 60 (if not stated confidence is usually 95%)
            #ASSUME random trials with normal distribution

            #EMPIRICAL RULE: If we have a true normal distribution, than 68% of data is within 1 SD of the mean, 95% within 2 SDs, 99.7% within 3 SDs

            #STANDARD ERROR (SE): estimate of SD, assumes errors are normal distributed and that the sample population is small relative to actual population

                #p = %sampled
                #n = sample size
                #SE = (p * (100 - p) / n )^0.5


#If we think someone will win 46% of votes after polling 1000 people, we can compute SE = 1.56 %
    #Interpreted to mean tht at 95% confidence true percentage of votes is within 2 SE of 46%

def poll(n, p):
    votes = 0.0
    for i in range(n):
        if random.random() < p/100.0:
            votes += 1
    return votes

def testErr(n = 1000, p = 46.0, numTrials = 1000):
    results = []
    for t in range(numTrials):
        results.append(poll(n, p))
    print 'std = ' + str((stdDev(results)/n)*100) + '%'
    results = matplotlib.pylab.array(results)/n
    matplotlib.pylab.hist(results)
    matplotlib.pylab.xlabel('Fraction of Votes')
    matplotlib.pylab.ylabel('Number of Polls')

# testErr()
# matplotlib.pylab.show()

#Because differences are normally distributed SE guess of 1.56% is very close to the SD calculated of 1.61% (good approximation)






    #2. Many naturally occurring instances
        #Results are often normally distributed
        #Examples of heights and weights for populations

        #Many experimental setups have normally distributed errors for measurements (most of science assumes normal distributions)







