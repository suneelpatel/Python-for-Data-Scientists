# Class: A class in python is the blueprint from which specific objects are created.
# Object: An object in python is the instance of class.

# Attribute = Data = Data Members = Instance Variables
# Method = Function
# Method : A methods which are accessed via dot notation.
# Methods are also called as functions which are defined in a class and describes the behaviour of an object.

# Variables:
# Class variable:  is a variable that is shared by all the different objects/instances of a class.
# Instance variables:  are variables which are unique to each instance.
# It is defined inside a method and belongs only to the current instance of a class.


'''
Now, let us move ahead and see how it works in PyCharm. To get started, first have a look at the syntax of a python class.

Syntax:
class Class_name:
statement-1
.
.
statement-N
'''


# Create class by the name of Student
class Student:

    pass

#create instance or object
Std_1 = Student()
Std_2 = Student()

# define instance variable for first instance std_1
Std_1.first = "Neel"
Std_1.last = "Verma"
Std_1.email = "Neel@school.com"
Std_1.marks = 55

# define instance variable for second instance std_2

Std_2.first = "Hemant"
Std_2.last = "Sharma"
Std_2.email = "Hemant@school.com"
Std_2.marks = 90

#Print or get output from both the instance
print(Std_1.email)
print(Std_2.email)

#-------------------------------------------------------------------------------------------------------------------

# Now ignore lot of codes and manual work for passing instance variable use Methods and Attributes in a Python Class.
# Use init() method as a contractor for new object or new instance.

class Student:
    def __init__(self, first, last, marks):
        self.first = first
        self.last = last
        self.marks = marks
        self.email = first + "." + last + "@school.com"

Std_1 = Student("Neel","Verma",60)
Std_2 = Student("Hemant","Sharma",90)

print(Std_1.first)
print(Std_2.first)

# Let's print email
print(Std_1.email)
print(Std_2.email)

# Let's print full name
print('{} {}'.format(Std_1.first, Std_1.last))
print('{} {}'.format(Std_2.first, Std_2.last))


#----------------- define another method for printing full name ---------------

class Student:
    def __init__(self, first, last, marks):
        self.first = first
        self.last = last
        self.marks = marks
        self.email = first + "." + last + "@school.com"
    
    def fullname(self):
            return '{}{}'.format(self.first,self.last)

Std_1 = Student("Neel","Verma",60)
Std_2 = Student("Hemant","Sharma",90)

# Let's print full name of all instance
print(Std_1.fullname())
print(Std_2.fullname())


#------ define another function which will calculate annual increment of marks

class Student:
    
    perc_rise = 1.05
    
    def __init__(self, first, last, marks):
        self.first = first
        self.last = last
        self.marks = marks
        self.email = first + "." + last + "@school.com"

    def fullname(self):
        return '{}{}'.format(self.first, self.last)

    def apply_raise(self):
        self.marks = int(self.marks * 1.05)
        
Std_1 = Student("Neel","Verma",60)
Std_2 = Student("Hemant","Sharma",90)

print(Std_1.marks)
Std_1.apply_raise()
print(Std_1.marks)

print(Std_2.marks)
Std_2.apply_raise()
print(Std_2.marks)


#---------- Let's create object instance from class "blueprint" -------------

class Student:
    
    perc_rise = 1.05
    
    def __init__(self, first, last, marks):
        self.first = first
        self.last = last
        self.marks = marks
        self.email = first + "." + last + "@school.com"

    def fullname(self):
        return '{}{}'.format(self.first, self.last)

    def apply_raise(self):
        self.marks = int(self.marks * 1.05)

Std_1 = Student("Neel","Verma",60)
Std_2 = Student("Hemant","Sharma",90)

print(Std_1)
print(Std_2)

print(Std_2.__dict__)
print(Student.__dict__)


#========================= Python Class: Inheritance========================

# Inheritance allows us to inherit attributes and methods from the base/parent class.

#1. Parent class ( Super or Base class)

#2. Child class (Subclass or Derived class )

#A class which inherits the properties is known as Child Class 
# whereas a class whose properties are inherited is known as Parent class.

