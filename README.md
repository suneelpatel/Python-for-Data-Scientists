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

# 2. Functions and Variables:

In Python, A function is **a block of organized, reusable code** that is used to perform single and related action. It is **only runs when it is called**.

You can **pass data, known as parameters**, into a function.

A function can **return data as a result**.

**Return Statement** : The return statement terminates the execution of function and returns control to the calling function 

To define a Python function, you’d have to use the ‘def’ keyword before the name of your function and add parentheses to its end, followed by a colon(:).

Python uses indentation to indicate blocks instead of brackets to make codes more readable.

The "rules" for naming a function are the same as naming a variable. It begins with either letter from A-Z, a-z in both upper & lower cases or an underscore(_). The rest of its name can contain underscores(_), digits(0-9), any letters in upper or lower case.

A reserved keyword may not be chosen as an identifier.
Good usage of grammar to ensure enhanced readability of code.
It is good practice to name a Python function according to what it does. use a docstring right under the first line of a function declaration. This is a documentation string, and it explains what the function does.

## Types Of Python Functions

There are many types of Python Functions. And each of them is very vital in its own way. The following are the different types of Python Functions:

#### 1. Python Built-in Functions
#### 2. Python Recursion Functions
#### 3. Python Lambda Functions
#### 4. Python User-defined Functions

### Built-in-Functions

The Python interpreter has a number of functions that are always available for use. These functions are called built-in functions. For example, print() function prints the given object to the standard output device (screen) or to the text stream file.

In Python 3.6, there are 68 built-in functions. But for the sake of simplicity let us consider the majorly used functions and we can build on from there.

#### 1. Python abs() Function:
Definition :
The abs() method returns the absolute value of the given number. If the number is a complex number, abs() returns its magnitude.

#### 2. Python all() Function:

##### Definition

The all() method returns True when all elements in the given iterable are true. If not, it returns False.

##### Syntax

The syntax of all() method is:

all(iterable)

##### Parameters

The all() method takes a single parameter:

iterable – Any iterable (list, tuple, dictionary, etc.) which contains the elements

#### 3. Python ascii() Function:
##### Definition

The ascii() method returns a string containing a printable representation of an object. It escapes the non-ASCII characters in the string using x, u or U escapes.

##### Syntax

The syntax of ascii() method is:

ascii(object)

##### Parameters

The ascii() method takes an object (like strings, list etc).

#### 4. Python bin() Function:
##### Definition

The bin() method converts and returns the binary equivalent string of a given integer. If the parameter isn’t an integer, it has to implement __index__() method to return an integer.

##### Syntax

The syntax of bin() method is:

bin(num)

##### Parameters

The bin() method takes a single parameter:

num – an integer number whose binary equivalent is to be calculated.
If not an integer, should implement __index__() method to return an integer.

#### 5. Python bool() Function:
##### Definition

The bool() method converts and returns the binary equivalent string of a given integer. If the parameter isn’t an integer, it has to implement __index__() method to return an integer.

##### Syntax

The syntax of bool() method is:

bool([value])

##### Parameters

It’s not mandatory to pass a value to bool(). If you do not pass a value, bool() returns False.

In general use, bool() takes a single parameter value.


#### 6. Python compile() Function:
##### Definition

The compile() method returns a Python code object from the source (normal string, a byte string, or an AST object).

##### Syntax

The syntax of compile() method is:

compile(source, filename, mode, flags=0, dont_inherit=False, optimize=-1)

##### Parameters

* source – a normal string, a byte string, or an AST object
* filename – file from which the code was read. If it wasn’t read from a file, you can give a name yourself
* mode – Either exec or eval or single.
        - eval – accepts only a single expression.
        - exec – It can take a code block that has Python statements, class and functions and so on.
        - single – if it consists of a single interactive statement
* flags (optional) and dont_inherit (optional) – controls which future statements affect the compilation of the source. Default Value: 0
* optimize (optional) – optimization level of the compiler. Default value -1.

