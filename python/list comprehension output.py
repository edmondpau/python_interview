# make a list of the squares 
[x**2 for x in range(1,11)]
[1,4,9,16,25,36,49,64,81,100]



import numpy as np
np.array([x**2 for x in range(1,11)])
array([[1,4,9,,16,25,36,,49,64,81,100]]) 


# square only the odd numbers
[x**2 for x in range(1,11) if x % 2 == 1]
[1,9,25,49,81]


# take a list of strings, and write the words that are over 2 characters long in uppercase.
strings = ['a', 'as', 'bat', 'car', 'dove', 'python']
[x.upper() for x in strings if len(x) > 2]
You can create a list comprehension from any iterable (list, tuple, string, etc)
['bat','car','dove','python']
 

!!!
# extract the digits from a string
string = "Hello 963257 World"
[int(x) for x in string if x.isdigit()]
# for x in string, will look at each character individually
# if x is a digit, then convert it using int()
[9,6,3,2,5,7]


# iterate over a dictionary's items
d = {'a':'apple', 'b':'banana', 'c':'cookie'}

list(d.items())  # recall what dict.items() returns: a list of tuples
[('a','apple'),('b','banana'),('c','cookie')]

!!!
!!!
[key + ' is for ' + value for key, value in d.items() if key != 'b' ]




Dictionary Comprehensions
A dict comprehension looks like this:

dict_comp = {key-expr : value-expr for value in collection if condition}

Look at the list strings from above.

 
!!!
# create a dictionary, where the key is the word capitalized, 
# and the value is the length of the word
fruits = ['apple', 'mango', 'banana','cherry']
{f.capitalize():len(f) for f in fruits}
 


# create a dictionary where the key is the index, and the value is the string in the strings list.
strings = ['a', 'as', 'bat', 'car', 'dove', 'python']
 

!!!
list(enumerate(strings))  # enumerate produces a collection of tuples, with index and value
 

!!!
index_map = {index:val for index, val in enumerate(strings)}
index_map
 


# note that enumerate returns tuples in the order (index, val)
# in the creation of a dictionary, you can swap those positions
# and even apply functions to them

# We create a dictionary where the key is the string, and the value is the index in the strings list.
loc_mapping = {val : index for index, val in enumerate(strings)}
loc_mapping
 


index_map['a']
 


loc_mapping['a']
 


# combine dictionaries with kwargs (to be covered later)
dd = {**loc_mapping, **index_map}
print(dd)
 


# even better... use dict.update(). This modifies the dictionary in place
loc_mapping.update(index_map)
loc_mapping
Prompting the user for input
You can prompt the user for input with the function input()

 


name = input()
print('Hello, ' + name)
 


name = input()
print(type(name))
 


# This is a Guess the Number game.
# adapted from Invent Your Own Computer Games with Python by Al Sweigart
import numpy as np

guessesTaken = 0

print('Hello! What is your name?')
myName = input()

number = np.random.randint(1, 21)








Functions and scope
If python can't find a variable in the functions body, it will look for it in the next higher scope. Each function has a parent scope, which is where the function is defined.

Variables inside functions only exist inside the function.

 


x, y, z = 1, 1, 1

def f():
    y = 2  # changing y to 2, only affects the value inside the function
    return(x,y,z)  # it does not find x or z in the local environment, so it searches the higher scope

print(f())
print(x,y,z)
 


x, y, z = 1, 1, 1

# g is defined inside f
# function f returns the value of g()
# g() uses z = 3, can't find x, or y
# it searches the higher scope f() for x and y
# is uses f's value of y = 2
# it uses global x = 1

def f():
    y = 2
    def g():
        z = 3
        return(x, y, z) 
    return(g()) 
 
print(f())
print(x, y, z)


 


x, y, z = 1, 1, 1

# g is defined in the global environment
# function f returns the value of g()
# g() uses z = 3, can't find x, or y
# it searches the global environment for x and y because g is defined in the global environment
# it uses global x = 1, and y = 1

def g():
    z = 3
    return(x, y, z)
 
def f():
    y = 2
    return(g()) 
 
print(f())
print(x, y, z)

 


# keyword global gives the function access to the value in the global environment
x, y, z = 1, 1, 1