#-------------------------- Create New Class Name: Class Dump---------------
class Student:
    
    perc_rise = 1.05
    
    def __init__(self, first, last, marks):
        self.first = first
        self.last = last
        self.marks = marks
        self.email = first + "." + last + "@school.com"

    def fullname(self):
        return '{}{}'.format(self.first, self.last)

    def apply_raise(self):
        self.marks = int(self.marks * 1.05)

class Dump(Student):
    
    pass

Std_1 = Dump ("Neel","Verma",60)

print(Std_1.email)

# Here we can see Method Resolution Order

print(help(Dump))

#----------------- Add one more attribute in out Base Class------------------

class Student:
    
    perc_rise = 1.05
    
    def __init__(self, first, last, marks):
        self.first = first
        self.last = last
        self.marks = marks
        self.email = first + "." + last + "@school.com"

    def fullname(self):
        return '{}{}'.format(self.first, self.last)

    def apply_raise(self):
        self.marks = int(self.marks * 1.05)

class Dump(Student):
    
    perc_rise = 1.1
    
    def __init__(self, first, last, marks, prog_lang):
        super().__init__(first, last, marks)
        self.prog_lang = prog_lang

Std_1 = Dump("Neel", "Verma", 60, "Python")

print(Std_1.prog_lang)


#======================== Abstract Class ==================================

from abc import ABC, abstractmethod

class Employee (ABC):
    
    @abstractmethod
    
    def calculate_salary(self, sal):
        
        pass
    
class Developer(Employee):
    
    def calculate_salary(self, sal):
        
        finalsalary = sal * 1.10
        
        return finalsalary
    
    def position_1(self, position):
        
        self.position = position
        
        return position
    
emp_1 = Developer()
print(emp_1.calculate_salary(10000))
print(emp_1.position_1("Web Developer"))



#======================= Example: Employee Salary ========================

class employee:
    
    num_empoyee = 0
    raise_amount = 1.04
    
    def __init__(self, first, last, sal):
        
        self.first = first
        self.last = last
        self.sal = sal
        self.email = first + "." + last + "@company.com"
        
    def fullname (self):
        return "{} {}".format(self.first, self.last)
    
    def apply_raise(self):
        self.sal = int(self.sal * raise_amount)
        
class developer (employee):
    
    pass

emp_1 = developer("Sunil","Patel",100000)
print(emp_1.email)


#Now what if I want to change the raise_amount for a developer to 10%?

class employee:
    
    num_empoyee = 0
    raise_amount = 1.04
    
    def __init__(self, first, last, sal):
        
        self.first = first
        self.last = last
        self.sal = sal
        self.email = first + "." + last + "@company.com"
        
    def fullname (self):
        return "{} {}".format(self.first, self.last)
    
    def apply_raise(self):
        self.sal = int(self.sal * raise_amount)
        
class developer (employee):
    
    raise_amount = 1.10

emp_1 = developer("Sunil","Patel",100000)
print(emp_1.raise_amount)


#---------------------------- inheritance ------------------------------

class employee:
    
    num_empoyee = 0
    raise_amount = 1.04
    
    def __init__(self, first, last, sal):
        
        self.first = first
        self.last = last
        self.sal = sal
        self.email = first + "." + last + "@company.com"
        
    def fullname (self):
        return "{} {}".format(self.first, self.last)
    
    def apply_raise(self):
        self.sal = int(self.sal * raise_amount)
        
class developer (employee):
    
    raise_amount = 1.10
    
    def __init__(self, first, last, sal, prog_lang):
        super().__init__(first,last,sal)
        self.prog_lang = prog_lang
        
emp_1 = developer('sunil','patel',100000,'Python')
print(emp_1.prog_lang)


#===============================Python Class: Polymorphism ==================

#Polymorphism in Computer Science is the ability to present the same interface for differing underlying forms.

class Animal:
    
    def __init__(self,name):
        self.name = name
        def talk(self):
            pass
        
class Dog (Animal):
    def talk(self):
        print("woof")
        
class Cat (Animal):
    def talk(self):
        print('Meow')

c = Cat('Ketty')
c.talk()

d = Dog(Animal)
d.talk()
        


