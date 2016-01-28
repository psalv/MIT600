__author__ = 'paulsalvatore57'


        #Quiz 1 Answer and OOP


#Classes let you define a custom type
    #We have been using classes with methods associated with them

#Classes have attributes and methods
    #Attributes are specific instances of a class

#Treat objects with a common superclass the same as their subclasses (POLYMORPHY)


#Not using classes:

def mperson(name, age, weight):
    person = {}
    person['name'] = name
    person['age'] = age
    person['weight'] = weight
    return person

#Will have a bunch of accessor and changer helper functions:

def get_name(person):
    return person['name']
def set_name(person, name):
    person['name'] = name
def print_p(person):
    print 'Name:', get_name(person)

#Doesn't give us any more information, type will be dict



#Using a class:

class Person(object):
    def __init__(self, name, weight):
        self.name = name
        self.weight = weight
    def get_name(self):
        return self.name
    def get_weight(self):
        return self.weight
    def set_name(self, name):
        self.name = name
    def set_weight(self, weight):
        self.weight = weight
    def __str__(self):
        return 'Name:' + self.name + ', Weight:' + self.weight
    def __eq__(self, other):
        return self.name == other.name
    #This method is important for being able to compare two objects together for equality


a1 = Person('Kash', '0')            #Must both be strings, or I need to convert to a string if not (can use assert to do this)
# print a1.get_weight()
# a1.set_weight(4)
# print a1.get_weight()

# print type(a1)
#Marked as being a person (new type)
# print a1

a2 = Person('Nibs', '1')
# print a1 == a2

# print a2.get_weight()
# print Person.get_weight(a2)     #alternative way of writing, where the self parameter comes from



#Can have place holder methods:

class shape(object):
    def area(self):
        raise NotImplementedError       #If you have a shape should have an area, if not have an error

class rect(shape):
    def __init__(self, s1, s2):
        self.s1 = s1
        self.s2 = s2
    def area(self):
        return self.s1 * self.s2

class sq(rect):
    def __init__(self, s):
        rect.__init__(self, s, s)

r = rect(2, 3)
# print r.area()

s = sq(2)
# print s.area()


#Because of polymorphism and inheritance we don't need to worry about which shape we are calling area on:
list_s = [s, r]
for shape in list_s:
    print shape.area()
    print type(shape)

list_s.sort()
print list_s
