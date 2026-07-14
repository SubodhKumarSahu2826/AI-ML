#our first programm

# name="Subodh Kumar Sahu"   #this is my name
# age=21 #this is my age
# PI=3.14 #this is the value of pi


# print(age)
# print(name,age,PI)
# print("My name is",name,"and my age is",age,"years.")
# print("My age is", age+4, "after 4 years.")

# name,age.pi are called as indentifieres in python.these are used to identify the varibles which are declared in the program.
# Python is a case sensitive language.
# we need to maintian indentation in python.  indentation is nothing but the spaces before the statement.
# we cannot start an identifier with a number.
# we cannot use special characters like @,#,$ etc in the identifier.
#name of the varible must be meaningful.

''' This is a multi line comment
in python and we can wirite
anything in this comment'''

# print(type(age))
# print(type(PI))
# print(type(name))

# num=6
# isPrime=True

# print(type(isPrime))

# tot_price=100 #snake_case (most preferred)
# totalPrice=100  #camelCase
# total_price=100  #pascalCase

# WAP to add two numbers and print the result

# a=5
# b=10
# sum=a+b
# print(sum)

#arithemetic operations in python
# a=9
# b=5
# print(a+b)  #addition
# print(a-b)  #subtraction
# print(a*b)  #multiplication
# print(a/b)  #division
# print(a%b)  #modulus (gives remainder)
# print(a**b) #exponentiation

#relational operators in python

# print(a>b)
# print(a<b)
# print(a>=b)
# print(a<=b)
# print(a==b) #compares the values of a and b and returns true if both are equal and false if not equal
# print(a!=b)

#assignment operators in python

# a=5
# a+=5 #a=a+5 
# print(a)
# a-=5 #a=a-5
# print(a)
# a*=5 #a=a*5
# print(a)
# a/=5 #a=a/5
# print(a)
# a**=5 #a=a**5
# print(a)

#relational operators in python

# print(a>b and a!=b)
# print(a<b or a!=b)
# print(not(a>b and a!=b)) 

# x=3
# x+=6
# print(x)

#operators precedence in python
# a=5
# b=10
# c=15      
# result=a+b*c
# print(result)  #multiplication has higher precedence than addition
# result=(a+b)*c
# print(result)  #parentheses has highest precedence
# result=a**b+c/5-b*a
# print(result)  #exponentiation has higher precedence than division,multiplication,addition
# result=a+b%c**2
# print(result)  #exponentiation has higher precedence than modulus and addition    
# result=a+b%c**2-a*b/4
# print(result)  #exponentiation has higher precedence than modulus,multiplication,division,addition
# result=a+b%c**2-a*b/4+1
# print(result)  #exponentiation has higher precedence than modulus,multiplication,division,addition
# result=a+b%c**2-a*b/4+1-2**3+6/3

#if our expression contains operators with same precedence then the associativity rule is applied.
# left to right associativity for +,-,*,/,%

#Type Conversion in python
#type conversion is of two types
#1. implicit type conversion
#2. explicit type conversion


#implicit type conversion
#it is a implicit type conversion where python automatically converts one data type to another data type without any user involvement with the help of its interpreter.

# a=10
# b=5
# print(type(a/b)) #here the integer value is converted to float value automatically by python interpreter.

#type casting in python
#type casting is a explicit type conversion where the user converts one data type to another data type with the help of its interpreter.

# a=10
# b=4
# print(type(int(a/b))) #here the integer value is converted the required data type by the user with the help of functions

# ans1=int(5+10.5) #casting
# ans2=5+10.5 #implicit
# print(ans1, type(ans1))
# print(ans2, type(ans2))

#user input in python
# a=input("enter the calue of a:")
# b=input("enter the calue of b:")
# print(a)
# print(b)


# username=input("enter your username:")
# print("Hello!", username)

#sum of 2 numbers
# a=float(input("enter the value of a:"))
# b=float(input("enter the value of b:"))
# sum=a+b
# print("sum of two numbers a+b is:", sum)

#WAP a program to calculate average of 2 numbers

# a=float(input("enter the first number:"))
# b=float(input("enter the second number:"))
# avg=(a+b)/2
# print("average po two numbers is :", avg)


#Conditional statements in python

# age=int(input("enter your age:"))

# if age>=18:
#     print("you are eligible to vote")
#     print("you can drive as well")
# else:
#     print("you cannot vote")
#     print("you cannot drive")

# color=input("enter the color:")

