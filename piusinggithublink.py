 # creating a class 
class Student:
    def __init__(self,fullname):
        self.name = fullname
        

# creatng an object 

s1 = Student("karan")
#print(s1.name)
# Methods 
# methods are function that belong to objects.
# methods are function that belong to objects.
# methods are function thet belong to objects.
# methods are function that belong to objects.
# methods are function that belong to objects.


# creating class 

class Student1:
    def __init__(self,fullname):
        self.name = fullname


    def hello(self):
        print("hello ",self.name)


s2 = Student1("Kumar")

# s2.hello()


# creae student class that takes name & marks of 3 subjects as argumetns in constructor.
# then create a method  to print the average.
# create student class that takes name & marks of 3 subjects as arguments in constructor.
# then create a method to print the average.[

class Student3:
    def __init__(self,fullname,math,english,history):
        self.name = fullname 
        self.math = math
        self.english = english
        self.history = history

    def average(self):
        averge =  (self.math+self.english+self.history)/3
        print("this is average of 3 sub... ",averge)

# s3 = Student3("Khan ",85,98,80)
# s3.average()
        
# create account class with 2 attributes - balance & account no.
# create methods for debit,credit &and printing the balance

class Account:
    def __init__(self,account,balance):
        self.account = account
        self.balance = balance

    def debit(self,debitamount):
        if self.balance > debitamount:
            self.balance -= debitamount
            print("money is debited :",debitamount)
        else:
            print("ineficient balance")

    def cridet(self,creditamount):
        if creditamount != 0:
            self.balance += creditamount
            print("the money added :",creditamount)

        else:
            print("0 is not valid amount :",creditamount)
        

    def printingBalance(self):
        print("YOUR BALANCE IS : ",self.balance)


# custember1 = Account(733210,10000)
# custember1.debit(100)
# custember1.printingBalance()
# custember1.cridet(200)
# custember1.printingBalance()
 
# class Car:
#     def __init__(self,make,model,year):
#         self.make = make
#         self.model = model
#         self.year = year 

#     def drive(self):
#         print("car is criving")

# car1 = Car(Toyota,Camry,2020)/
import math

# class Circle:
#     def  __init__(self,radius):
#         self.radius = radius

#     def calculate_area(self):
#         return math.pi * self.radius **2
    

#     def calculate_perimter(self):
#         return 2 * math.pi * self.radius
    

# circle1 = Circle(21)

# print("this area of circle 1 : ",circle1.calculate_area())
# print("this is a perimetter of circle1 : ",circle1.calculate_perimter())


print(2**8)