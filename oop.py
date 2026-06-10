# class Person:
#     def __init__(self,name,age,height):
#         self.name=name
#         self.age=age
#         self.height=height

#     def display(self):
#         print(f"The person name {self.name} with {self.age} years old having {self.height} cm height")

# p1=Person("Susmi",15,172)
# p2=Person("Rishana",10,162)

# p1.name="Aami" # modifying objects

# print(p1.name)
# # print(p2.name)

# p1.display()
# # p2.display()

# __str__ method #

# class Book:

#     def __init__(self,title,author):
#         self.title=title
#         self.author=author
    
#     # def abc(self):
#     #     print(f"{self.title} by {self.author}")

#     def __str__(self):
#         return f"'{self.title}' by {self.author}"

# book=Book("Isneham","Anjal Taj")

# # print(book.title)
# # print(book.author)
# # book.abc()
# print(book)

# CLASS VARIABLE & INSTANCE VARIABLE #

# class Employee:
#     company="Softroniics"

#     def __init__(self,name,position):
#         self.name=name
#         self.position=position
    

# emp1=Employee("susmi","python developer")
# emp2=Employee("rishana","python developer")

# print(emp1.company)
# print(emp2.company)

# INNER CLASS #

# class Employee:
#     class Company:
#         def __init__(self,cname,location):
#             self.cname=cname
#             self.location=location
#     def __init__(self,name,salary,cname,location):
#         self.ename=name
#         self.salary=salary
#         self.Company=Employee.Company(cname,location) 
    
#     def display(self):
#         print(f"name: {self.ename} salary: {self.salary} company: {self.Company.cname} location: {self.Company.location}")


# emp=Employee("susmi",50000,"TCS","Banglore")
# emp.display()
# print(emp.Company.cname)

# composition #
# tightly coupled #

# class Company:
#     def __init__(self,cname,location):
#         self.cname=cname
#         self.location=location
        
# class Employee:
#     def __init__(self,name,salary,cname,location):
#         self.ename=name
#         self.salary=salary
#         self.Company=Company(cname,location) 
    
  
# emp=Employee("susmi",50000,"TCS","Banglore")
# # print(emp.Company.cname)
# print(emp.ename)

#loosely coupled #

# class Company:
#     def __init__(self,cname,location):
#         self.cname=cname
#         self.location=location
        
# class Employee:
#     def __init__(self,name,salary,cmp):
#         self.ename=name
#         self.salary=salary
#         self.cmp=cmp


#     def display(self):
#         print(f"name: {self.ename} salary: {self.salary} company: {self.cmp.cname} location: {self.cmp.location}")   
    
# c=Company("TCS","Kochi") 
# emp=Employee("susmi",50000,c)
# emp.display()

# TASK 1 #

# class Student:
#     def __init__(self,name,marks):
#         self.name=name
#         self.marks=marks

    
#     def display(self):

        

#         if self.marks>=90:Grade="A"
            
#         elif self.marks>=75 and self.marks<90:Grade="B"
            
#         elif self.marks>=50 and self.marks<75:Grade="C"
            
#         else:Grade="Fail"
            

#         print(f"name:{self.name},marks:{self.marks}")

# std=Student("susmi",70)
# std.display()

# Task 2 #

# class Student:
#     def __init__(self,name,marks):
#         self.name=name
#         self.marks=marks

#     def avarage(self):
#         total = sum(self.marks.values())
#         avg = total / len(self.marks.values())
#         return avg

    
#     def display(self):

#         avg = self.avarage()

#         if avg>=90:Grade="A"
            
#         elif avg>=75 and avg<90:Grade="B"
            
#         elif avg>=50 and avg<75:Grade="C"
            
#         else:Grade="Fail"
            

#         print(f"name:{self.name} average:{avg} | grade:{Grade}")

# std=Student("susmi",{"maths":80,"physics":70,"chemistry":50})
# std.display()

# Encapsulation #