#### 7. Python dict() Function:
##### Definition
The dict() constructor creates a dictionary in Python.

##### Syntax
Different forms of dict() constructors are:

* class dict(**kwarg)
* class dict(mapping, **kwarg)
* class dict(iterable, **kwarg)

#### 8. Python enumerate() Function:
##### Definition
The enumerate() method adds counter to an iterable and returns it (the enumerate object).

##### Syntax

The syntax of enumerate() method is:

enumerate(iterable, start=0)

##### Parameters

The enumerate() method takes two parameters:

* iterable – a sequence, an iterator, or objects that support iteration
* start (optional) – enumerate() starts counting from this number. If start is omitted, 0 is taken as the start.

#### 9. Python eval() Function:
##### Definition

The eval() method parses the expression passed to this method and runs python expression (code) within the program.

##### Syntax

The syntax of eval() method is:

eval(expression, globals=None, locals=None)

##### Parameters

The eval() takes three parameters:

* expression – this string is parsed and evaluated as a Python expression
* globals (optional) – a dictionary
* locals (optional)- a mapping object. Dictionary is the standard and commonly used mapping type in Python.

#### 10. Python filter() Function:

##### Definition

The filter() method constructs an iterator from elements of an iterable for which a function returns true.

##### Syntax

The syntax of filter() method is:

filter(function, iterable)

##### Parameters

The filter() method takes two parameters:

* function – function that tests if elements of an iterable return true or false
If None, the function defaults to Identity function – which returns false if any elements are false
* iterable – iterable which is to be filtered, could be sets, lists, tuples, or containers of any iterators

#### 11. Python getattr() Function:

##### Definition

The getattr() method returns the value of the named attribute of an object. If not found, it returns the default value provided to the function.

##### Syntax

The syntax of getattr() method is:

getattr(object, name[, default])

##### Parameters

The getattr() method takes multiple parameters:

* object – object whose named attribute’s value is to be returned
* name – string that contains the attribute’s name
* default (Optional) – value that is returned when the named attribute is not foun

#### 12. Python help() Function:

#### Definition

The help() method calls the built-in Python help system.

##### Syntax
The syntax of help() method is:

help(object)

##### Parameters

The help() method takes the maximum of one parameter.

* object (optional) – you want to generate the help of the given object

#### 13. Python id() Function:
##### Definition

The id() function returns identity (unique integer) of an object.

##### Syntax

The syntax of id() method is:

id(object)

##### Parameters

The id() function takes a single parameter object.

#### 14. Python len() Function:
##### Definition

The len() function returns the number of items (length) in an object.

##### Syntax

The syntax of len() method is:

len(s)

##### Parameters

s – a sequence (string, bytes, tuple, list, or range) or a collection (dictionary, set or frozen set)

#### 15. Python max() Function:
##### Definition

The max() method returns the largest element in an iterable or largest of two or more parameters.

##### Syntax

The syntax of max() method is:

max(iterable, *iterables[,key, default])

max(arg1, arg2, *args[, key])

##### Parameters

max() has two forms of arguments it can work with.

* max(iterable, *iterables[, key, default])
        - iterable – sequence (tuple, string), collection (set, dictionary) or an iterator object whose largest element is to be found
        - *iterables (Optional) – any number of iterables whose largest is to be found
        - key (Optional) – key function where the iterables are passed and the comparison is performed based on its return value
        - default (Optional) – default value if the given iterable is empty

* max(arg1, arg2, *args[, key])
        - arg1 – mandatory first object for comparison (could be number, string or other object)
        - arg2 – mandatory second object for comparison (could be number, string or another object)
        - *args (Optional) – other objects for comparison
        - key – key function where each argument is passed and the comparison is performed based on its return value
        
#### 16. Python min() Function:

##### Definition

The min() method returns the smallest element in an iterable or smallest of two or more parameters.

