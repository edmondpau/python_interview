#How is string interpolation
name = 'Chris'


f strings
print(f'Hello {name}')


% operator
print('Hey %s %s' % (name, name))


format
print(
    "My name is {}".format(name))
)

#3
a = [1,2,3]
b = a
c = [1,2,3]


check equality and they are all EQUAL


print(a == b)   True 
print(a == c)   True


print(a is b)   True
print(a is c)   False


print(id(a))    123
print(id(b))    123
print(id(c))    888


Diff ID

#4

def logging(func):
    def log_function_called():
        print(f'{func} called.')
        func()
    return log_function_called

# Function with decorator
def my_name():
    print('chris')


def friends_name():
    print('naruto')


my_name()
friends_name()
#=> chris
#=> naruto


@logging
def my_name():
    print('chris')


@logging
def friends_name():
    print('naruto')


my_name()
friends_name()
#=> <function my_name at 0x0cx0> called.
#=> chris
#=> <function friends_name at 0x0c0>
called.
#=> naruto



##5

Range generates a list of integers and there are 3 ways to use it.
The function takes 1 to 3 arguments. Note I’ve wrapped each usage in list comprehension so we can see the values generated.
range(stop) : generate integers from 0 to the “stop” integer.


[i for i in range(2,10)]
#=> [2,3,4,5,6,7,8,9]


[i for i in range(2,10)]
#=> [2,3,4,5,6,7,8,9]


[i for i in range(2,10,2)]
#=> [2,4,6,8]


list(range(2,10,2))
#=> [2,4,6,8]


##6

class Car :
    def __init__(self,color,speed):
        self.color = color
        self.speed = speed


car = Car('red', '100mph')
car.speed
#=> '100mph'



###7

