#Dictionary
mydict = {"name":"Max", "age":28, "city":"Palo ALto"}
print(mydict)

for key in my mydict.keys():
    print(key)

for value in my mydict.values():
    print(value)

for key, value in mydict.items():
    print(key,value)

###copyting dict
##NOTE this will shit bed
mydict_copy = mydict 

#correct way
mydict_copy = dict(mydict)
mydict_copy = mydict.copy()

mydict_copy['email'] = "edmond@com"
print(mydict_copy)
print(mydict)

#### Updating dictionary
mydict = {"name":"Max", "age":28, "city":"Palo ALto"}
mydict2 = {"name":"Max", "age":28, "email":"edmond@gmail"}

#All existing key got overwritten
mydict.update(mydict2)
print(mydict)

######
####
mydict = {3:9, 6:36, 9:81}
print(mydict)
value = mydict[3]
print(value)

# Always possible
mytuple = (8,7)
mydict = {mytuple: 15}
print(mydict)

----------------------------------------------------------------------------------------------------

set('hello')



odds = {1,3,5,7,9}
evens = {0,2,4,6,8}
primes = {2,3,5,7}

u = odds.union(evens)
u = odds.intersection(evens)

setA = {1,2,3,4,5,6,7,8,9}
setA
setB = {1,2,3,10,11,12}
setB

v = setA.update(setB)
print(v)
print(value)
print(setA.difference_update(setB))
print()



######
##### Strings

#remove all white space
my_string = '    Hello World    '
my_string.strip()


my_string = 'Hello World'
my_string.startswith(my_string)
my_string.endswith(my_string)
my_string.find('H')
my_string.count('o')
my_string.replace('Hello' , 'FKKKK')
#if fails
#return my_string


#splitting string into a list
my_string = 'how re you doing'
mylist = my_stirng.split()
mylist = my_string.split(" ") #default
my_string = 'how,re,you,doing'
mylist = my_string.split(",") # , is now the delimiter
print(mylist)


#List back to string (always .join methond)
my_string = 'how,re,you,doing'
mylist = my_string.split(",") # List here
newstring = ''.join(mylist) #back to string
print(newstring) # concatenate 

newstring2 = ' '.join(mylist) #with space
print(newstring2) 


# .join method is the fastest way
# join = concatnate 
from timeit import default_timer as timer
timeit.Timer
mylist = ['a'] * 1000000
print(mylist)

start = timer()
mystring = ''.join(mylist)
stop = timer()
print(stop-start)

# On the other hand
# using not .join
start = timer()
mystring = ''
for i in mylist:
    mystring += i
stop = timer()
print(stop-start)





#% old format

#%s string value
var = "Tom"
mystring = "the variable is %s" % var
print(mystring)
#%d decimal value
var = 3
mystring = "the variable is %d" % var
print(mystring)
#%f floating point value
var = 9.99999999
mystring = "the variable is %f" % var
print(mystring)
#%.xf specify decimal place
var = 9.99999999
mystring = "the variable is %.2f" % var
print(mystring)


#.format()  old too
var =9.999
mystring - "the variable is {}".format(var)
print(mystring)

#specify decimal place
var =9.999
var = 1991919191
mystring - "the variable is {:.2f} 
and {}".format(var, var2)
print(mystring)



#f-string newest (concise and faster)
var =9.999
var = 1991919191
mystring - f"the variable is {var} 
and {var2}"
print(mystring)


---------------------------------------

####
####
## Collection
# Counter (store elements as dict key)
from collections import Counter
a = "aaabbbcccc"
mycounter = Counter(a)
print(mycounter)
# general
print(mycounter.items())
print(mycounter.keys())
print(mycounter.values())
# most common element
print(mycounter.most_common(1))
# 2 most common element
print(mycounter.most_common(2))
# 1st tuple
print(mycounter.most_common(1)[0])
# 1st element
print(mycounter.most_common(1)[0][0])
# show all elements
# Note must use list
print(list(mycounter.elements()))


#namedtuple
from collections import namedtuple
# (class name, whatever fields)
Point = namedtuple('Point', 'x,y')
pt = Point(1, -4)
print(pt)
print(pt.x,pt.y)



# OrderedDict
# now 3.7 will remeber the order in normal dict
from collections import OrderedDict
odict = OrderedDict()
odict['b'] = 2
odict['c'] = 3
odict['d'] = 4
odict['a'] = 1
print(odict)


