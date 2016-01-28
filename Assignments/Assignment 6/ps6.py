# Problem Set 6: Simulating robots
# Name:
# Collaborators:
# Time:


###PROBLEM SPECIFICATIONS:

    #Can have multiple robots in one room, can overlap
    #Room is rectangular (robot must stay within room)
    #Coordinates (x, y) where 0 <= x < width and, 0 <= y < height
    #360 degrees of motion therefore 0 <= d < 360
    #Robots have the same speed moving s units every
    #Robot will continue in the same direction until it hits a wall, when it then picks a new direction randomly

    #Tiles will be 1x1 unit, if the robot is within the tile we consider it cleaned
    #Will have a list of pairs (0,0), (0,1)...(0,h-1), (1,0)...(w-1,0)...(w-1,h-1)

    #Simulation ends when a specified percentage of tiles have been cleaned



import math
import random

import ps6_visualize
import matplotlib.pylab


# === Provided classes


class Position(object):
    """
    A Position represents a location in a two-dimensional room.
    """
    def __init__(self, x, y):
        """
        Initializes a position with coordinates (x, y).
        """
        self.x = x
        self.y = y
    def getX(self):
        return self.x
    def getY(self):
        return self.y
    def getNewPosition(self, angle, speed):
        """
        Computes and returns the new Position after a single clock-tick has
        passed, with this object as the current position, and with the
        specified angle and speed.

        Does NOT test whether the returned position fits inside the room.

        angle: float representing angle in degrees, 0 <= angle < 360
        speed: positive float representing speed

        Returns: a Position object representing the new position.
        """
        old_x, old_y = self.getX(), self.getY()
        # Compute the change in position
        delta_y = speed * math.cos(math.radians(angle))
        delta_x = speed * math.sin(math.radians(angle))
        # Add that to the existing position
        new_x = old_x + delta_x
        new_y = old_y + delta_y
        return Position(new_x, new_y)


# === Problems 1


class RectangularRoom(object):
    """
    A RectangularRoom represents a rectangular region containing clean or dirty
    tiles.

    A room has a width and a height and contains (width * height) tiles. At any
    particular time, each of these tiles is either clean or dirty.
    """
    def __init__(self, width, height):
        """
        Initializes a rectangular room with the specified width and height.

        Initially, no tiles in the room have been cleaned.

        width: an integer > 0
        height: an integer > 0
        """
        assert width and height > 0
        self.width = width
        self.height = height
        self.clean = []
    
    def cleanTileAtPosition(self, pos):
        """
        Mark the tile under the position POS as cleaned.

        Assumes that POS represents a valid position inside this room.

        pos: a Position
        """
        self.clean += [pos,]
        return self.clean

    def isTileCleaned(self, m, n):
        """
        Return True if the tile (m, n) has been cleaned.

        Assumes that (m, n) represents a valid tile inside the room.

        m: an integer
        n: an integer
        returns: True if (m, n) is cleaned, False otherwise
        """
        if (m, n) in self.clean:
            return True
        else:
            return False
    
    def getNumTiles(self):
        """
        Return the total number of tiles in the room.

        returns: an integer
        """
        return self.height*self.width

    def getNumCleanedTiles(self):
        """
        Return the total number of clean tiles in the room.

        returns: an integer
        """
        return len(self.clean)

    def getRandomPosition(self):
        """
        Return a random position inside the room.

        returns: a Position object.
        """
        return Position(random.choice(range(self.width + 1)), random.choice(range(self.height + 1)))

    def isPositionInRoom(self, pos):
        """
        Return True if pos is inside the room.

        pos: a Position object.
        returns: True if pos is in the room, False otherwise.
        """
        if 0 <= pos.getX() < self.width and 0 <= pos.getY() < self.height:
            return True
        else:
            return False


class Robot(object):
    """
    Represents a robot cleaning a particular room.

    At all times the robot has a particular position and direction in the room.
    The robot also has a fixed speed.

    Subclasses of Robot should provide movement strategies by implementing
    updatePositionAndClean(), which simulates a single time-step.
    """
    def __init__(self, room, speed):
        """
        Initializes a Robot with the given speed in the specified room. The
        robot initially has a random direction and a random position in the
        room. The robot cleans the tile it is on.

        room:  a RectangularRoom object.
        speed: a float (speed > 0)
        """
        self.speed = speed
        self.room = room
        self.direction = random.choice(range(361))
        self.position = room.getRandomPosition()

    def getRobotPosition(self):
        """
        Return the position of the robot.

        returns: a Position object giving the robot's position.
        """
        return self.position
    
    def getRobotDirection(self):
        """
        Return the direction of the robot.

        returns: an integer d giving the direction of the robot as an angle in
        degrees, 0 <= d < 360.
        """
        return self.direction

    def setRobotPosition(self, position):
        """
        Set the position of the robot to POSITION.

        position: a Position object.
        """
        self.position = position
        return self.position

    def setRobotDirection(self, direction):
        """
        Set the direction of the robot to DIRECTION.

        direction: integer representing an angle in degrees
        """
        self.direction = direction
        return self.direction

    def updatePositionAndClean(self):
        """
        Simulate the raise passage of a single time-step.

        Move the robot to a new position and mark the tile it is on as having
        been cleaned.
        """
        newposition = self.position.getNewPosition(self.direction, self.speed)
        if self.room.isPositionInRoom(newposition):
            self.position = newposition
            if self.room.isTileCleaned(int(self.position.getX()), int(self.position.getY())) == False:
                    self.room.cleanTileAtPosition((int(self.position.getX()), int(self.position.getY())))
            return True
        else:
            return False


