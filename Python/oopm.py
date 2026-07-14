#OOPM
'''object orieneted programming
OOPM is mapping real world entities into programming world.
It is a programming paradigm that uses "objects" to design software.'''

'''class is a blueprint or template for creating objects.
It defines the properties (attributes) and behaviors (methods) that the objects created from the class. We create one single class and then create multiple objects from that class.'''

'''Class is a blueprint of an object and object is an instance of a class.'''

# class Student:
#     subject="Python"
#     college="ABC"
#     year="4th year"

# stu1 = Student()
# stu2 = Student()
# print(stu1.subject, stu1.college, stu1.year) 
# print(stu2.subject, stu2.college, stu2.year) 

# . is used to print the properties of the student class

'''Constructor:
A constructor is a special method in a class that is automatically called when an object of the class is created.
It is used to initialize the attributes of the object. In Python, the constructor method is defined using the __init__() method.'''

'''The init method is used to initialize the object's attributes with specific values when the object is created.
Init is called every time an object is created from a class and allows us to set initial values for the object's properties.'''

# class Student:
#     def __init__(self, name, cgpa): #self is used to refer to the current instance of the class. This is a parametized constructor
#         self.name = name
#         self.cgpa = cgpa

#     def get_cgpa(self):
#         return self.cgpa

# stu1=Student("Rahul", 8.5) 
# stu2=Student("Urvashi", 9.0) 
# stu3=Student("Aakash", 7.8) #the parentheses are used to call the constructor method

# print(f"{stu1.name} has CGPA = {stu1.get_cgpa()}")
# print(f"{stu2.name} has CGPA = {stu2.get_cgpa()}")
# print(f"{stu3.name} has CGPA = {stu3.get_cgpa()}")


'''Types of constructors:
1. Default constructor: A constructor that takes no parameters and initializes the object with default values i.e self .
2. Parameterized constructor: A constructor that takes parameters to initialize the object with specific values. It can accept one or more arguments.'''

'''Attribues
There are 2 types of attribute namely: class attribute and instance attribute.
1. Class attribute: A class attribute is shared by all instances of the class. It is defined within the class but outside any methods. It is accessed using the class name or through any instance of the class.
Class attribute belongs to the class itself and is shared among all instances of the class.
2. Instance attribute: An instance attribute is specific to each instance of the class. It is defined within the constructor method (init) using the self parameter. Each instance of the class can have its own unique values for instance attributes.
Instance attribute belongs to the specific instance of the class and is not shared among other instances. 
These are instance which belong to the object and are unique for each object.
Instance attribute has higher precedence than class attribute if they have the same name.'''

# class Student:
#     college_name = "ABC Collge" #class attribute
#     PI=3.1

#     def __init__(self, name, cgpa):
#         self.name = name #instance attribute
#         self.cgpa = cgpa
#         self.PI=3.14

# stu1=Student("rahul", 8.5)

# print(stu1.name) #accessing instance attribute
# print(Student.college_name) #accessing class attribute
# print(stu1.college_name) #accessing class attribute using object

'''Different types of Methods:
1. Instance method: An instance method is a method that operates on the instance of the class. It takes self as the first parameter, which refers to the current instance of the class. Instance methods can access and modify instance attributes as well as class attributes.'''

# class Laptop:
#     storage_type="ssd"

#     def __init__(self, RAM, storage):
#         self.RAM=RAM
#         self.storage=storage

#     def get_info(self):
#         print(f"laptop has {self.RAM} Ram and {self.storage} {self.storage_type}")

# l1=Laptop("16g", "512gb")
# l2=Laptop("8g", "1tb")

# l1.get_info()



'''2. Class method: A class method is a method that operates on the class itself rather than on instances of the class. It takes cls as the first parameter, which refers to the class itself. Class methods are defined using the @classmethod decorator. They can access and modify class attributes but cannot access instance attributes directly.'''

# class Laptop:
#     storage_type="ssd"

#     def __init__(self, RAM, storage):
#         self.RAM=RAM
#         self.storage=storage