#defaultdict
# otherwise normal dict will show KeyError
from collections import defaultdict
d = defaultdict(int)
d['a'] = 1
d['b'] = 2
print(d['a'])
print(d['c'])

d = defaultdict(float)
print(d['c']) # 0.0

d = defaultdict(list)
print(d['c']) # empty list []

#deque
from collections import deque
d   = deque()

d.append(1)
d.append(2)

d.appendleft(3) # add at the left side
print(d)

d.popleft() #delete the left
d.extendleft([4,4,4]) # extend at the left

d.rotate(1) # every element move 1 to right
d.rotate(2) # move 2 to right
d.rotate(-1) # to the left

------------------------------------------------------

# itertools module
## product
from itertools import product
a = [1,2]
b = [3]
prod = product(a,b)
print(prod)
print(list(prod)) # see all elements

# repeat 
prod = product(a,b, repeat = 2) 
print(list(prod)) # see all elements


## permutations = return all possible as
## input
from itertools import permutations
a = [1,2,3]
perm = permutations(a)
print(list(perm))

perm = permutations(a,2) # with length of 2
print(list(perm))

## combinations
from itertools import combinations
a = [1,2,3,4]
comb = combinations(a,2)
print(list(comb))

from itertools import combinations, combinations_with_replacement
a = [1,2,3,4]
combr = combinations_with_replacement(a,2)
print(list(combr))

## accumulate = add up previous all
from itertools import accumulate
a = [1,2,3,4]
acc = accumulate(a)
print(a)
print(list(acc))

# taking max value each
a = [1,3,99,10,109]
acc_f = accumulate(a, func=max)
print(a)
print(list(acc_f))

## groupby
from itertools import groupby

def smaller_than_3(x):
    return x < 3

a = [1,2,3,4]
group_obj = groupby(a, key=smaller_than_3)
print(group_obj)

for key, value in group_obj:
    print(key, list(value))



# infinite iterators 
# count cycle repeat
from itertools import count, cycle,repeat

for i in count(10):
    print(i)
    if i == 15:
        break


a = [1,2,3]
for i in cycle(a):
    print(i)
    break

for i in repeat(1,10):
    print(i)





----------------------------------------------------
#map(func, sequence)
a = [1,2,3,4,5]
b = map(lambda x: x*2 , a)
print(list(b))
# Method2 list comprehension (better)
c = [x*2 for x in a]
print(c)


# filter(func, sequence)
# show all elements which func is TRUE
a = [1,2,3,4,5,6]
b = filter(lambda x: x%2==0, a)
print(list(b))
# Method2 list comprehension (better)
c = [x for x in a if x%2==0]

# reduce(func,sequence)
# repeating apply the func and return a single value
from functools import reduce
a = [1,2,3,4,5,6]

# need 2 arguments x,y
product_a = reduce(lambda x,y: x*y, a)
print(product_a)


--------------------------------------

#### logging module
# only last 3 show
import logging
logging.debug('show')
logging.info('show')
logging.warning('show')
logging.error('show')
logging.critical('show')

#change basic
#check website

# create own internal logger
# logger with module name
logger = logging.getLogger(__name__)
logger.info('hello from testing module')

# create handler
streamhan = logging.StreamHandler()
filehan = logging.FileHandler('file.log')

# setting level and format
streamhan.setLevel(logging.WARNING)
filehan.setLevel(logging.ERROR)

streamformat = logging.Formatter('')
filefo

------------------------------
## random number 

import random
# uniform(lowerbound,upperbound)
a = random.uniform(1,10)
#randint(lowerb, upperb) = including upperbound
a = random.randint.(1,10)
10
#randrange(lowerb,upperb) = not including upperb
a = random.randrange(1,10)

# normalvariate(mean,s.d.)
a = random.normalvariate(0,1)

#choice(x)
mylist = list("ABCDEFGH")
a = random.choice(mylist)

# sample(x , number of elements) = unique element
mylist = list("ABCDEFGH")
a = random.sample(mylist, 3)
print(a)

# choices(x, # of times) = pick multiple time
mylist = list("ABCDEFGH")
a = random.choices(mylist, k=3)
print(a)
['F', 'D', 'D']

# shuffle(x) = shuffle and change list instead care!!
mylist = list("ABCDEFGH")
random.shuffle(mylist)
print(mylist)


# random.seed(value) = pseudo-random numbers because 
# reproducible to reproduce data  
# DONT USE FOR SECURITY