# # === Problem 2


class StandardRobot(Robot):
    """
    A StandardRobot is a Robot with the standard movement strategy.

    At each time-step, a StandardRobot attempts to move in its current direction; when
    it hits a wall, it chooses a new direction randomly.
    """
    def updatePositionAndClean(self):
        """
        Simulate the passage of a single time-step.

        Move the robot to a new position and mark the tile it is on as having
        been cleaned.
        """
        while True:
            newposition = self.position.getNewPosition(self.direction, self.speed)
            if self.room.isPositionInRoom(newposition):
                self.position = newposition
                if self.room.isTileCleaned(int(self.position.getX()), int(self.position.getY())) == False:
                    self.room.cleanTileAtPosition((int(self.position.getX()), int(self.position.getY())))
                return True
            else:
                self.direction = random.choice(range(361))



# # === Problem 3
#We want to find how many time steps (on average) are needed to cover a specified area (percentage)


def runSimulation(num_robots, speed, width, height, min_coverage, num_trials, robot_type):
    """
    Runs NUM_TRIALS trials of the simulation and returns the mean number of
    time-steps needed to clean the fraction MIN_COVERAGE of the room.

    The simulation is run with NUM_ROBOTS robots of type ROBOT_TYPE, each with
    speed SPEED, in a room of dimensions WIDTH x HEIGHT.

    num_robots: an int (num_robots > 0)
    speed: a float (speed > 0)
    width: an int (width > 0)
    height: an int (height > 0)
    min_coverage: a float (0 <= min_coverage <= 1.0)
    num_trials: an int (num_trials > 0)
    robot_type: class of robot to be instantiated (e.g. Robot or
                RandomWalkRobot)
    """
    numstepsrequired = []
    tilesneeded = width*height*min_coverage
    for n in range(num_trials):
        # anim = ps6_visualize.RobotVisualization(num_robots, width, height)            #Tk() in ps6_visualize is causing python to crash, I am unsure why
        stepholder = []
        room = RectangularRoom(width, height)
        robots = []
        for x in range(num_robots):
            robots += [robot_type(room, speed)]
        for i in robots:
            starting_position = i.getRobotPosition()
            if room.isTileCleaned(int(starting_position.getX()), int(starting_position.getY())) == False:
                room.cleanTileAtPosition((int(starting_position.getX()), int(starting_position.getY())))
        while room.getNumCleanedTiles() < tilesneeded:
            for i in robots:
                stepholder += [1,]                      #Could have put this after the for loop therefore will only add after all robots have moved
                i.updatePositionAndClean()
                # if len(stepholder)%num_robots == 0:
                #     anim.update(room, robots)
        # anim.done()
        numstepsrequired += [(len(stepholder)/num_robots),]
    avg = 0
    for i in numstepsrequired:
        avg += i
    return avg/num_trials

# avg = runSimulation(1, 1.0, 5, 5, 1.0, 10, StandardRobot)
# print avg


# # === Problem 4


# # 1) How long does it take to clean 80% of a 20x20 room with each of 1-10 robots?

# # 2) How long does it take two robots to clean 80% of rooms with dimensions:
#           20x20, 25x16, 40x10, 50x8, 80x5, and 100x4?

def showPlot1(fraction, num_robots):
    """
    Produces a plot showing dependence of cleaning time on number of robots.
    """
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

def showPlot2(list_dimensions):
    """
    Produces a plot showing dependence of cleaning time on room shape.
    """
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






# # === Problem 5


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


# print runSimulation(1, 1.0, 5, 5, 1.0, 100, RandomWalkRobot)



# # === Problem 6
#
# # For the parameters tested below (cleaning 80% of a 20x20 square room),
# # RandomWalkRobots take approximately twice as long to clean the same room as
# # StandardRobots do.

def showPlot3(fraction, num_robots):
    """
    Produces a plot showing dependence of cleaning time on number of robots.
    """
    q = fraction
    timesteps = []
    timestepsR = []
    robotnumber = []
    robotnumberR = []
    for i in range(1,num_robots + 1):
        timesteps.append(runSimulation(i, 1.0, 20, 20, q, 100, StandardRobot))
        print 'STANDARD:', i, 'has completed'
        robotnumber.append((i))
    matplotlib.pylab.plot(robotnumber, timesteps)
    for i in range(1,num_robots + 1):
        timestepsR.append(runSimulation(i, 1.0, 20, 20, q, 100, RandomWalkRobot))
        print 'RANDOM:', i, 'has completed'
        robotnumberR.append((i))
    print 'Standard times:', timesteps
    print 'Random times:', timestepsR
    matplotlib.pylab.plot(robotnumberR, timestepsR)
    matplotlib.pylab.title('Cleaning time as a function of number of robots')
    matplotlib.pylab.xlabel('Number of robots')
    matplotlib.pylab.ylabel('Average timesteps taken to complete cleaning')
    matplotlib.pylab.show()

showPlot3(0.8, 10)

