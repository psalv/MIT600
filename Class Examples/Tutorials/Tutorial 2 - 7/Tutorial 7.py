__author__ = 'paulsalvatore57'

import math
import random
# import matplotlib.pylab as pylab

            #DISTRIBUTIONS, MONTE CARLO SIMULATIONS, AND REGRESSION



###Uniform distribution (horizontal line on a histogram)

def unDis(a, b, num_points):
    points = []
    for n in range(num_points):
        points.append(random.randint(a, b))
    pylab.figure()
    pylab.hist(points, 100, normed = True)
    #This gives  the proportion of points that wind up in a particular bin rathr than raw frequency counts
    pylab.title('Discrete uniform distribution with ' + str(num_points) + ' points')
    pylab.show()
# unDis(1, 100, 100000)

def unDisContinuous(a, b, num_points):
    points = []
    for n in range(num_points):
        points.append(random.uniform(a, b))
        #Uniform command is used for random continuous values
    pylab.figure()
    pylab.hist(points, 100, normed = True)
    pylab.title('Continuous uniform distribution with ' + str(num_points) + ' points')
    pylab.show()
# unDisContinuous(0, 1.0, 100000)




####Normal distribution (peak at mean, bell curve)
    #SD and mean can fully define a normal distribution


def make_gaus(mean, SD, num_points):
    points = []
    for n in range(num_points):
        points.append(random.gauss(mean, SD))
        #Random in a Gausian distribution
    pylab.figure()
    pylab.hist(points, 100, normed=True)

    pylab.legend(['Random points'])
    pylab.title('Gausian distribution')
    pylab.show()

# make_gaus(0, 1, 100000)





###Monte Carlo Methods: arrive at a solution by random sampling

    #Monte Hall problem:

def door():
    return random.choice([1, 2, 3])

def MHALL(trials):
    stay = 0
    change = 0
    for n in range(trials):
        prize_door = door()
        player_door = door()
        if prize_door == player_door:
            stay += 1
        else:
            change += 1
    pylab.figure()
    pylab.pie([stay, change], labels=(['Stay', 'Change']), autopct = '%.2f%%')
    pylab.show()
# MHALL(100000)

#When I was attempting this problem myself I was over complicating it, the only question is stay or change, the number are irrelevant



#In the pi example what we are doing is dropping pins randomly in a square
    #We find the distance from the center that these are, if they are further than the radius than they are not in the circle
    #The number of pins within the circle/num of pins * 4 should be equivalent to pi


def drop_pin():
    return [random.random(), random.random()]

def in_circle(x, y):
    if math.sqrt(x**2 + y**2) <= 1:
        return True
    else:
        return False

def pin_sim(trials):
    within = 0
    outside = 0
    for n in range(trials):
        x, y = drop_pin()
        if in_circle(x, y):
            within += 1
        else:
            outside += 1
    return float(within)/trials * 4

# print pin_sim(100000)

#Can plot the actual points to show how the distribution begins to get better with more trials > pylab.scatter()







#Integration of a polynomial by Monte Carlo Method:

def frange(start, stop, step):
    """
    Returns a range with custom steps
    """
    l = []
    for i in range(int((stop-start)/step)):
        l.append(start + step*i)
    return l

#If we have a function bordered by two bounds (x values), than we can use the same idea (number of points that land beneath the curve) to integrate the function

def find_fxn(f, min, max, xstep = 0.001):
    """
    Finds y bounds of fxn
    """
    ymin = None
    ymax = None
    for x in frange(min, max, xstep):
        f_y = f(x)
        if ymin is None or f_y < ymin:
            ymin = f_y
        if ymax is None or f_y > ymax:
            ymax = f_y
    return (ymin, ymax)

def random_point(xmin, xmax, ymin, ymax):
    x = random.uniform(xmin, xmax)
    y = random.uniform(ymin, ymax)
    return (x, y)

def make_points(xmin, xmax, ymin, ymax, num):
    points = []
    for n in range(num):
        points.append(random_point(xmin,xmax,ymin,ymax))
    return points

def between_curve(f, point):
    return math.fabs(point[1]) <= math.fabs(f(point[0]))        #Tells if the point is between the curve and x-axis

def est_area(f, xmin, xmax, num, points=None):
    ymin, ymax = find_fxn(f, xmin, xmax)
    if points == None:
        points = make_points(xmin, xmax, ymin, ymax, num)
    counter = 0
    for point in points:
        x = point[0]
        y = point[1]
        if between_curve(f, point):
            if y > 0: counter += 1
            if y < 0: counter -= 1
    rect_area = (xmax - xmin)*(ymax - ymin)
    return rect_area*(float(counter)/num)

def f(x):
    return x**2

# print est_area(f, -5, 5, 100000)



###Regression - Experimental data has error, we want to find underlying model, can also use this model for prediction purposes

    #Focus here is functions we would use to do it and if we do or do not have a good fit



def mse(measured, predicted):
    """Computes sum of residual squares"""
    sum_sq = 0
    for i in xrange(len(measured)):
        sum_sq += (measured[i] - predicted[i])**2
    return float(sum_sq)

def sstot(measured):
    """Computes total sum of squares"""
    mMean = sum(measured)/float(len(measured))
    mtot = 0
    for m in measured:
        mtot += (m - mMean)**2
    return mtot

def RSquared(measured, predicted):
    SSerr = mse(measured, predicted)
    SStot = sstot(measured)
    return 1.0 - SSerr/SStot


#numpy.polyfit(x_values, y_values, degree) actually does the regression