class CoffeeShop:
    specialty = 'espresso'

    
    def __init__(self, coffee_price):
        self.coffee_price = coffee_price

    
    # instance method
    def make_coffee(self):
        print(f'Making {self.specialty} for
    ${self.coffee_price}')


    # static method
    @staticmethod
    def check_weather():
        print('Its sunny')


    # classs method
    @classmethod
    def change_specialty(cls,specialty):
        cls.specialty = specialty
        print(f'Specialty changed to 
    {specialty}')


coffee_shop = CoffeeShop('5')
coffee_shop.make_coffee()
#=> Making espresso for $5


coffee_shop.check_weather()
#=> Its sunny


coffee_shop.change_specialty('drip coffee')
#=> Specialty changed to drip coffee


coffee_shop.make_coffee()
#=> Making drip coffee for $5





#8
def func():
    print('Im a function')


func
#=> function __main__.func>


func()
#=> Im a function



#9
def add_three(x):
    return x + 3

li = [1,2,3]


[i for i in map(add_three, li)]
#=> [4,5,6]


def add_three(x):
    return x + 3


li = [1,2,3]
list(map(add_three, li))
#=> [4, 5, 6]



##10
from functools import reduce


def add_three(x,y):
    return x + y


li = [1,2,3,5]


reduce(add_three,li)
#=> 11



####11
def add_three(x):
    if x % 2 == 0:
        return True
    else:
        return False


li = [1,2,3,4,5,6,7,8]


[i for i in filter(add_three, li)]
#=> [2,4,6,8]


# 12

x = 'some text'
y = x
x is y
#=> True


del x
this deletes the 'a' name but does nothing to the object in memoryview


z = y
y is z
#=> True


What we see is that all these names point to the same object in memory, which wasn’t affected by del x.
Here’s another interesting example with a function.



name = 'text'


def add_chars(strl):
    print( id(strl) )   #=> 123
    print( id(name) )   #=> 123


#new name, same object
str2 = strl


creates a new name (with same name as the first) and object
strl += 's'
print( id(strl) ) #=> 888


still the original object
print(  id(str2)  ) #=> 123


add_chars(name)
print(name) 
#=>text


## 13

li = ['a','b','c']


print(li)
li.reverse()
print(li)

#>>> ['a', 'b', 'c']
#>>> ['c', 'b', 'a']



## 14

'cat' * 3
#>>> 'catcatcat'


#15 

[1,2,3] * 2
#>> [1,2,3,1,2,3]



## 16

class Shirt:
    def __init_(self, color):
        self.color = color


s = Shirt('yellow')
s.color
#>>> 'yellow'


#17

a = [1.2]
b = [3,4,5]


a + b



##18

li1 = [['a'],['b'],['c']]
li2 = li1


li1.append(['d'])
print(li2)
#=> [['a'], ['b'], ['c'], ['d']]


li3 = [['a'],['b'],['c']]
li4 = list(li3)


li3.append([4])
print(li4)
#=> [['a'], ['b'], ['c']]


li3[0][0] = ['X']
print(li4)
#=> [[['X']], ['b'], ['c']]

import copy


li5 = [['a'],['b'],['c']]
li6 = copy.deepcopy(li5)


li5.append([4])
li5[0][0] = ['X']
print(li6)
#=> [['a'], ['b'], ['c']]



#19


#20

import numpy as np


a = np.array([1,2,3])
b = np.array([4,5,6])


np.concatenate((a,b))
#=> array([1, 2, 3, 4, 5, 6])


a = 5.12345
round(a,3)
#=> 5.123


a = [0,1,2,3,4,5,6,7,8,9]
print(a[:2])
#=> [0, 1]
print(a[8:])
#=> [8, 9]
print(a[2:8])
#=> [2, 3, 4, 5, 6, 7]
print(a[2:8:2])
#=> [2, 4, 6]


import pickle
obj = [
    {'id':1, 'name':'Stuffy'},
    {'id':2, 'name': 'Fluffy'}
]


with open('file.p', 'wb') as f:
    pickle.dump(obj, f)
with open('file.p', 'rb') as f:
    loaded_obj = pickle.load(f)


print(loaded_obj)
#=> [{'id': 1, 'name': 'Stuffy'}, {'id': 2, 'name': 'Fluffy'}]



#29


a = [False, False, False]
b = [True, False, False]
c = [True, True, True]
print( any(a) )
print( any(b) )
print( any(c) )
#=> False
#=> True
#=> True
print( all(a) )
print( all(b) )
print( all(c) )
#=> False
#=> False
#=> True

import sklearn

from sklearn import cross_validation

#32

value = 5
value += 1
print(value)
#=> 6
value -= 1
value -= 1
print(value)
#=> 4


#33
bin(5)
#=> '0b101'


#34
a = [1,1,1,2,3]
a = list(set(a))
print(a)
#=> [1, 2, 3]



#35
'a' in ['a','b','c']
#=> True
'a' in [1,2,3]
#=> False
1 in [1,2,3]
#=> True

#36

a = [1,2,3]
b = [1,2,3]
a.append(6)
print(a)
#=> [1, 2, 3, 6]
b.extend([4,5])
print(b)
#=> [1, 2, 3, 4, 5]

abs(2)
#=> 2
abs(-2)
#=> 2

#38
a = ['a','b','c']
b = [1,2,3]
[(k,v) for k,v in zip(a,b)]
#=> [('a', 1), ('b', 2), ('c', 3)]


#39

d = {'c':3, 'd':4, 'b':2, 'a':1}
sorted(d.items())
#=> [('a', 1), ('b', 2), ('c', 3), ('d', 4)]




#40
class Car():
    def drive(self):
        print('vroom')


class Audi(Car):
    pass


audi = Audi()
audi.drive()

#41
s = 'A string with     white space'
''.join(s.split())
#=> 'Astringwithwhitespace'

s = 'A string with     white space'
s.replace(' ', '')
#=> 'Astringwithwhitespace'

a = 'Astringwithwhitespace'
a.replace('',' ')
' A s t r i n g w i t h w h i t e s p a c e '



#42 enumerate()
li = ['a','b','c','d','e']

for idx,val in enumerate(li):
    print(idx, val)
    
#=> 0 a
#=> 1 b
#=> 2 c
#=> 3 d
#=> 4 e

#43



a = [1,2,3,4,5]

for i in a:
    if i > 3:
print(i)

a = [1,2,3,4,5]

for i in a:
    if i > 3:
        pass
    print(i)

#=> 1
#=> 2
#=> 3
#=> 4
#=> 5

# Continue
for i in a:
    if i > 3:
    print(i)


for i in a:
    if i > 3:
        continue
    print(i)

#=> 1
#=> 2
#=> 3

for i in a:
    if i < 3:
        continue
    print(i)

#=> 3
#=> 4
#=> 5


#BREAK

for i in a:
    if i == 3:
        break
    print(i)   

#=> 1
#=> 2



#44 Convert the following for loop into a list comprehension
a = [1,2,3,4,5]
a2 = []
for i in a:
     a2.append(i + 1)
print(a2)
#=> [2, 3, 4, 5, 6]

ConvertTTTTTTTTTTTTTTT
a3 = [i+1 for i in a]
print(a3)
#=> [2, 3, 4, 5, 6]

#45
x = 5
y = 10
'greater' if x > 6 else 'less'
#=> 'less'
'greater' if y > 6 else 'less'
#=> 'greater'

#46
'123a'.isnumeric()
#=> False
'123'.isnumeric()
#=> True

#47
'123a'.isalpha()
#=> False
'a'.isalpha()
#=> True

'123a'.is()

#48
'123abc...'.isalnum()
#=> False
'123abc'.isalnum()
#=> True

#49
d = {'id':7, 'name':'Shiba', 'color':'brown', 'speed':'very slow'}
list(d)
#=> ['id', 'name', 'color', 'speed']

#50
small_word = 'potatocake'
big_word = 'FISHCAKE'
small_word.upper()
#=> 'POTATOCAKE'
big_word.lower()
#=> 'fishcake'

#51
li = ['a','b','c','d']
li.remove('b')
li
#=> ['a', 'c', 'd']

li = ['a','b','c','d']
del li[0]
li
#=> ['b', 'c', 'd']

li = ['a','b','c','d']
li.pop(2)
#=> 'c'
li
#=> ['a', 'b', 'd']

#52
# creating a list of letters
import string
list(string.ascii_lowercase)
alphabet = list(string.ascii_lowercase)
# list comprehension
d = {val:idx for idx,val in enumerate(alphabet)} 
d
#=> {'a': 0,
#=>  'b': 1,
#=>  'c': 2,
#=> ...
#=>  'x': 23,
#=>  'y': 24,
#=>  'z': 25}


try:
    # try to do this
except:
    # if try block fails then do this
finally:
    # always do this

try:
    val = 1 + 'A'
except:
    val = 10
finally:
    print('complete')
    
print(val)
#=> complete
#=> 10

# Dict
my_dict = {'name': 'Hugh Jackman', 'age': 50, 'films': ['Logan', 'Deadpool 2', 'The Front Runner']}
my_dict['age']

#Lamda
(lambda x, y, z: (x+y) ** z)(3,2,2)
#>25


#List comprehensions
old_list = [1, 0, -2, 4, -3]
new_list = [x**2 for x in old_list if x > 0]
print(new_list)
#>>> [1,16]

#List indexing
list = [2, 5, 4, 7, 5, 6, 9]
print (list[-1])
#> 9

text = "I love data science"
print (text[-3])
#> n\

#Pandas library
import pandas as pd
emloyees = pd.read_csv('HR.csv')

employees.isna()

emploees.info()


employees[['Department', 'Age']]

employees['Active'] = 1
employees.head()

employees['Age'].hist()


1. load library
2. create numpy matrix
3. Trace
import numpy as np
matrix = np.array([[1, 2, 3],
                   [4, 5, 6],
                   [7, 8, 9],
                   [10, 11, 12]])
print()
print('Calculate the tracre of the matrix: ',
       matrix.diagonal().sum())


 import numpy as np

 matrixA = np.array([[1, 2, 3, 23],
                       [4, 5, 6, 25],
                       [7, 8, 9, 28],
                       [10, 11, 12, 41]])


 print(); print(matrixA.flatten())

 [ 1  2  3 23  4  5  6 25  7  8  9 28 10 11 12 41]

#Determinant
 import numpy as np
# Create matrix
matrixA = np.array([[1, 2, 3, 23],
                   [4, 5, 6, 25],
                   [7, 8, 9, 28],
                   [10, 11, 12, 41]])
matrixB = np.array([[2, 3, 4],
                   [5, 6, 9],
                   [7, 8, 1]])
# Return determinant of matrix
print(); print(np.linalg.det(matrixA))
print(); print(np.linalg.det(matrixB))

#Trace of Matrix
import numpy as np
# Create matrix
matrix = np.array([[1, 2, 3],
                   [4, 5, 6],
                   [7, 8, 9],
                   [10, 11, 12]])
# Calculate the tracre of the matrix
print()
print('Calculate the tracre of the matrix: ',
       matrix.diagonal().sum())


#DIagonal of matrix
import numpy as np
# Create matrix
matrix = np.array([[1, 2, 3, 23],
                   [4, 5, 6, 25],
                   [7, 8, 9, 28],
                   [10, 11, 12, 41]])
# Return diagonal elements
print()
print(matrix.diagonal())
# Calculate the tracre of the matrix
print()
print(matrix.diagonal().sum())


#Inverse of matrix
import numpy as np
matrix = np.array([[1, 2, 3, 23],
                   [4, 5, 6, 25],
                   [7, 8, 9, 28],
                   [10, 11, 12, 41]])
Inv = np.linalg.inv(matrix)
print()
print(Inv)



#How to convert a dictionary to a matrix or nArray in Python?
from sklearn.feature_extraction 
import DictVectorizer

data_dict = [{'Pen': 2, 'Pencil': 4},
                 {'Pen': 4, 'Pencil': 3},
                 {'Pen': 1, 'Eraser': 2},
                 {'Pen': 2, 'Eraser': 2}]
print(data_dict)

dictvectorizer = DictVectorizer(sparse=False)
features = dictvectorizer.fit_transform(data_dict)
print(features)

feature_name =dictvectorizer.get_feature_names()
print(feature_name)

# reshape & change dimension of a matrix

import numpy as np
# Create a 4x3 matrix
matrix = np.array([[1, 2, 3],
                   [4, 5, 6],
                   [7, 8, 9],
                   [10, 11, 12]])
# Reshape matrix into 2x6 matrix
print()
print(matrix.reshape(2, 6))
print()
print(matrix.reshape(3, 4))
print()
print(matrix.reshape(6, 2))

#select array
import numpy as np

vector = np.array([1, 2, 3, 4, 5, 6])
# Select second element
print()
print(vector[1])


# Create matrix
matrix = np.array([[1, 2, 3],
               [4, 5, 6],
               [7, 8, 9]])
# Select second row, second column
print()
print(matrix[1,1])

# Create Tensor
tensor = np.array([
                [[[1, 1], [1, 1]], [[2, 2], [2, 2]]],
                [[[3, 3], [3, 3]], [[4, 4], [4, 4]]]
              ])
# Select second element of each of the three dimensions
print()
print(tensor[1,1,1])

# Create vector and matrix
import numpy as np
# Create vector
vector = np.array([1, 2, 3, 4, 5, 6])
print()
print("Original Vector: \n", vector)
# Tranpose vector
V = vector.T
print("Transpose Vector: \n", V)
# Create matrix
matrix = np.array([[1, 2, 3],
               [4, 5, 6],
               [7, 8, 9]])
print()
print("Original Matrix: \n", matrix)
# Transpose matrix
M = matrix.T
print("Transpose Matrix: \n", M)

5/2
-5//2
-5//3


-4.1//2
5.6/2

#Append
a = [1,2,3,4,5]
a.append(6)
print(a)

b = [1,56,8,4,6, 'value']
b.append('value')
print(b)

#Extend
a = [1,2,3,4,5]
a.extend('2')
print(a)

a = [1,2,3,4,5]
a.extend(8)
print(a)


a = [1,2,3,4,5]
a.extend(b)
print(a)


#remove
a = [1,2,3,4,5,10]
a.remove(10)
a
a = [1,2,3,4,5,10]
a.remove("3")
a

a = ["A", "B"]
a.remove("A")
a

b = [1,56,8,4,6, 'value']
b.pop(0)
print(b)

b = [1,56,8,4,6, 'value']
b.pop()
print(b)

#count


#open()
a = open("asdahuf","w")
print(a.writable())
a.close()



a = open("asdahuf","r")
print(a.readable())
a.close()


#if-else
if True:
    this
else:
    that

if AA or BB:
    this
else:
    that

#if-elif-else
#not

if AA or BB:
    1 + +
elif AA and not BB:
    2 + -
elif not AA and BB:
    3 - +
else:
    4 otherwise

AA = True
BB = False
if not AA or BB:
    print("BB")
else:
    that


#Setup dictionary
aaa = {"1": "something", "2": "something2"}
aaa[1]
aaa["1"]

aaa.get("33","testing")
aaa

aaa.get("33",)



#while loop

while this condition True:
    do this 
    then REPEAT
else:
    do this when False



#for loop
friends = ["a", "b", "c"]
for wtf in friends:
    print(friends)

friends = ["a", "b", "c"]
for i in friends:
    print(friends)

friends = [1,2,3,4,"5253523"]
for i in friends:
    print(friends)

friends = "AAA"
for i in friends:
    print(friends)

friends = "A"
for wtf in friends:
    print(friends)

friends = 123
for wtf in friends:
    print(friends)

for every index in something:
    do this

"123" = 3 index
[1,2,3,4,"5253523"] = 5 index

##Matrix
matrixA = [
    [1,2,3],
    [4,5,6],
    [7,8,9]
]
print(matrixA)
print(matrixA[2][2])

friends = [1,2,3,4,["abc","777","pop"]]
friends[4]

friends[[4]]

friends[4][0]

friends[4][[0]]

friends[[4]][0]

friends[4][0][1]

friends[0:4]

##string
"don't"
"\"yes\", i said"

print("""\
Usage: thingy [OPTIONS]
     -h                        Display this usage message
     -H hostname               Hostname to connect to
""")

friends = [1,2,3,4,["abc","777","pop"]]
friends[0:99]

range(10)
print(range(10))

#join
','.join('12345')

#split
'1,2,3,4,5'.split(',')

#Fizzbuzz
# 0-50
for i in range(51):
    if i % 3 == 0 and i % 5 == 0:
        print("fizzbuzz")
    elif i % 5 == 0:
        print("buzz")
    elif i % 3 == 0:
        print("fizz")
    else:
        print(i)

# 1-50
for i in range(1,51):
    if i % 3 == 0 and i % 5 == 0:
        print("fizzbuzz")
    elif i % 5 == 0:
        print("buzz")
    elif i % 3 == 0:
        print("fizz")
    else:
        print(i)



#factorial
import math as math
math.factorial()

#interpolation
name = 'aa'

print(f'TESTINT{name}')

print('My {}'.format(name))



#Given an array
#k largest elements

#Ascending order
def klargestASC(array,k,n):
    array.sort()
    for i in range(n-k, n):
        print(array[i])

array = [1,23,4,500,9999]
print(klargestASC(array,3,len(array)))
klargestASC(array,3,len(array))


#Descending order
def klargestDESC(array,k):
    array.sort(reverse= True)
    for i in range(k):
        print(array[i])


array = [1,23,4,500,9999]
k = 4
print(klargestDESC(array,k))





