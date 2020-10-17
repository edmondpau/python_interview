character_name = "John"
character_age = "35"
print("AAAA" + character_name + "BBB    BB")

character_name = "Tom"
character_age = "50"
print("THere once as a man named" + character_name + ",")
print("but didn't like being" + character_age + ".")

is_male = False

print("edmond\nPau")
print("edmond\"Pau")
print("edmond\Pau")

phrase = "Edmond Pau"
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


############################################
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
    print("A")
print(cube(3))


### If statements
is_dick = False
is_pussy = False

if is_dick or is_pussy:
    print("You are a dick")
else:
    print("BB")


### elif bug but the code is good
if is_dick and is_pussy:
    print("Get fk")
elif not (is_dick) and (is_pussy):
    print("minus plus")
elif is_dick and is_pussy:
    print("WOWOOWO")
else:
    print("Double negative")


def max_num(num1, num2, num3)
    if num1 >= num2 and num1 >= num3:
        print("1 is pussy")
        return num1
    elif num2 >= num1 and num2 >= num3:
        print("2 OP")
        return num2
    else:
        print("3")
        return num3

print(max_num(300,1,20))


## Dictionary
monthconversions = {
    "jan" : "jannn",
    "feb" : "febbb"
}
print(monthconversions["feb"])
print(monthconversions.get("dec","WTF"))


########################################
##3 While loop
i = 1
while i <= 10:
    print(i)
    i += 1
else:
    print("bye")


secret_word = 'Edmond'
guess = ""

while guess != secret_word:
    guess = input('Enter Word')
print("WINN")

secret_word = 'Edmond'
guess = ""
guess_count = 0
guess_limit = 3
out_of_guesses = False
while guess != secret_word and not(out_of_guesses):
    if guess_count < guess_limit:
        guess = input("Enter STH")
        guess_count += 1
    else:
        out_of_guesses True
if out_of_guesses:
    print("fuck off bye")
else:
    print("havea a one night stand")


########################################
#### For loop

for letter in "AA fancy houSE":
    print(letter)

for index in range(3,10):
    print(index)

friends = ["11", "2222", "33333"]
for whatevername in friends:
    print(whateveRname)

for index in range(len(friends)):
    print(friends[index])
## equals to
    friends[1]
    friends[2]
    friends[3]

# for loop example
for index in range(5):
    if index == 0:
        print("first iteration")
    else:
        print("Others")

# exponential function selfmade

print(2**3)

def raise_to_power(base_num, power_num):
    result = 1
    for index in range(power_num):
        result = result * base_num
    return result

print(raise_to_power(3,3))


##########

## 2D lists loop
#### LISTS
number_grid = [
    [1,2,3],
    [4,5,6],
    [7,8,9],
    [0]
]

print(number_grid[2][1])



for row in number_grid:
    print(row)


for row in number_grid:
    print(row)


for row in number_grid:
    for col in row:
        print(col)



def translate(phrase):
    translation = ""
    for letter in phrase:
        if letter in "AEIOUaeiou":
            translation = translation + "fuck"
        else:
            translation = translation + letter
    return translation

print(translate(input("Enter a phrase: ")))


def translate(phrase):
    translation = ""
    for letter in phrase:
        if letter.lower() in "aeiou":
            translation = translation + "FUCK"
        else:
            translation = translation + "fuck"
    else:
        translation = translation + letter
    return translation

print(translate(input("Enter a phrase: ")))





###### Try/Except Block 
### Protect program

# Avoid PROGRAM crash
# try a piece of code before crashing


try:
    number = int(input("Enter a number"))
    print(number)

    value = 0/0
except ValueError:
    print("Noob program")
except ZeroDivisionError:
    print("MATH FUCK")


except ZeroDivisionError as err:
    print(err)
    print("Math Fuck")


### IMPORTING MODULES
# importing functionality from EXTERNAL files

import useful_tools
print(useful_tools.roll_dice)

## 3rd party modules
# PYTHON-DOCX
# Pypl.org

pip install python-docx
import docx
docx.end=

pip uninstall python-docx





############## CLASSES & OBJECTS
# Create OWN DATA type --> class
# Something cant be represented

class Student:

    def __init__(self, name, major, gpa, is_on_probation)
        self.name = name
        self.major = major
        self.gpa = gpa
        self.is_on_probation = is_on_probation

from Student import Student

student1 = Student("Jim","Business", 3.1, False)

print(student1.name)
print(student1.is_on_probation)


class Student:

    def __init__(self, name, major, gpa, is_on_probation)
        self.name = name
        self.major = major
        self.gpa = gpa
        self.is_on_probation

    def on_honor_roll(self):
        if self.gpa > 3.5:
            return True
        else:
            return False


######Multiple choice Quiz (Classes & IF & LOOP)

from Question import Question

question_prompts = [
    "What color are FUCK?\n(a) Red/Green\n(b) Purple",
    "What color are pussy?\n(a) Red/Green\n(b) Purple",
    "What color are BITCH?\n(a) Red/Green\n(b) Purple"
]

questions = [
    Question(question_prompts[0], "b"),
    Question(question_prompts[0], "a"),
    Question(question_prompts[0], "b"),
]


def run_test(questions):
    score = 0
    for question in questions:
        answer = input(question.prompt)
        if answer == question.answer:
            score += 1


print("You got" + str(score) + "/" + str(len(questions)) + "correct")

run_test(questions)





#### Class
class Chef:

    def make_chicken(self):
        print("The chef makes a chicken")

    def make_salad(self):
        print("The chef makes salads")
    
    def make_special_dish(self):
        print("BBQ ribs")

from Chef import Chef

class ChineseChef(Chef):

# Inside of ChineseChef
# I am able to use all FUNCTIOLNS inside of Chef

def make_salad(self):
    print("The chef makes a salad")

def make_special_dish(self):
    print("The chef makes bbq ribs")