#     @classmethod
#     def get_storage_type(cls):
#         print(f"storage type = {cls.storage_type}")

#     def get_info(self):
#         print(f"laptop has {self.RAM} Ram and {self.storage} {self.storage_type}")

# l1=Laptop("16g", "512gb")
# l2=Laptop("8g", "1tb")

# l1.get_storage_type()

'''3. Static method: A static method is a method that does not operate on either the instance or the class. It does not take self or cls as the first parameter. Static methods are defined using the @staticmethod decorator. They are used for utility functions that do not require access to instance or class attributes.
No compulsory parameter is required in static method.'''


# class Laptop:
#     storage_type="ssd"

#     def __init__(self, RAM, storage):
#         self.RAM=RAM
#         self.storage=storage

#     @classmethod
#     def get_storage_type(cls):
#         print(f"storage type = {cls.storage_type}")

#     def get_info(self):
#         print(f"laptop has {self.RAM} Ram and {self.storage} {self.storage_type}")

#     @staticmethod
#     def calc_discount(price,discount):
#         final_price = price - (price * discount / 100)
#         print(f"final discounted price is {final_price}")

# l1=Laptop("16g", "512gb")
# l2=Laptop("8g", "1tb")

# l1.calc_discount(49_000, 10)


'''Design and create an online store for Products (name, price).
Track total products being created.
Create a static method to calculate discount on each product based on a % parameter'''

# class Product:
#     count=0

#     def __init__(self, name, price):
#         self.name=name
#         self.price=price
#         Product.count+=1

#     def get_info(self):
#         print(f"price of {self.name} is Rs.. {self.price}")

#     @classmethod
#     def get_count(cls):
#         print(f"total products created: {cls.count}")

#     @staticmethod
#     def calc_discount(price, discount):
#         final_price = price - (price * discount / 100)
#         print(f"final discounted price is Rs.. {final_price}")

# p1= Product("mobile",10_000)
# p2= Product("laptop",65_000)
# p3= Product("Microwave",13_000)
# p4= Product("Refrigerator",20_000)

# Product.get_count()

# p1.calc_discount(p1.price, 17)


'''OOP Pillars:
1. Encapsulation: 
It is a process of wrapping data and methods into a single unit
Encapsulation is the bundling of data (attributes) and methods (functions) that operate on that data within a single unit, typically a class. It restricts direct access to some of the object's components, which helps prevent unintended interference and misuse of the data. Encapsulation is achieved using access modifiers like private, protected, and public.
'''

'''Data Hiding: Data hiding is a principle of encapsulation that restricts access to certain attributes and methods of an object from outside the class. It is done to protect the integrity of the data and prevent unauthorized access or modification. In Python, data hiding is typically achieved by prefixing attribute names with a double underscore (__), making them private to the class.

There are 3 types of access modifiers:
1. Public: Public members are accessible from anywhere, both inside and outside the class. In Python, all members are public by default.
2. Protected: Protected members are accessible within the class and its subclasses. In Python, protected members are indicated by a single underscore (_) prefix.
3. Private: Private members are accessible only within the class itself. In Python, private members are indicated by a double underscore (__) prefix.'''

# class BankAccount:
#     def __init__(self, name, balance):
#         self.name=name
#         self.__balance=balance #private-data mangling, attribute double underscore makes it private

#     def get_balance(self):  #getter method
#         return self.__balance
    
#     def set_balance(self, newBalance): #setter method
#         self.__balance

# acc1 =BankAccount("Rahul", 100_000)

# acc1.set_balance(150_000)
# print(acc1.name, acc1.get_balance())



'''To access private attribute we can use getter and setter methods.'''



'''2. Abstraction: Abstraction is the concept of hiding the complex implementation details and showing only the essential features of an object. It allows programmers to focus on interactions at a higher level without needing to understand all the underlying complexities. Abstraction is achieved using abstract classes and interfaces.
The difference between abstraction and data hiding is that abstraction focuses on exposing only the necessary details while hiding the complexity, whereas data hiding focuses on restricting access to certain attributes and methods to protect the integrity of the data.'''

