__author__ = 'paulsalvatore57'
import random
import math

h = 10
w = 20

#HOW TO RETURN A RANDOM NUMBER OVER A RANGE OF NUMBERS:
# random.choice(range(h + 1))

class Position(object):

    def __init__(self, x, y):
        self.x = x
        self.y = y
    def getX(self):
        return self.x
    def getY(self):
        return self.y
    def getNewPosition(self, angle, speed):
        old_x, old_y = self.getX(), self.getY()
        # Compute the change in position
        delta_y = speed * math.cos(math.radians(angle))
        delta_x = speed * math.sin(math.radians(angle))
        # Add that to the existing position
        new_x = old_x + delta_x
        new_y = old_y + delta_y
        return Position(new_x, new_y)

# p = Position(random.choice(range(w + 1)), random.choice(range(h + 1)))
# print p.getX()

class RectangularRoom(object):
    def __init__(self, width, height):
        assert width and height > 0
        self.width = width
        self.height = height
        self.clean = []
    def cleanTileAtPosition(self, pos):     #Implemented as a list of tuples, unsure if this is correct
        self.clean += [pos,]
        # print self.clean
        return self.clean
    def isTileCleaned(self, m, n):
        if (m, n) in self.clean:
            return True
        else:
            return False
    def getNumTiles(self):
        return self.height*self.width
    def getNumCleanedTiles(self):
        return len(self.clean)
    def getRandomPosition(self):
        return Position(random.choice(range(self.width + 1)), random.choice(range(self.height + 1)))
    def isPositionInRoom(self, pos):
        if 0 <= pos.getX() < self.width and 0 <= pos.getY() < self.height:
            return True
        else:
            return False

class Robot(object):
    def __init__(self, room, speed):
        self.speed = speed
        self.room = room
        self.direction = random.choice(range(361))
        self.position = room.getRandomPosition()
    def getRobotPosition(self):
        return self.position
    def getRobotDirection(self):
        return self.direction
    def setRobotPosition(self, position):
        self.position = position
        return self.position
    def setRobotDirection(self, direction):
        self.direction = direction
        return self.direction
    def updatePositionAndClean(self):
        newposition = self.position.getNewPosition(self.direction, self.speed)
        if self.room.isPositionInRoom(newposition):
            self.position = newposition
            if self.room.isTileCleaned(int(self.position.getX()), int(self.position.getY())) == False:
                    self.room.cleanTileAtPosition((int(self.position.getX()), int(self.position.getY())))
            return True
        else:
            return False


# room = RectangularRoom(w, h)

# r1 = Robot(room, 1)
# p = r1.getRobotPosition()
# pcoordinates = (p.getX(), p.getY())
# print 'Starting point:', pcoordinates
# print 'New point:', r1.updatePositionAndClean()


class StandardRobot(Robot):
    def updatePositionAndClean(self):
        while True:
            newposition = self.position.getNewPosition(self.direction, self.speed)
            if self.room.isPositionInRoom(newposition):
                self.position = newposition
            #Ensures that we have not moved out of the room, if so then we need to change direction and try again

                if self.room.isTileCleaned(int(self.position.getX()), int(self.position.getY())) == False:
                    self.room.cleanTileAtPosition((int(self.position.getX()), int(self.position.getY())))
            #If the tile is not yet clean it adds it to the list of clean tiles

                return True
            else:
                self.direction = random.choice(range(361))


# r2 = StandardRobot(room, 1)
# p2 = r2.getRobotPosition()
# p2coordinates = (p2.getX(), p2.getY())
# print 'Starting point:', p2coordinates
# print 'New point:', r2.updatePositionAndClean()

def runSimulation(num_robots, speed, width, height, min_coverage, num_trials, robot_type):              #ALWAYS ROUND DOWN, THIS IS USEFUL
    numstepsrequired = []
    tilesneeded = width*height*min_coverage
    for n in range(num_trials):
        stepholder = []
        room = RectangularRoom(width, height)
        #Resets the room, and therefore the clean tiles

        robots = []
        for x in range(num_robots):
            robots += [robot_type(room, speed)]
        #Creates a list of robots

        for i in robots:
            starting_position = i.getRobotPosition()
            if room.isTileCleaned(int(starting_position.getX()), int(starting_position.getY())) == False:
                room.cleanTileAtPosition((int(starting_position.getX()), int(starting_position.getY())))
        #Initilizes the robots such that they are all at a posiion, and the position is cleaned (accounts for same starting position)

        while room.getNumCleanedTiles() < tilesneeded:
            for i in robots:
                stepholder += [1,]
                i.updatePositionAndClean()
        #Moves the robots, one at a time in sequential order cleaning uncleaned tiles until the desired amount are clean

        numstepsrequired += [(len(stepholder)/num_robots),]
        #Steps represent seconds therefore must divide by number of robots (take x number of steps/second)

    avg = 0
    for i in numstepsrequired:
        avg += i
    return avg/num_trials
    #Takes the average of the trials and returns it


#print runSimulation(1, 1.0, 5, 5, 1.0, 100, StandardRobot)


import matplotlib.pylab

def showPlot1(fraction, num_robots):
    q = fraction
    timesteps = []
    robotnumber = []
    for i in range(1,num_robots + 1):
        timesteps.append(runSimulation(i, 1.0, 20, 20, q, 100, StandardRobot))
        robotnumber.append((i))
    matplotlib.pylab.plot(robotnumber, timesteps)
    matplotlib.pylab.title('Cleaning time as a function of number of robots')
    matplotlib.pylab.xlabel('Number of robots')
    matplotlib.pylab.ylabel('Average timesteps taken to complete cleaning')
    matplotlib.pylab.show()

# showPlot1(0.8, 10)



#Y-axis = mean time
#X-axis = ratio width:height

def showPlot2(list_dimensions):
    q = 0.8
    timesteps = []
    ratio = []
    for i in list_dimensions:
        timesteps.append(runSimulation(2, 1.0, i[0], i[1], q, 100, StandardRobot))
        ratio.append(i[0]/i[1])
    matplotlib.pylab.plot(ratio, timesteps)
    matplotlib.pylab.title('Cleaning time as a function of room dimensions')
    matplotlib.pylab.xlabel('Ratio of width:height')
    matplotlib.pylab.ylabel('Average timesteps taken to complete cleaning')
    matplotlib.pylab.show()

# showPlot2([(20, 20), (25, 16), (40, 10), (50, 8), (80, 5), (100, 4)])


class RandomWalkRobot(Robot):
    def updatePositionAndClean(self):
            while True:
                self.direction = random.choice(range(361))
                newposition = self.position.getNewPosition(self.direction, self.speed)
                if self.room.isPositionInRoom(newposition):
                    self.position = newposition
                    if self.room.isTileCleaned(int(self.position.getX()), int(self.position.getY())) == False:
                        self.room.cleanTileAtPosition((int(self.position.getX()), int(self.position.getY())))
                    return True


# print 'Random:', runSimulation(1, 1.0, 5, 5, 1.0, 200, RandomWalkRobot)
# print 'Standard:', runSimulation(1, 1.0, 5, 5, 1.0, 200, StandardRobot)