# class Employee:
#     def __init__(self,name,salary):
#         self.name=name
#         self.__salary=salary  # private attribute cannot access outside

#     def display(self):
#         print(f"name:{self.name} salary:{self.__salary}")

#     def update_salary(self,new_salary):
#         self.__salary=new_salary

# emp=Employee("Aami",50000)
# # emp.display()
# # print(emp.name)
# emp.update_salary(60000)
# emp.display()

# TASK 3 #

# class BankAccount:
#     def __init__(self,owner,balance):
#         self.owner=owner
#         self.__balance=balance
        
    
#     def deposit(self,amount):
#         if amount > 0:
#             self.__balance += amount
#             print(f"Deposited Rs {amount}")

            

#     def withdraw(self,amount):
#         if amount > 0 and amount <= self.__balance:
#             self.__balance -= amount
#             print(f"Withdrew Rs {amount}")
#         else:
#             print("Insufficient Balance")

#     def get_balance(self):
#         return self.__balance
           

#     def display(self):
#         print(f"owner:{self.owner}, Final Balance: {self.get_balance()}")

# bk=BankAccount("Alice",1000)
# bk.deposit(500)
# bk.withdraw(200)
# bk.display()

#*** INHERITANCE ***#

# single inheritance #

# class Animal:
#     def __init__(self,name):
#         self.name=name

#     def speak(self):
#         print(f"{self.name} makes sound")

# class Dog(Animal):
# pass
#         def __init__(self,name):
#             self.name=name

#         # def speak(self):
#         #     print(f"{self.name} says bow")


    
# dog=Dog("Buddy")
# dog.speak()        
            

# multiple inheritance #

# class engine:
#     def works(self):
#         print(f"engine starts working")

# class wheel:
#     def rotate(self):
#         print(f"wheels rotate")


# class car(engine,wheel):
#     def drive(self):
            # print(f"car is driving")

# ca=car()
# ca.works()
# ca.rotate()
# ca.drive()
    

# multilevel inheritance #

# class grandparent:
#     def sing(self):
#         print(f"grandparent sing songs")

# class parent(grandparent):
#     def dance(self):
#         print(f"parent dance with songs ")

# class child(parent):
#     def play(self):
#         print(f"child is playing")


# stud=child()
# stud.sing()
# stud.dance()
# stud.play()


# Hierarchical Inheritance #

# class Animal:
#     def speak(self):
#         print(f"Animal speaks")

# class Dog(Animal):
#     pass
#     # def speak(self):
#     #     print(f"Dog Barks")

# class Cat(Animal):
#     def speak(self):
#         print(f"Cat sounds Meow")
    
# cat=Cat()
# dog=Dog()

# cat.speak()
# dog.speak()

# Hybrid Inheritance : Combining Multilevel and Hierarchical Inheritance #

# class A:
#     def a(self):
#         print(f"method from class A")

# class B(A):
#     def b(self):
#         print(f"method from class B")

# class C(A):
#     def c(self):
#         print(f"method from class C")

# class D(B,C):
#     def d(self):
#         print(f"method from class D")

# x=D()
# x.a()
# x.b()
# x.c()
# x.d()

# task 1: multilevel inheritance #

# class Employee:
#     def get_employee_id(self):
#         self.id=int(input("Employee ID: "))

#     def display_id(self):
#         print(f"Employee ID is {self.id}")

# class Manager(Employee):
#     def get_department(self):
#         self.dep=input("Department: ")

#     def display_dep(self):
#         print(f"Department is {self.dep}")

# class SeniorManager(Manager):
#     def get_team_size(self):
#         self.teamsize=int(input("teamsize: "))

#     def display_teamsize(self):
#         print(f"Team size is {self.teamsize}")

# x=SeniorManager()

# x.get_employee_id()
# x.get_department()
# x.get_team_size()

# x.display_id()
# x.display_dep()
# x.display_teamsize()

# task 2: multiple inheritance #

