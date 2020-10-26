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
