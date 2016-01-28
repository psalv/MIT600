__author__ = 'paulsalvatore57'


                    #17 - Curve Fitting



#Look into downloading Anaconda

#From last lecture saying that we are 95% certain that pi lies within the SD (when it is small) is not true
    #Statistically sound conclusions are not necessarily models of reality
        #For instance if we miswrote the program it would still converge with statistical accuracy, but just to the wrong number

#Need to have confidence that conceptual model is correct, and that we have correctly implemented it
    #Can experimentally test the results to verify them

#Physical Reality vs Theoretical Model vs Computational Simulation

#We need to model experimental error, which typical has a normal distribution




#Spring example:

    #Hook's law: f = -kx        < force stored in the spring is linearly related to x, the distance the spring has been stretched
    #Can attach a weight to a spring, measure stretching (k = m*g, where g = 9.8m/s^2 and m = mass of weight), therefore determining the stored force

import math
import matplotlib.pylab

def getData(fileName):
    dataFile = open(fileName, 'r')
    distances = []
    masses = []
    discardHeader = dataFile.readline()
    for line in dataFile:
        d, m = line.split()
        distances.append(float(d))
        masses.append(float(m))
    dataFile.close()
    return (masses, distances)

def plotData(fileName):
    xVals, yVals = getData(fileName)            #Use this SLIT to get the x and y values (works for any number of variables and a list of the same length)
    xVals = matplotlib.pylab.ary(xVals)       #Can do point wise operations on an array, so if you multiply an array by 3, each element is multiplied by 3
    yVals = matplotlib.pylab.array(yVals)           #Multiply one array by another than does a crossproduct (often build up lists, than operations with arrays)
    # xVals *= 9.81
    xVals = xVals*9.81  #acc. due to gravity
    matplotlib.pylab.plot(xVals, yVals, 'bo', label = 'Measured displacements')
    matplotlib.pylab.title('Measured Displacement of Spring')
    matplotlib.pylab.xlabel('|Force| (Newtons)')
    matplotlib.pylab.ylabel('Distance (meters)')

# plotData('/Users/paulsalvatore57/PycharmProjects/MIT600/Class Examples/Class 16 - 17/springData.txt')
# matplotlib.pylab.show()



#Theoretical model states that the data should fall on a line, if we know this line we can compute k (slope of line is inverse of k)
    #What line is the best fit? Need an objective fxn telling us how good the fits are
        #My guess is the line that minimizes the distance between the points and the lines

#LEAST-SQUARES FIT: objective function used for fitting curves          >>> LINEAR REGRESSION
    #Sum of (observed - predict)**2 at each point, and we want to minimize this number

    #In our model for every x value, a y value will be predicted
        #Measure difference between predicted and observed, squared (to make the value positive, above or below does not matter)
        #Smaller the sum, better the fit



#This function is built into pylab > polyfit(observed x values, observed y values, degree of polynomial)


def fitData(fileName):
    xVals, yVals = getData(fileName)
    # xVals = matplotlib.pylab.array(xVals)
    xVals = matplotlib.pylab.array(xVals[:-6])  #This code is to eliminate the last six points (that appear to be flat lining)
    # yVals = matplotlib.pylab.array(yVals)
    yVals = matplotlib.pylab.array(yVals[:-6])
    xVals = xVals*9.81
    matplotlib.pylab.plot(xVals, yVals, 'bo', label = 'Measured displacements')     #Note the label and 'bo' (blue) included in the plot code
    matplotlib.pylab.title('Measured Displacement of Spring')
    matplotlib.pylab.xlabel('|Force| (Newtons)')
    matplotlib.pylab.ylabel('Distance (meters)')
    a,b = matplotlib.pylab.polyfit(xVals, yVals, 1)                 #Find the a and b values of the equation
    estYVals = a*matplotlib.pylab.array(xVals) + b                     #Compute the estimated y values (using an array for iteration over a list)
    k = 1/a
    matplotlib.pylab.plot(xVals, estYVals, label = 'Linear fit, k = ' + str(round(k, 5)))   #Plot it and can compute k; also ROUND function that I have never seen before
    matplotlib.pylab.legend(loc = 'best')