# if color=="red":
#     print("stop")
# elif color=="yellow":
#     print("get ready")
# elif color=="green":
#     print("go")
# else:
#     print("please enter a valid color")

# age=int(input("enter your age:"))

# if age<13:
#     print("you are a child")
# elif age>=13 and age<18:
#     print("you are a teenager")
# else:
#     print("you are an adult")

# username="admin"
# password="pass"

# input_username=input("enter your username:")
# input_password=input("enter your password:")

# if username==input_username and password==input_password :
#     print(" correct login credentials,logged in suucessfully")
# else:
#     print("invalid username and password please try again")

#WAP to check if a number is a multiple fo 5 or not

# n=int(input("enter a number:"))

# if n % 5==0:
#     print("the number is a multiple of 5")
# else:
#     print("the number is not a multiple of 5")


#WAP to check if a number is even or odd
# n=int(input("enter a number:"))
# if n%2==0:
#     print("the number is even")
# else:
#     print("the number is odd")


#Nesting of if-else statements in python

# username=input("enter your username:")
# password=input("enter your passsword:")

# if (username=="admin" and password=="pass"):
#     print("logged in successfully")

# else:
#     if (username !="admin"):
#        print("invalid username")
#     else:
#         print("invalid password")

#Match case in conditional statement in python

#it is used as and alternative to if-elif-else ladder when we have multiple conditions to check for a single variable.

# color=input("enter yhe color:")

# match color:
#     case "Green":
#         print("Go")
#     case "yellow":
#         print("get ready to go")
#     case "Red":
#         print("stop")

#     case _:
#         print("worng color") #default case
#         print("please enter a valid color")


#Loops in python

#loops are used to repeat a set of instructions multiple times

#while loop in python
#in While we perfrom the task until the condition is true.


# count=1. #iterator
# while (count<=13):
#     print("hello", count)
#     count=count+1

#Wap to print numbers from 1-5
# i=1
# while(i<=5):
#     print(i)
#     i=i+1

#WAP to print first 5 numbers in reverse order
# i=17
# while(i>=1):
#     print(i)
#     i-=1

#WAP to print the multiplication table of a number entered by the user

# n=int(input("enter a number whose multiplication table you want to print"))
# i=1
# while(i<=10):
#       print(n*i)
#       i+=1

#Break and continue statement in python

#break statement is used to terminate the loop when encountered

# i=5
# while(i<=10):
#     if (i%6==0):
#         break
#     print(i)
#     i+=1

#continue statement is used to skip the current iteration of the loop and move to the next iteration

# i=1
# while(i<=10):
#     if(1%3==0):
#         i+=1
#         continue
#     print(i)
#     i+=1
     
#WAP a program to print odd numbers from 1 to 10

# i=1
# while(i<=10):
#     print(i)
#     i+=2

# i=1
# while(i<=10):
#     i+=1
#     if(i%2==0):
#         continue
#     print(i)



# For loop in python

#for loop is used to iterate over a sequence (list, tuple, string) or other iterable objects

# string="hello"

#in=> membership operator (it is also used to check presence of an element in a sequence)
#var=> variable to hold each character of the string one by one

# for var in string:
#     print(var)

#if we want to check if a particular character is present in the string or not then we can use 'in' membership operator

# if 'o' in string:
#     print("o exist in the string")
# else:
#     print("The element does not exist in the string")

# for i in range(5):
#     print(i+1)

#WAP to print numbers of i in artiicial intelligence
# word="Artificial intelligence"

# count=0

# for ch in word:
#     if(ch=='i'):
#         count+=1
#     print("count of i=", count)

#print vowel count of a given string

# word="artificial"
# count=0

# for ch in word:
#     if(ch=='a' or ch=='e' or ch=='i' or ch=='o' or ch=='u'):
#         count+=1
# print("vowel count=", count)

#Range function in python

#range function is used to generate a sequence of numbers

#range(start, stop, step)

# for i in range(6):
#     print(i)

# for i in range (1,18,2):
#     print("the series of odd numbers a are:", i)

#WAP to print first n natural numbers using for loop


# n=int(input("enter the number whose sum you want to find:"))
# sum=0

# for i in range(1,n+1):
#     sum+=i
# print("sum of first n natural numbers is:", sum)

#Functions in python

#function is a block of code that performs a specific task

#fucntion has 2 parts => function definition and function call

#function definition
#in function definition we define the function and write the core logic using def keyword followed by function name and parentheses()

