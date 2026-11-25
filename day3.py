from abc import ABC , abstractmethod
from dataclasses import dataclass, field
## class and object 

class home:
   

    def sum(self, a, b):
        print("self is:", self)
        return a + b

# home1=home
home1=home()
print(home1.sum(10, 20) )

##constructor 

class student:
    def __init__(self, name, age):
        self.name = name
        self.age = age

    def display(self):
        print("Name:", self.name)
        print("Age:", self.age)

# Creating an object of the student class
student1 = student("Yash", 20)
student1.display()

## instance variable and class variable
wheelss = 6
class car:
    
    wheels = 4  # class variable

    def __init__(self, color, model):
        self.color = color  # instance variable
        self.model = model  # instance variable

    def display(self):
        print("Color:", self.color)
        print("Model:", self.model)
        print("Wheels:", car.wheels)  # Accessing class variable
        print("Global Wheels:", wheelss)  # Accessing global variable
# Creating an object of the car class
car1 = car("Red", "Sedan")
car1.display()

## methods and dunder method

## local 
class car :
    def __init__(self, model,colour):
        self.model=model
        self.colour=colour
        
    def models(self ):
        return f"model of car is {self.model} and colour of car is {self.colour}"

car1=car("2026", "white")
car2=car("2025", "black")
print(car1.models())
print(car2.models())

## class method and static method

class school:
    
    school_name = "ABC School"  # Class variable

    def __init__(self, student_name):
        self.student_name = student_name  # Instance variable

    @classmethod
    def change_school_name(cls, new_name):
        cls.school_name = new_name  # Modifying  class variable

    @staticmethod
    def greet():
        return "Welcome to the school!"  # Static method
print("School Name:", school.school_name)  # Accessing class variable
school.change_school_name("XYZ School")  # Calling class method
print("School Name:", school.school_name)  # Accessing class variable

## object creation using class method and static method
class object_creation:
   def __init__(self, name, age):
       self.name = name
       self.age = age
    
   @classmethod 
   def create_object(cls, data):
       name ,age=data.split(",")
       return cls(name, int(age))

obj = object_creation.create_object("John,25")  # Creating an object using class method
print("Name:", obj.name)
print("Age:", obj.age)

class calculator:
   

    @staticmethod
    def multiply(num1, num2):
        return num1 * num2
print("Multiplication:", calculator.multiply(5, 10))  # Calling static method

## inheritance and method overriding
class employee:
    def __init__(self, name, salary):
        self.name = name
        self.salary = salary
    def work(self):
        print(f"{self.name} is working and earning {self.salary}.")

class developer(employee):
    def __init__(self, name, salary, programming_language):
       super().__init__(name, salary)
       self.programming_language = programming_language

    # def work(self):
    #     print(f"{self.name} is working as a developer and earning {self.salary}.")    
# developer1 = developer("Alice", 5000, "Python")
# developer1.work()
employee1 = employee("Bob", 4000)
developer1 = developer("Alice", 5000, "Python")  
developer1.work()


# print(f"{developer1.name} is a developer and knows {developer1.programming_language}.")
# print(f"{employee1.name} is working and earning {employee1.salary}.")
# employee1 = employee("Bob", 4000)
# employee1.work()

## polmorphism 

class car:
    
    def start(self):
        print("Car is starting.")

class bike:

     def brake(self):
            print("apply.")
    
    # def start(self):
    #     print("Bike is starting.")

class bus:

    def start(self):
        print("Bus is starting.")

def start_vehicle(vehicle):
    vehicle.start() 

class train:
    def start(self):
        print("Train is starting.")

car1 = car()
bike1 = bike()
bus1 = bus()
train1 = train()

start_vehicle(car1)
# start_vehicle(train1)


## encapsulation
 
class bank_account:
    __accountbalance= 1000

    def __init__(self , number):
         self.__number=number

transaction1=bank_account(123456)
print("Account Number:", transaction1._bank_account__number)
transaction1.__number=2222
print("Account Number:", transaction1.__number)
transaction1.__accountbalance=2000
# print("Account Balance:", bank_account.__accountbalance)
print(transaction1._bank_account__number)

# @propety 
class emp:

    def __init__(self,number):
        self.__number=number

    @property
    def salary(self):
        return self.__number

    @salary.setter
    def salary(number):
        if number>= 0:
            selg.__number=number
        else:
            return "salary is not set as negative"

emp1=emp(20000)

print(emp.salary)
emp.salary=30000
print(emp.salary)


# abstract

class shape(ABC):

    @abstractmethod
    def area(self):
        pass

class rectrangle(shape):

    def __init__(self , hight, width):
        self.hight=hight
        self.width= width

    def area(self):
        return self.hight*self.width

r1=rectrangle(10,20)
print(r1.area())

#data class
@dataclass(frozen=True)
class product:
    name:str
    price:int
    quentity:int=1
    tag:list = field(default_factory=list)


p1=product("mobile",20000,tag=["best","no1"])
p2=product("watch",5000,2,["smart","handband"])
print(p1)
print(p2)