# fitData('/Users/paulsalvatore57/PycharmProjects/MIT600/Class Examples/Class 16 - 17/springData.txt')
# matplotlib.pylab.show()



def fitData_cubic(fileName):
    xVals, yVals = getData(fileName)
    xVals = matplotlib.pylab.array(xVals)
    yVals = matplotlib.pylab.array(yVals)
    xVals = xVals*9.81
    matplotlib.pylab.plot(xVals, yVals, 'bo', label = 'Measured displacements')
    matplotlib.pylab.title('Measured Displacement of Spring')
    matplotlib.pylab.xlabel('|Force| (Newtons)')
    matplotlib.pylab.ylabel('Distance (meters)')
    a,b = matplotlib.pylab.polyfit(xVals, yVals, 1)
    estYVals = a*matplotlib.pylab.array(xVals) + b

    ##Cubic fit instead of linear
    # matplotlib.pylab.plot(xVals, estYVals, label = 'Linear fit')
    a,b,c,d = matplotlib.pylab.polyfit(xVals, yVals, 3)
    estYVals = a*matplotlib.pylab.array(xVals)**3 + b*matplotlib.pylab.array(xVals)**2 + c*matplotlib.pylab.array(xVals) + d
    k = 1/a
    matplotlib.pylab.plot(xVals, estYVals, label = 'Cubic fit')
    matplotlib.pylab.legend(loc = 'best')


#After you've fit your line you need to look at the graph, is it accurate?
    #Cubic fits the system better, but we are using it to predict experiments that we cannot run



    #USNG A LIN EOF BEST FIT FOR PREDICTIONS

def fitData_predict(fileName):
    xVals, yVals = getData(fileName)
    extX = matplotlib.pylab.array(xVals + [1.5])
    xVals = matplotlib.pylab.array(xVals)        #We have added a point for prediction purposes
    yVals = matplotlib.pylab.array(yVals)
    xVals = xVals*9.81
    extX *= 9.81
    matplotlib.pylab.plot(xVals, yVals, 'bo', label = 'Measured displacements')
    matplotlib.pylab.title('Measured Displacement of Spring')
    matplotlib.pylab.xlabel('|Force| (Newtons)')
    matplotlib.pylab.ylabel('Distance (meters)')
    a,b = matplotlib.pylab.polyfit(xVals, yVals, 1)
    extY = a*matplotlib.pylab.array(extX) + b
    matplotlib.pylab.plot(extX, extY, label = 'Linear fit')
    a,b,c,d = matplotlib.pylab.polyfit(xVals, yVals, 3)
    extY = a*(extX)**3 + b*(extX)**2 + c*(extX) + d
    k = 1/a
    matplotlib.pylab.plot(extX, extY, label = 'Cubic fit')
    matplotlib.pylab.legend(loc = 'best')

# fitData_predict('/Users/paulsalvatore57/PycharmProjects/MIT600/Class Examples/Class 16 - 17/springData.txt')
# matplotlib.pylab.show()

#This prediction is not feasible in a physical world: Although you can fit a curve easily to this data, it has bad predictive data
#Because our data doesn't fit theory doesn't mean we should fit an arbitrary curve and see what happens


#We need to look at the raw data: looks like the spring is flattening out which means the elastic limit of the spring has been exceeded.
    #We go back and discard the last six points wherein the spring appears to have flat lined

#We get a visually much better fit, and a different value for k
    #We have to go back to the theory to justify removing the last 6 points; statistics can only take us so far, need to be backed by theory



#BOW AND ARROW EXAMPLE:

