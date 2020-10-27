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
print()