# def hello():
#     print("Hello!, world")
#     print("from python function")

#function call
#it is used to execute the function and basically invokes the function
#function call is done by writing the function name followed by parentheses()

# hello()

#function is a resuable block of code

# a=int(input("Entere the cvalue of a:"))
# b=int(input("Enter the value of b:"))

# def sum(a,b):  #a, b are called as parameters and the actual values are called as arguments
#     s=a+b
#     return s

# result=sum(a,b)
# print("sum of two numbers is:", result)

#create a function which takes 3 numbers as input and returns the average of those numbers

# def average(a,b,c):
#     avg=(a+b+c)/3
#     return avg

# a=int(input("Enter the value of a:"))
# b=int(input("Enter the value of b:")) 
# c=int(input("Enter the value of c:"))

# result= average(a,b,c)
# print("Average of 3 numbers is:", result)

#Types of functions in python

#1. Built-in functions
#2. User-defined functions

#Built-in functions are the functions that are pre-defined in python

#eg: print(), input(), len(), sum(), max(), min(), range(), type(), int(), float(), str(), bool(), list(), tuple(), set(), dict(), etc.

#User-defined functions are the functions that are defined by the user
#eg: sum(), average(), etc.

#lambda functions in python
#lambda functions are anonymous functions that are defined using the lambda keyword
#they can take any number of arguments but can only have one expression
#syntax: lambda arguments: expression
# square=lambda x: x**2

# mul=lambda a,b: a*b
# print(mul(7,9))

#lambda functions are mostly used in higher order functions like map(), filter(), reduce() etc.

#WAF to find the factorial of a number 
#1. using iterative approach
# def factorial(n):
#     if n==0:
#         return 1
#     else:
#         return n*factorial(n-1)

# n=int(input("Enter a number:"))
# print("Factorial of",n,"is:",factorial(n))

# #2. using recursive approach
# def cal_factorial(n):
#     fact=1
#     for i in range(1,n+1):
#         fact*=i
#     return fact

# n=int(input("Enter a number:"))
# print("Factorial of ",n, "is:", cal_factorial(n))

#String in python
#String is a sequence of characters enclosed in single quotes(' ') or double quotes(" ")
# word1="python programming"
# word2="is easy to learn"

#concatenation of strings
# print(word1 + " " + word2)

# word1="Python"
# print(word1[3])

#string are immutable in python
# word1[0]='p' #this will give an error as strings are immutable

#Slicing of strings in python
# word="Python"
# # print(word[1:4]) #start index is inclusive and end index is exclusive
# print(word[2:4]) #prints characters from index 2 to 3
# print(word[:3])  #prints characters from index 0 to 2
# print(word[3:])  #prints characters from index 3 to end
# print(word[-4:-1]) #prints characters from index -4 to -2
# print(word[::-1]) #prints the string in reverse order
# print(word[-1::-1]) #prints the string in reverse order

#Formatting of strings in python
#it is used when we want to create dynamic strings in which we can use some variables and their values

#format() method is used for string formatting in python in whcih we use {} as placeholders for the variables and their values are passed in the format() method

# a=5
# b=10
# sum=a+b

#normal formatting  
# print("language is {}".format("Python"))
# print("sum is {}". format(sum))
# print("sum of {} and {} is {}".format(a,b,sum))

#indexed formatting
# print("sum of {1} and {0} is {2}".format(a,b,sum))

#f-string formatting
# print(f"sum of {a} and {b} is {a+b}")
 

 #Lists in python
 #List is a mutable sequence of elements enclosed in square brackets [ ]
#List can contain elements of different data types

# marks=[99,89,86,79,77,92,84,98]
# print(len(marks)) #length of the list
# print(marks[2])  #accessing elements of the list
# marks[2]=95      #modifying elements of the list
# print(marks)
# print(type(marks))

# print(marks[:4]) #slicing of list
# print(marks[3:])

# print(marks[-5:-2]) #slicing using negative indexing 

#Methods of list in python
#when we write function of classes it is called as method

#l.append(val) #adds an element at the end of the list
# nums=[1,2,3,4,5]
# nums.append(6)
# print(nums)

# #l.insert(index, val) #adds an element at the specified index
# nums.insert(1,7)
# print(nums)

# #l.sort() #sorts the list in ascending order
# nums.sort()
# print(nums)

# #l.reverse() #reverses the list
# nums.reverse()
# print(nums)

#Loops through list

# nums=[2,4,3,6,7,9]

