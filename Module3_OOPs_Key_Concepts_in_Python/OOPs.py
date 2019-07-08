# -*- coding: utf-8 -*-
"""
Created on Tue Mar 19 21:34:03 2019

@author: HP
"""

# ========================= OPPs (Object Oriented Programming)===============

#Creating a Class

class number():
    pass

#Creating Instance of Class
x=number()
print(x)

##Method

class Master():
    def Hello(self):
        print("Happy Learning")

ob=Master()
ob.Hello()



##Scope of variables
a=50
class number():
    b=30
    print(b)

print(a)
print(b)
number()



a=30
def add(b):
    c=30
    print("c=",c)
    sum=b+c
    print("Addition is: ",sum)

print(a)
add(40)
print(c)


##Built in class attributes
class Master:
    empcount=0

print("Master.__dict__:",Master.__dict__)

print("Master.__doc__:",Master.__doc__)

print("Master.__name__",Master.__name__)

print("Master.__module__:",Master.__module__)

print("Master.__bases__:",Master.__bases__)


##user defined attributes

a=50

class Foo(object):
    def meth(self):
       pass
   
###public provate protected
class Master():
    def __init__(self):
        self.__pri="I am Private"
        self._pro="I am Protected"
        self.pub="I am Public"

ob=Master()

#Accessing Public Attribute
ob.pub

#Accessing Protected Attributes
ob._pro

#Accessing Private Attributes
ob.__pri



###Private method
class MyClass:
    def myPublicMethod(self):
        print('public method')
    def __myPrivateMethod(self):
        print('this is private!!')

obj = MyClass()
obj.myPublicMethod()

obj.__myPrivateMethod()

#obj.__myPrivateMethod()
obj._MyClass__myPrivateMethod()


### Class variables are instence variables
class Master:
    domain=("Data Science")
    def Setcourse(self,name):
        self.name=name

ob1=Master()
ob2=Master()

ob1.Setcourse("Python")
ob2.Setcourse("Machine Learning")

print(ob2.domain)
ob1.domain = 'GOD'
print(ob1.domain)
print(ob2.domain)

print(ob1.name)
print(ob2.name)

##Constructor an destructor
class TestClass:
    def __init__(self):
        print("constructor")

    def __del__(self):
        print("destructor")


if __name__ == "__main__":
    obj = TestClass()
    del obj
    
    
    
##Multiple constructor
    
class Date:
	def __init__(self, year, month, day): #year-month-day
		self.year = year
		self.month = month
		self.day = day
		# print("init")

	@classmethod
	def dmy(cls, day, month, year): #day-month-year
		# print("dmy")
		cls.year = year
		cls.month = month
		cls.day = day
		#order of return should be same as init
		return cls(cls.year, cls.month, cls.day)

	@classmethod
	def mdy(cls, month, day, year): #month-day-year
		# print("mdy")
		cls.year = year
		cls.month = month
		cls.day = day
		#order of return should be same as init
		return cls(cls.year, cls.month, cls.day)

a=Date(2016, 12, 11)
print(a.month) #2016

b=Date.dmy(9, 10, 2015)
print(b.year) #2015

a=Date.mdy(7, 8, 2014)
print(a.year) #2014



###sing inheritence
class base1:
    def fun(self):
        print("In Class Base 1")

class sub(base1):
        pass

ob=sub()
ob.fun()


#####multi inheritence


#Multiple Inheritance
class First(object):
    def __init__(self):
        super(First, self).__init__()
        print("first")


class Second(object):
    def __init__(self):
        super(Second, self).__init__()
        print("second")


class Third(Second, First):
    def __init__(self):
        super(Third, self).__init__()
        print("third")


Third();
Second();



#Multilevel Inheritance
class Animal:
    def eat(self):
      print('Eating...')
class Dog(Animal):
   def bark(self):
      print('Barking...')
class BabyDog(Dog):
    def weep(self):
        print('Weeping...')
d=BabyDog()
d.eat()
d.bark()
d.weep()


##Over writing method
class Parent: # define parent class
  def myMethod(self):
    print("Calling parent method")
class Child(Parent): # define child class
  def myMethod(self):
    print("Calling child method")
c = Child()   # instance of child
c.myMethod() # child calls overridden method


#Another Example:

class Rectangle():
  def __init__(self,length,breadth):
    self.length = length
    self.breadth = breadth
  def getArea(self):
    print(self.length*self.breadth," is area of rectangle")

class Square(Rectangle):
  def __init__(self,side):
    self.side = side
    Rectangle.__init__(self,side,side)
  def getArea(self):
    print(self.side*self.side," is area of square")

s = Square(4)
r = Rectangle(2,4)
s.getArea()
r.getArea()



###Poly
class Animal:
    def __init(self,name):
        self.name=name

    def talk(self):
        print("Talk")

class Cat(Animal):
    def talk(self):
        print("Meow")

class Dog(Animal):
    def talk(self):
        print("Woof")

c=Cat()
c.talk()

d=Dog()
d.talk()




class Bear(object):
    def sound(self):
        print ("Groarrr")
 
class Dog(object):
    def sound(self):
        print ("Woof woof!")
 
def makeSound(animalType):
    animalType.sound()
 
 
bearObj = Bear()
dogObj = Dog()
 
makeSound(bearObj)
makeSound(dogObj)

##Getter and Setter
class Master:
    def __init__(self,courseName):
        self.courseName=courseName

    def setCourse_Name(self,courseName):
        self.courseName=courseName

    def getCourse_Name(self):
        return(self.courseName)

ob=Master("Machine Learning")

print(ob.getCourse_Name())

ob.setCourse_Name("Python")
print(ob.getCourse_Name())