def getTrajData(file):
    file = open(file, 'r')
    distances = []
    h1, h2, h3, h4 = [],[],[],[]
    discardHeader = file.readline()
    for line in file:
        d, ht1, ht2, ht3, ht4 = line.split()
        distances.append(float(d))
        h1.append(float(ht1))
        h2.append(float(ht2))
        h3.append(float(ht3))
        h4.append(float(ht4))
    file.close()
    return(distances, [h1, h2, h3, h4])


def tryFits(fName):
    distances, heights = getTrajData(fName)
    distances = matplotlib.pylab.array(distances)*36
    totHeights = matplotlib.pylab.array([0]*len(distances))
    for h in heights:
        totHeights = totHeights + matplotlib.pylab.array(h)
    matplotlib.pylab.title('Trajectory of Projectile (Mean of 4 Trials)')
    matplotlib.pylab.xlabel('Inches from Launch Point')
    matplotlib.pylab.ylabel('Inches Above Launch Point')
    meanHeights = totHeights/float(len(heights))
    matplotlib.pylab.plot(distances, meanHeights, 'bo')
    a,b = matplotlib.pylab.polyfit(distances, meanHeights, 1)
    altitudes = a*distances + b
    matplotlib.pylab.plot(distances, altitudes, 'r',
               label = 'Linear Fit')
    a,b,c = matplotlib.pylab.polyfit(distances, meanHeights, 2)
    altitudes = a*(distances**2) + b*distances + c
    matplotlib.pylab.plot(distances, altitudes, 'g',
               label = 'Quadratic Fit')
    matplotlib.pylab.legend()

# tryFits('/Users/paulsalvatore57/PycharmProjects/MIT600/Class Examples/Class 16 - 17/launcherData.txt')
# matplotlib.pylab.show()


#Fit of degree 2 is visually better, but how much better? Polyfit uses least mean squared, so we can compare these values
    #Mean squared error can't, however tell us how good the fit is in itself (no upper bound, can go infinitely high)





#We use COEFFICIENT OF DETERMINATION, or r**2 = 1 - EE/MV  (estimated error - variance in measured data) >> This value is always between 0 and 1

def rSquare(measured, estimated):
    """measured: one dimensional array of measured values
       estimate: one dimensional array of predicted values"""
    EE = ((estimated - measured)**2).sum()
    mMean = measured.sum()/float(len(measured))
    MV = ((mMean - measured)**2).sum()
    return 1 - EE/MV


def tryFits1(fName):
    distances, heights = getTrajData(fName)
    distances = matplotlib.pylab.array(distances)*36
    totHeights = matplotlib.pylab.array([0]*len(distances))
    for h in heights:
        totHeights = totHeights + matplotlib.pylab.array(h)
    matplotlib.pylab.title('Trajectory of Projectile (Mean of 4 Trials)')
    matplotlib.pylab.xlabel('Inches from Launch Point')
    matplotlib.pylab.ylabel('Inches Above Launch Point')
    meanHeights = totHeights/float(len(heights))
    matplotlib.pylab.plot(distances, meanHeights, 'bo')
    a,b = matplotlib.pylab.polyfit(distances, meanHeights, 1)
    altitudes = a*distances + b
    matplotlib.pylab.plot(distances, altitudes, 'r',
               label = 'Linear Fit' + ', R2 = '
               + str(round(rSquare(meanHeights, altitudes), 4)))
    a,b,c = matplotlib.pylab.polyfit(distances, meanHeights, 2)
    altitudes = a*(distances**2) + b*distances + c
    matplotlib.pylab.plot(distances, altitudes, 'g',
               label = 'Quadratic Fit' + ', R2 = '
               + str(round(rSquare(meanHeights, altitudes), 4)))
    matplotlib.pylab.legend()

tryFits1('/Users/paulsalvatore57/PycharmProjects/MIT600/Class Examples/Class 16 - 17/launcherData.txt')
matplotlib.pylab.show()


#I have learned that "import matplotlib.pylab as pylab" will allow me to stop having to add matplotlib. before every instance of pylab
    #This is incredibly helpful since adding the class was getting annoying