# for val in nums:
#     print(val)

#WAP to find an element in the list and return its index
#liner search algorithm: we traverse through each element of the list and compare it with the given element

# x=6
# index=0
# for val in nums:
#     if val==x:
#         print(f"{x} found at index={index}")
#         break
#     index+=1

#Tuples in python
#Tuple is an immutable sequence of elements enclosed in parentheses ( )
#Tuple can contain elements of different data types

# tup=(1,2,3, "abc",4,5)
# print(tup)
# print(type(tup))
# print(len(tup))

# #single vale tuple are created as follows
# single_val_tup=(5,)

# #Slicing of tuple
# print(tup[1:4])
# print(tup[:3])
# print(tup[2:])


# tup=(4,2,6,7,5)
# sum=0
# for val in tup:
#     sum+=val
# print(f"sum of all elements in the tuple is: {sum}")

#methods of tuple in python
#t.index(val) returns the index of the first occurrence of the given value

# tup=(3,6,7,9,3,2,6,7)
# print(tup.index(6))

#t.count(val) returns the count of occurrences of the given value in the tuple
# print(tup.count(3))

#Dictionary in python
#Dictionary is a mutable collection of key-value pairs enclosed in curly braces { }
#Dictionary can contain elements of different data types    

#keys are always unique and values can be duplicate
#Values can be accessed using keys
#Dictionary are unordered collection of elements

info={"name": "Subodh",
      "CGPA":9.1, 
      "Subjects":["AI", "ML",],
      3.14:"PI Value"}

# print(type(info))
# print(info)

# print(info["name"])  #accessing values using keys
# info["CGPA"]=9.5    #modifying values using keys
# print(info)

#Methods of dictionary in python
# d.keys() #returns a list of all keys in the dictionary

# print(info.keys())

# # d.values() #returns a list of all values in the dictionary
# print(info.values())

# #d.items() #returns a list of all key-value pairs in the dictionary
# print(info.items())

# #d.get(key) #returns the value for the given key
# print(info.get("name"))

# #d.update({key:val}) #updates the value for the given key
# info.update({"CGPA":9.8})
# print(info)

#Set in python
#Set is an unordered collection of unique elements enclosed in curly braces { }
#Set can contain elements of different data types
#set elements are immutable but we can add or remove elements from the set

# set={1,2,3,4,5,5,4,3}
# print(set)
# print(type(set))
# print(len(set))

# #Methods of set in python
# # s.add(val) #adds an element to the set
# set.add(6)
# print(set)

# # s.remove(val) #removes an element from the set
# set.remove(3)
# print(set)

# #s.clear() #removes all elements from the set
# set.clear()
# print(set)

# #s.pop() #removes and returns an arbitrary element from the set
# set={1,2,3,4,5}
# removed_element=set.pop()
# print("removed element:", removed_element)
# print(set)

# s.union(set2) #returns a new set that is the union of set and set2
# set1={1,2,3}
# set2={3,4,5}
# set3=set1.union(set2)
# print("union of set1 and set2:", set3)  


# s.intersection(set2) #returns a new set that is the intersection of set and set2
# set4=set1.intersection(set2)
# print("intersection of set1 and set2:", set4)

#Students Enrolments
''' Given a list of tuples wth info(name,subject):
-> list all unique courses
->list students enrolled inenglish
->create dictionary(student, set of courses)'''

info=[("Subodh", "AI"),
      ("Rahul", "ML"), 
      ("Priya", "AI"), 
      ("Sneha", "English"), 
      ("Subodh", "English"), 
      ("Priya", "ML")]

#list all unique courses

# courses_set=set()
# for tup in info:
#     courses_set.add(tup[1])
# print("unique courses offered are:", courses_set)

#list students enrolled in english
# for name, course in info:
#     if(course=="English"):
#         print(name)

#create dictionary(student, set of courses)

# dict={}
# for name,course in info:
#     if(dict.get(name)==None):
#         dict.update({name:set()})
#         dict[name].add(course)
#     else:
#         dict[name].add(course)
# print(dict)

'''File I/O in python
File I/O is used to read and write data to files
When we are opening a file we need to specify the mode in which we want to open the file and need to close the file after performing the operations on it.
Modes of file I/O in python:
1. r: read mode (default mode) - used to read data from a file
2. w: write mode - used to write data to a file (if the file already'''

# f=open("sample.txt", "r")

# data =f.read()
# print(data)
# print(type(data))

# f.close()

