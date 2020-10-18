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