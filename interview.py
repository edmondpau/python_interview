 character_name = "John"
character_age = "35"
print("AAAA" + character_name + "BBB    BB")

character_name = "Tom"
character_age "50"
print("THere once as a man named" + character_name + ",")
print("but didn't like being" + character_age + ".")

is_male = False

print("edmond\nPau")
print("edmond\"Pau")
print("edmond\Pau")

phrase = "Edmond Pau"a0
print(phrase.)
print(phrase.lower() + " is cool")
print(phrase.upper() + " is Fking good")
print(phrase.isupper())
print(phrase.otherfunctions)

phrase = "Edmond"
print(phrase.upper().isupper())
print(len(phrase))

phrase = "Edmond"
          0123
print(phrase[3])

phrase = "Edmond"
print(phrase.index("E"))
print(phrase.index("dmond"))

phrase = "Edmond Pau"
print(phrase.index("E"))
print(phrase.index("dmond"))
print(phrase.)replace("edmond", "AA")


## Numbers & Input
print(pow(3,2))
        min
        max
        abs
        round
        sqrt()
        floor()
        ceil()
        .
        .
        .
        .
        .

name = input("Enter your name: ")
age = input("Enter your age: ")
print("Hello" + name + "!" + "You are" + age)

num1 = input("Enter a number: ")
num2 = input("Enter another number: ")
result = num1 + num2
print(result)
result = float(num1) + float(num2)

color = input("Enter a color: ")
plural_noun = input("Enter a Plural noun: ")
celebrity = input("Enter a celebrity: ")
print("Roses are " + color)
print(plural_noun + " are blue")
print("I love " + celebrity)





### Lists
### List function
### Tuples
friends = ["Kevin", "Amy", "Cat"]
print(friends[0])

list2 = [1,2,3,4,5]
friends = ["Kevin", "Amy", "Cat"]
friends.extend(list2)
print(friends[1:])


friends = ["Kevin", "Amy", "Cat", "TT", "Benz"]
friends.insert(1, "22")
print(friends)

friends = ["Kevin", "Amy", "Cat", "TT", "Benz"]
friends.remove("Amy")
print(friends)

#pop
friends = ["Kevin", "Amy", "Cat", "TT", "Benz"]
friends.pop("Amy")
print(friends)

#copy()
friends = ["Kevin", "Amy", "Cat", "TT", "Benz"]
friends2 = friends.copy()
print(friends2)

coordinates = (1,5)
coordinates[1] = 10

# FILES
### Reading
### Writing
### Appending

open("employees.txt", "r")
open("employees.txt", "w")
open("employees.txt", "a")
open("employees.txt", "r+")

employee_file = open("employees.txt", "w")
print(employee_file.readable())
employee_file.close()

employee_file = open("employees.txt", "r")
print(employee_file.read())
employee_file.close()

employee_file = open("employees.txt", "r")
print(employee_file.readline())
print(employee_file.readline())
employee_file.close()

employee_file = open("employees.txt", "r")
print(employee_file.readlines())
employee_file.close()

employee_file = open("employees.txt", "r")
print(employee_file.readlines()[1])
employee_file.close()

employee_file = open("employees.txt", "r")
for employee in employee_file.readlines():
    print(employee)
employee_file.close()

employee_file = open("aa", "bb")
employee_file.write("MOTHER FK")
employee_file.close()

employee_file = open("aa", "bb")
employee_file.write("\n\n\n\nMOTHER FK")
employee_file.close()

employee_file = open("employees.txt", "w")
employee_file.write("\nKelly Customer Services")
employee_file.close()

### FUNCTIONS

def say_hi ():
    print("Hello fker")
print("A")
say_hi()
print("B")

def functionA (name,age):
    print("Hello " + name + " you're " + str(age))
functionA("A", 3)
functionA("B", 6)

def own_cube(num) :
    num*num*num
print(cube(3))

def cube(num) :
    return num*num*num


### Using Git
# TO TEST pushing small commits