# data=f.readline() #reads a single line from the file
# print(data)
# f.close()


# f=open("sample.txt","w")
# f.write("Text to overwrite \n the compleate data.")
# f.close()

'''File Operation mode in python
1. r: read mode (default mode) - used to read data from a file
2. w: write mode - used to write data to a file (if the file already exists it will overwrite the existing data)
3. a: append mode - used to append data to a file (if the file already exists it will add the new data at the end of the existing data)
4. x: exclusive creation mode - used to create a new file (if the file already exists it will give an error)
5.a: read and write mode - used to read and write data to a file
6.b: binary mode - used to read and write binary data to a file
7.t: text mode (default mode) - used to read and write text data to a file
8.+: read and write mode - used to read and write data to a file
9.r+: read and write mode - used to read and write data to a file
10.w+: write and read mode - used to write and read data to a file
11.a+: append and read mode - used to append and read data to a file
'''

'''With Keyword in python
The with keyword in python is used to simplify the process of working with files.
It automatically takes care of closing the file after the operations are done, even if an exception occurs.
This helps to avoid potential memory leaks and ensures that the file is properly closed after its use.'''

# with open("sample.txt", "r") as f:
#     print(f.read())
    
'''Deleting files in python
To delete a file in python we can use the os module which provides a method called remove()
We need to import the os module before using it.'''

# import os 
# os.remove("sample.txt")

# print("file deleted successfully")

'''Word Search in a file
WAP to search for a word in a file and print the line number and the line containing the word'''

# data=True
# line=1
# word="Python"

# with open("sample.txt","r") as f:
#     while data:
#        data=f.readline()

#        if("Python" in data):
#            print(f"{word} found at line {line}")
#            break
       
#        line+=1


'''Exception Handling in python
Exception handling is used to handle errors and exceptions that may occur during the execution of a program.
It helps to prevent the program from crashing and allows us to handle the errors gracefully.

try: block is used to write the code that may raise an exception or may not   

except: block is used to handle the exception that may occur in the try block

else: block is used to write the code that will be executed if no exception occurs in the try block

finally: block is used to write the code that will be executed regardless of whether an exception occurs or not in the try block
'''

# try:
#       x=int(input("enter x:"))
#       ans=10/x

# except ZeroDivisionError:
#       print(f"Division by zero is not allowed")

# except ValueError:
#       print(f"Invalid input, please enter a valid integer")

# else:
#       print(f"ans={ans}")

# finally:
#       print("End of Python programm")


'''List Comprehension in python
List comprehension is a concise way to create lists in python.
It consists of brackets containing an expression followed by a for clause, then zero or more for or if clauses.
The expressions can be anything, meaning you can put in all kinds of objects in lists
list comprehension is written in a single line of code which makes it more readable and efficient than traditional for loops.
Syntax:
list=[expression for item in iterable if condition]
'''

# squares=[]

# for i in range(6):
#     squares.append(i*i)

# print(squares)

# sq=[i*i for i in range(6)]
# print(sq)

# sq=[i*i for i in range(6) if i%2!=0]
# print(sq)

# nums=[1,-2,4,-5,6,-3]
# nums=[0 if val<0 else val for val in nums]
# print(nums)

# words=["hello", "world", "PYTHON", "programming"]
# print(words[0].upper())

# print(words[2].lower())

'''JSON Module in python
JSON (JavaScript Object Notation) is a lightweight data interchange format that is easy for humans to read and write and easy for machines to parse and generate.
In python, we can use the json module to work with JSON data.
The json module provides methods to convert python objects to JSON format and vice versa.

JASON is a format to store and exchange data
It is similar to dictionary in python as it is stored in key-value pairs

python list are converted to JSON arrays
python dict are converted to JSON objects
python str are converted to JSON strings
None are converted to JSON null

Modules in JSON:
1. json.dumps(): converts python object to JSON string
2. json.dump(): writes python object to a JSON file
3. json.loads(): converts JSON string to python object
4. json.load(): reads JSON file and converts it to python object
'''

# import json

# py_obj={
#     "name": "Subodh Kumar",
#     "isTeacher": True
# }
# json_str='{"name": "Subodh Kumar", "isTeacher": true}'


# json_str=json.dumps(py_obj)
# # py_obj=json.loads(json_str)
# print(type(json_str), json_str)
# # print(type(py_obj), py_obj)


# import json
# with open("data.json","r") as f:
#     pyobj=json.loads(f)
#     print(type(py_obj))