# from abc import ABC, abstractmethod

# class Animal(ABC):
#     @abstractmethod
#     def make_sound(self):
#         pass

# class Lion(Animal):
#     def make_sound(self):
#         print("Roar!")


# class Dog(Animal):
#     def make_sound(self):
#         print("Bark!")

# class Cat(Animal):
#     def make_sound(self):
#         print("Meow!")

# lion=Lion()
# lion.make_sound()

# cat=Cat()
# cat.make_sound()


'''3. Inheritance: Inheritance is a mechanism that allows a new class (derived class or child class) to inherit properties and behaviors (attributes and methods) from an existing class (base class or parent class). This promotes code reusability and establishes a hierarchical relationship between classes.'''

# class Employee:
#     start_time="10am"
#     end_time="6pm"

#     def change_time(self, new_end_time):
#         self.end_time=new_end_time

# class Teacher(Employee):
#     def __init__(self, subject):
#         self.subject=subject

# class AdminStaff(Employee):
#     def __init__(self, role):
#         self.role=role

# staff1 = AdminStaff("manager")
# print(staff1.role, staff1.start_time, staff1.end_time)

'''Types of Inheritance:
1. Single Inheritance: A derived class inherits from a single base class, only one parent class is involved.'''

'''
2. Multiple Inheritance: A derived class inherits from multiple base classes.'''

# class Teacher:
#     def __init__(self,salary):
#         self.salary=salary

# class Student:
#     def __init__(self, gpa):
#         self.gpa=gpa

# class TA(Teacher, Student):
#     def __init__(self, salary, gpa, name):
#         super().__init__(salary)
#         Student.__init__(self, gpa)
#         self.name=name
# ta1 =TA(40000, 9.4, "Subodh")
# print(ta1.name, ta1.gpa, ta1.salary)



'''3. Multilevel Inheritance: A derived class inherits from a base class, which in turn inherits from another base class.'''

# class Employee:
#     start_time="10am"
#     end_time="6pm"

# class AdminStaff(Employee):
#     def __init__(self, role):
#         self.role=role

# class Accountant(AdminStaff):
#     def __init__(self, salary, role):
#         super().__init__(role)
#         self.salary=salary

# acc1=Accountant(50000, "CA")
# print(acc1.role, acc1.salary, acc1.start_time, acc1.end_time)

'''
4. Hierarchical Inheritance: Multiple derived classes inherit from a single base class.
5. Hybrid Inheritance: A combination of two or more types of inheritance.'''


'''4. Polymorphism: Polymorphism is the ability of different classes to be treated as instances of the same class through a common interface. It allows methods to do different things based on the object it is acting upon, even if they share the same name. Polymorphism is typically achieved through method overriding and method overloading.
we create different functions with the same name but with different implementations.

Ex: Operator Overloading, Method Overriding

There are two types of polymorphism:
1.Function overriding: Function overriding is a feature in object-oriented programming where a derived class provides a specific implementation of a method that is already defined in its base class. When the method is called on an instance of the derived class, the overridden method in the derived class is executed instead of the one in the base class.Redefining parent class function in child class is called function overriding.'''

# class Employee:
#     def get_designation(self):
#         print("designation= Employee")

# class Teacher(Employee):
#     def get_designation(self):
#         print("designation= Teacher")

'''
2.Duck Typing: Duck typing is a concept in programming, particularly in dynamically typed languages like Python, where the type or class of an object is determined by the methods and properties it has, rather than its actual class or inheritance hierarchy. The idea is summarized by the phrase "If it looks like a duck and quacks like a duck, it's a duck." This means that if an object behaves like a certain type (i.e., it has the necessary methods and properties), it can be treated as that type, regardless of its actual class.If something walks like a duck and quacks like a duck, then it must be treated as  a duck.
'''
# class Teacher():
#     def get_designation(slef):
#         print("designation= Teacher")

# class Accountant():
#     def get_designation(self):
#         print("designation= Accountant")


# t1=Teacher()
# t1.get_designation()

# acc1=Accountant()
# acc1.get_designation()