#### The syntax of min() method is:

min(iterable, *iterables[,key, default])
min(arg1, arg2, *args[, key])

##### Parameters

min() has two forms of arguments it can work with.

* min(iterable, *iterables[, key, default])
        - iterable – sequence (tuple, string), collection (set, dictionary) or an iterator object whose smallest element is to be found
        - *iterables (Optional) – any number of iterables whose smallest is to be found
        - key (Optional) – key function where the iterables are passed and the comparison is performed based on its return value
        - default (Optional) – default value if the given iterable is empty
* min(arg1, arg2, *args[, key])
        - arg1 – mandatory first object for comparison (could be number, string or other object)
        - arg2 – mandatory second object for comparison (could be number, string or other object)
        - *args (Optional) – other objects for comparison
        - key – key function where each argument is passed and a comparison is performed based on its return value

#### 17. Python oct() Function:

##### Definition

The oct() method takes an integer number and returns its octal representation. If the given number is an int, it must implement __index__() method to return an integer.

##### The syntax of oct() method is:

oct(x)

##### Parameters

The oct() method takes a single parameter x.

This parameter could be:

* an integer number (binary, decimal or hexadecimal)
* if not an integer, must implement __index__() method to return an integer


#### 18. Python pow() Function:

##### Definition

The pow() method returns x to the power of y. If the third argument (z) is given, it returns x to the power of y modulus z, i.e. pow(x, y) % z.

##### The syntax of pow() method is:

pow(x, y[, z])

##### Parameters

The pow() method takes three parameters:

* x – number which is to be powered
* y – number which is to be powered with x
* z (Optional) – number which is to be used for modulus operation

#### 19.Python reversed() Function:

##### Definition

The reversed() method returns the reversed iterator of the given sequence.

##### The syntax of reversed() method is:
reversed(seq)

##### Parameters

The reversed() method takes a single parameter:

* seq – sequence that should be reversed

Could be an object that supports sequence protocol (__len__() and __getitem__() methods) as tuple, string, list or range

Could be an object that has implemented __reversed__()

#### 20. Python sum() Function:

##### Definition

The sum() method returns the reversed iterator of the given sequence.

##### The syntax of sum() method is:
sum(iterable, start)

##### Parameters

* iterable – iterable (list, tuple, dict etc) whose item’s sum is to be found. Normally, items of the iterable should be numbers.
* start (optional) – this value is added to the sum of items of the iterable. The default value of start is 0 (if omitted)

#### 21. Python type() Function:

##### Definition

If a single argument (object) is passed to type() built-in, it returns the type of the given object. If three arguments (name, bases, and dict) are passed, it returns a new type object.

##### The syntax of type() method is:
* type(object)
* type(name, bases, dict)

##### Parameters

If the single object argument is passed to type(), it returns the type of the given object.


### Python Recursive Functions

#### What is recursion in Python?
Recursion is the process of defining something in terms of itself.

A physical world example would be to place two parallel mirrors facing each other. Any object in between them would be reflected recursively.

#### Python Recursive Function
We know that in Python, a function can call other functions. It is even possible for the function to call itself. These type of construct are termed as recursive functions.

Following is an example of a recursive function to find the factorial of an integer.

Factorial of a number is the product of all the integers from 1 to that number. For example, the factorial of 5 (denoted as 5!) is 1*2*3*4*5 = 120.


### Lambda Function

#### What Are Lambda functions?

In Python, an anonymous function is a function that is defined without a name.

While normal functions are defined using the def keyword, in Python anonymous functions are defined using the lambda keyword.

Hence, anonymous functions are also called lambda functions.

#### How To Use Lambda Functions In Python?

A Lambda function in python has the following syntax:

lambda arguments: expression

Lambda functions can have any number of arguments but only one expression. The expression is evaluated and returned. Lambda functions can be used wherever function objects are required.

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