#1st seed
random.seed(1)
print(random.random())
print(random.randint(1,10))

# different seed = different
random.seed(1)
print(random.random())
print(random.randint(1,10))

# For secrets use secrets instead of random
import secrets
#ranbelow(lowerb,upperb) = not including upperb
a = secrets.ranbelow(1,10)
3

#ranbits() = 1111 = 1+2+4+8 = 15 
a = secrets.randbits(4) # 0-15

#choice() = not reproducible
a = secrets.choice(mylist)


#NUMPY
# seed working too
np.random.seed(1)

import numpy as np
#np.random.rand(dimension)
a = np.random.rand(3) #1d array with 3 elemnts

#NUMPY

#np.random.rand(dimension)
a = np.random.rand(3) #1d array with 3 elemnts
print(a)
[0.09038764 0.09925056 0.6040674 ]


#rp.random.randint(lowerb, upperb,size) =
a = np.random.randint(0,10,3)
print(a)
[3 8 0]

#higher dimension using tuple
a = np.random.randint(0,10,(3,4))
print(a)
[[1 2 7 2]
 [7 1 6 6]
 [6 2 7 1]]

#np.array
ar = np.array([[1,2,3], [4,5,6], [7,8,9]])
print(ar)
[[1 2 3]
 [4 5 6]
 [7 8 9]]
#np.shuffle array
np.random.shuffle(ar)
print(ar)
[[4 5 6]
 [1 2 3]
 [7 8 9]]



------------------------------------------

# Decorators (confusing)
# function decorator

#1st class object can be defined 
@myd
def dosomething():
    pass


## example
def startenddecorator(func):

    def wrapper():
        print('Start')
        func{}
        print('End')
    return wrapper

def printname():
    print('Alex')

printname()

printname = startenddecorator(printname)

printname()



###Add5

import functools

def startenddecorator(func):

    @function.wrap(function)
    def wrapper(*args,**kwargs):
        print('Start')
        func{*arg,**kwargs}
        print('End')
        return result
    return wrapper



@startenddecorator
def add5(x):
    return x + 5

add5(10)

result = add5(10)
print(result)

print(help(add5))
print(add5.__name__)


--------------------------------------------

# Generators
# function that return an object that can be iterated over
# MEMORY EFFICIENT = save a lot of memory when large data

# special : generate the items only one at a time and only when
# you ask for it

## google it

def 
## exmaple
def mygenerator():
    yield 1
    yield 2
    yield 3

g = mygenerator()
print(g)
<generator object mygenerator at 0x0000010E538E2740>

for i in g:
    print(i)

# stop at 1, stop at 2, stop at 3, stopiteration then
# stopiteration shows = always raise if it has no yield
value = next(g)
print(value)


# next example
def mygenerator():
    yield 1
    yield 2
    yield 3

g = mygenerator()

#1+2+3
print(sum(g))
#sort
sorted(g)


# another function
def countdown(num):
    print('Starting')
    while num > 0:
        yield num
        num -= 1

cd = countdown(4)

value = next(cd)
print(value)

#4.3.2.1, stopiteration
print(next(cd))

### BIGBIG advantage
#
import sys
def firstn(n):
    nums = []
    num = 0
    while num < n:
        nums.append(num)
        num += 1 #update current num
    return nums

#0 to 9
print(firstn(10))

# since num store in list = lots of memory
print(sum(firstn(10)))

# Use generator instead

def firstn_generator(n):
    num = 0
    while num < n:
        yield num
        num += 1 # update

    

# SAVE TONS OF MEMORY!!!!
print(sys.getsizeof(firstn(100000))) #800984 bits
print(sys.getsizeof(firstn_generator(100000))) # 112 bits


# Practice
# Fibonacci series

def mygenerator():
    a,a2 = 0, 1
    while a < limit
        yield a
        a,a2 = a2, a+a2

fib = fibonacci(30)
for i in fib:
    print(i)
1
3
5
8
13
21


#  exmaple 2
# quick generator function
import sys
mygenerator = (i for i in range(10000) if i % 2 == 0)
for i in mygenerator:
    print(i)
0
2
4
6
8
print(list(mygenerator))
print(sys.getsizeof(mygenerator))
112
# normal list size
mylist = [i for i in range(10000) if i % 2 == 0]
print(mylist)
print(sys.getsizeof(mylist))
41880









