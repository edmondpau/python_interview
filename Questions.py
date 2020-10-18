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


#40
class Car():
    def drive(self):
        print('vroom')


class Audi(Car):
    pass


audi = Audi()
audi.drive()