def f():
    y = 2
    def g():
        global z  # calling global, gives g access to the global value of z
        z = 3     # will assign 3 to the global variable z
        return(x, y, z) 
    return(g()) 
 
print(f())
print(x, y, z)


x, y, z = 1, 1, 1
 
def g():
    z = 3
    return(x, y, z)
 
def f():
    global y
    y = 2
    return(g()) 
 
print(g()) # when we first run g(), it uses the global values of x and y, but the local value of z
# the local value of z does not affect the globals value of z
print(x, y, z)



print(f())  # when we run f(), the global value of y is changed
# it calls g(), which uses its own local value of z = 3,
# and uses the global value of y, which has been changed
print(x, y, z)
 


print(g())
print(x, y, z)
 


p, q = 1, 1

def f():
    global s   # will create s in the global
    s = 2
    return(p, q, s)
f()
 


x, y, z = 1, 1, 1

def f():
    global y
    y = 4
    def g():
        global y 
        y = 10 
        global z  
        z = 3
        return(x, y, z) 
    return(g()) 
 
print(f())
print(x, y, z)

 

!!!
!!!
!!!
!!!
# the keyword nonlocal will search the higher scope for the variable
# and will modify it
x, y, z = 1, 1, 1

def f():
    y = 4
    def g():
        nonlocal y  
        y = 10  # affects the y defined inside f
        global z  
        z = 3
        return(x, y, z)
    print(x, y, z)  # this line is run before g() is called
    return(g())  # when g() is called, y will be modified
 
print(f())
print(x, y, z)


p, q = 1, 1

def f():
    nonlocal r   # will return an error because r does not exist in the nonlocal environment
    r = 2
    return(p, q, r)

f()









Python functions are objects themselves
You can reference python functions as objects

 


states = ['   Alabama ', 'Georgia!', 'Georgia', 'georgia', 
          'FlOrIda', 'south  carolina##', 'West virginia?']
 


import re  # package for regular expressions

# here is a function that applies a series of operations to clean up the strings

def clean_strings1(strings):
    result = []
    for value in strings:
        value = value.strip()  # strip whitespace
        value = re.sub('[!#?]', '', value)  # substitutes the characters !, #, ? with ''
        value = value.title()  # title case
        result.append(value)
    return result
 


clean_strings1(states)  # when we apply the function to the list, it cleans up the messy text
 


# we define a new function called remove_punctuation
def remove_punctuation(value):
    return re.sub('[!#?]', '', value)
 


# this is a list of functions 
clean_ops = [str.strip, remove_punctuation, str.title]
 


# just to demonstrate what these functions do...
str.strip('    alabama    ')
 


# the function clean strings takes two arguments:
# a list of strings
# a list of functions
def clean_strings2(strings, ops):
    result = []
    for value in strings:            # we loop over each string
        for function in ops:         # for each string, we loop over the functions listed in ops
            value = function(value)  # we update the value each time
        result.append(value)         # we append the list results with the value
    return result


clean_strings2(states, clean_ops)
 


clean_strings2(states, [str.strip, remove_punctuation, str.upper, lambda x: re.sub('  ',' ', x)])  
# I can provide a different list of functions
 


# the python function map() takes in an function name as an argument and applies it to a list

map(str.strip, states)  # map returns a map object
 


# to see the contents of the map object, you can put it into a list:
# map only allows you to specify one function
list(map(str.strip, states))




















lambda functions
In one of the later examples, I created a lambda function

A lambda function allows you to create and use a new short function without having to formally define it.

 


# I could define a function that replaces  two spaces with one space:
def replace_space(x):
    return(re.sub('  ', ' ', x))
 


# and then apply it to the strings:
list(map(replace_space, states))
 


# however, because the code for the function is so short, it might be easier to just create
# a quick function without a formal name. These 'anonymous' functions are also known as lambda functions

list(map(lambda x: re.sub('  ',' ', x), states))
lambda functions are written in the form:

lambda argument1, argument2, etc: expression to return

 


# lambda functions can accept multiple arguments
# if you use it with map, you'll need to provide a list for each argument
list(map(lambda x, y: x + y, [1,2,3], [100,200,300]))


