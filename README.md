# Python-for-Data-Scientists
This repository will offer several learning strategies and advanced study material along with the interesting Python code that will help jump start your journey of becoming a rockstar Python programmer!

# Table of Content:
1. Sequence and it's operation
    - What is Sequences
    - Type of Sequence
    - Sequence Operations
2. Functions and Variables
    - Built-in-Functions
    - Lambda Function
    - Scope of Variables
3. Object Oriented Progrmaming (OOPs) Key Concepts
    - POPs Vs OOPs
    - Classes and Objects
    - OOPs Features
4. Standard Libraries
    - Built-in-Function
    - Modules
    - Packages
5. Numpy
5. Pandas
6. Matplotlib (Data Visualization)
7. Data Manipulation
8. Web Mapping
9. Web Scrapping
10. Computer Vision
11. Regular Expression (RegEx)


# 1. Sequence and it's operation

## What is Sequences

A sequence is a succession of values bound together by a container that reflects their type. In other words, Sequences are containers with the items or elements that are accessible by indexing or slicing.

Almost every stream that you put in Python is a sequence. The sequence is central to programming and central to Python.

### Type of Sequence
    - 1. List
    - 2. Tuples
    - 3. Xrange
    - 4. Strings
    - 5. Sets
    - 6. Dictionaries
    
### Sequence Operations

* Concatenation
* Repetation
* Membership Testing
* Slicing
* Indexing
* Reversing

### List

List is a collection datatype in python. It is ordered and allows duplicate entries as well. Lists in python need not be homogeneous, which means it can contain different data types like integers, strings and other collection data types. 

It is mutable in nature and allows indexing to access the members in a list. Also, the values can be changed even after a list is declared.

* A list is a sort of container that holds a number of other objects, in a given order.
* The list type implements the sequence protocol, and it also allows you to add and remove objects from the sequence.
* It is an ordered set of elements enclosed in square brackets.

Simple definition of list – li = []

li = list() # empty list
li = list(sequence)
li = list(expression for variable in sequence)

#### Accessing List Elements
To access the elements of a list:

n = len(li)

item = li[index] #Indexing

slice = li[start:stop] #Slicing


#### Why Use A List?
While choosing a data type for storing our data, we must keep in mind the properties and features of the data type. It becomes more efficient and secure if we make the right choice in first place.

A list is preferred because it can store multiple data at the same time. It becomes easy to replace and modify the values inside a list. We can store the sequence in a list and perform several iterations using the loops as well. There are numerous operations we can perform on a list as well, lets understand the various operations that we have for lists in python.

### List Operations in Sequence
Following are the operations that we can perform on a list.
* append
* clear
* copy
* count
* extend
* insert
* index
* pop
* remove
* reverse
* sort


### Tuples Operation in Sequence
Tuple is a collection which is unchangeable or immutable. It is ordered and the values can be accessed using the index values. A tuple can have duplicate values as well. To declare a tuple we use the round brackets.


### Xrange Operation in Sequence
Range is a data type which is mainly used when we are using a loop.

#### Range Function
Range() generates lists containing arithmetic progression.

There are three variations of range() function:

>> range(stop) – Starts from 0 till (stop – 1)

>> range(start,stop) – Ends at (stop – 1)

>> range(start,stop,step) – Step cannot be 0, default is 1

##### Example of Range Function

#### range(stop): 
If the range is defined as 5, it will simply show the list of numbers falling in the range from 0 to 5. It starts by default from 0 and stops before 5, as defined.

#### range(start, stop): 
In this, point of starting as well as stopping is defined. As shown in the example below, the start range has been defined as 5, while stop range as 10. Hence, it will display the numbers 5, 6, 7, 8, 9, which range between 5 to 10.

#### range(start, stop, step): 
The first two values defined here are the same, start and stop, while the third one is step, which means the difference between every two consecutive numbers. For example, if range is defined in this way: range(0, 10, 2). It will give away numbers between 0 to 10, but with a difference of 2, in this way: [0, 2, 4, 6, 8]. The step here cannot be given 0 value. It has to be 1 or greater than 1.


### Strings Operation in Sequence

Strings in python are used to represent unicode character values. Python does not have a character data type, a single character is also considered as a string.

We denote or declare the string values inside single quotes or double quotes. To access the values in a string, we use the indexes and square brackets.

Strings are immutable in nature, which means you cannot change a string once replaced. 


### Sets Operation in Sequence

A set is a collection which is unordered,  it does not have any indexes as well. To declare a set in python we use the curly brackets.

myset = {10, 20 , 30 ,40, 50, 50}

A set does not have any duplicate values, even though it will not show any errors while declaring the set, the output will only have the distinct values.

#### When to use sets in Python?
Sets in Python are used when-

* The order of data does not matter
* You do not need any repetitions in the data elements
* You need to perform mathematical operations such as union, intersection, etc

Now let us move ahead and see how to create sets in Python.

#### How do you create a set in Python?
Sets in Python can be created in two ways-

* enclosing elements within curly braces
* by using the set() function

#### Set Operations
A number of operations can be performed on sets such as adding elements, deleting elements, finding the length of a set, etc. To know what all methods can be used on sets, you can use the dir() function.

#### Finding the Length of a Set
To find the length of a set in Python, you can use the len() function. This function takes the name of the set as a parameter and returns an integer value which is equal to the number of elements present in the set.

#### Accessing Elements of a Set
Set elements cannot be accessed using the index numbers because, as specified before, elements of a set are not indexed. Therefore, when you want to access elements of a set, you can loop through it and access its elements.

#### Adding elements to a Set:
Elements can be added to a set using two functions, the add() and the update() function.

#### Removing Elements of a Set
To remove elements from a set, you can use either the remove(), discard() and the pop() functions.

#### Union of Sets
Union of sets refers to the concatenation of two or more sets into a single set by adding all unique elements present in both sets. This can be done in two ways:

* Using pipeline
* Using union() function

####   Intersection of Sets

The intersection of two or more sets is a new set consisting of only the common elements present in those sets.

This can be done in two ways:

* Using ‘&’ symbol
* Using intersection() function

#### Difference of Sets:
The difference of sets produces a new set consisting of elements that are present only in one of those sets. This means that all elements except the common elements of those sets will be returned.

This can be done in two ways:

* Using the ‘-‘ symbol
* Using difference() function

#### What is a frozen set?

A frozen set in Python is a set whose values cannot be modified. This means that it is immutable unlike a normal set which I have discussed previously. Frozen sets help serve as a key in dictionary key-value pairs.

#### How to create frozen sets?
Frozen sets can be obtained using the frozenset() method. This function takes any iterable items and converts it to immutable.


### Dictionaries Operation in Sequence

A dictionary is just like any other collection array in python. But they have key value pairs. A dictionary is unordered and changeable. We use the keys to access the items from a dictionary. To declare a dictionary, we use the curly brackets.

Since we are using the keys to access the items, they cannot be duplicate.The values can have duplicate items.

# 2. Functions and Variables

### Built-in-Functions

### Lambda Function

### Scope of Variables

# 3. Object Oriented Progrmaming (OOPs) Key Concepts

### POPs Vs OOPs

### Classes and Objects

### OOPs Features

# 4. Standard Libraries

### Built-in-Function

### Modules

### Packages

# 5. Numpy

# 6. Pandas

# 7. Matplotlib (Data Visualization)

# 8. Data Manipulation

# 9. Web Mapping

# 10 Web Scrapping

# 11. Computer Vision

# 12. Regular Expression (RegEx)