# class Marks:
#     def get_marks(self):
#         self.m1 = int(input("Enter marks of Subject 1: "))
#         self.m2 = int(input("Enter marks of Subject 2: "))
#         self.m3 = int(input("Enter marks of Subject 3: "))


# class Sports:
#     def get_sports_score(self):
#         self.sports_score = int(input("Enter Sports Score: "))


# class Result(Marks, Sports):
#     def calculate(self):
#         self.total_marks = self.m1 + self.m2 + self.m3
#         self.average_marks = self.total_marks / 3
#         self.final_score = self.total_marks + self.sports_score

#     def display(self):
#         print("\nTotal Marks =", self.total_marks)
#         print("Average Marks =", self.average_marks)
#         print("Final Score =", self.final_score)

# student = Result()

# student.get_marks()
# student.get_sports_score()

# student.calculate()
# student.display()

# task #

# class Book:
#     def __init__(self, title, author, copies):
#         self.title = title
#         self.author = author
#         self.copies = copies

#     def display_info(self):
#         print(f"Book Title: {self.title}")
#         print(f"Book Author: {self.author}")
#         print(f"Copies: {self.copies}")


# multiple_books = []

# for i in range(3):
#     title = input("Enter the Book Title: ")
#     author = input("Enter the Author: ")
#     copies = int(input("Enter the no. of Copies: "))

#     book = Book(title, author, copies)
#     multiple_books.append(book)

# search = input("Enter the Book Title to search: ")

# found = False

# for book in multiple_books:
#     if book.title.lower() == search.lower():
#         book.display_info()
#         print("Book is Available")
#         found = True
#         break

# if not found:
#     print("Book not Available")


# Polymorphism #

# class Animal:
#     def speak(self):
#         return "makes sound"

# class cat(Animal):
#     def speak(self):
#         return "Meow"

# class dog(Animal):
#     def speak(self):
#         return "barks"

# animal=[cat(),dog()]
# for a in animal:
#     print(a.speak())

# Method Overriding #

# class Animal:
#     def speak(self):
#         print(f"Animal makes sound")

# class Dog(Animal):
#     def speak(self):
#         print(f"Dogs Barks")

# class Cat(Animal):
#     def speak(self):
#         print(f"Cats sounds Meow")

# animal=[Cat(),Dog()]
# for i in animal:
#     animal.speak()

# Duck typing #

# class Animal:
#     def speak(self):
#         return "makes sound"

# class cat():
#     def speak(self):
#         return "Meow"

# class dog():
#     def speak(self):
#         return "barks"

# animal=[cat(),dog()]
# for a in animal:
#     print(a.speak())

# Abstraction #

# from abc import ABC, abstractmethod

# class Shape(ABC):
#     @abstractmethod
#     def area(self):
#         pass

# class rectangle(Shape):
#     def __init__(self,width,height):
#         self.width=width
#         self.height=height 

#     def area(self):
#         return self.width * self.height



# rect=rectangle(5,6)
# print(rect.area())

# shp=Shape()

# constructor and destructor #

# class Student:
#     def __init__(self,name,age):
#         self.name=name
#         self.age=age
#         print(f"{self.name} is created")

#     def __del__(self):
#         print(f"{self.name} is destroyed")

# stud=Student("susmi",10)
# # print(stud.name)
# del stud

# decorators #
# def sprinkles(fun):
#     def wrapper(*args):
#         print(f"sprinkles on")
#         fun(*args)
#         print(f"sprinkles off")
#     return wrapper



# @sprinkles
# def icecream(name):
#     print(f"{name} icecream")

# icecream("choclate")

# Class Method #

# class company #:
#     company_name="Softroniics"
    
#     @classmethod
#     def change_cmpname(cls,new_name):
#         cls.company_name=new_name

# # change class variable through a class method #
# company.change_cmpname("Tata Consultancy Services")
# print(company.company_name)

# Static Method #:

class Math:
    
    @staticmethod
    def add(a,b):
        return a+b

m=Math() 
print(m.add(10,20))

