# syntax error #
# print("hello"

# zero division error #

# a=10
# b=0
# print(a/b)

# TypeError #

# def add(a,b):
#     return a+b 
# print(add(3))

# def add(a,b):
#     return a>b 
# print(int(3,3.5))

# a=10
# b=''
# print(a/b)

# valueError #
 
# int("abc")

# Index error #

# a=[1,2,3,4,5,6]
# print(a[8])

# keyError #

# a={"name":"susmi","age":20,"city":"valanchery"}
# print(a["fname"])

# FileNotFoundError #

# file=open("susmi.txt","r")
# print(file.read())
# file.close()

# Exception Handling with try-except

# try:
#     10/0
# except ZeroDivisionError:
#     print("cant divided by zero")

# else and finally block #

# try:
#     num=int(input("enter a number: "))
#     result=10/num
# except ZeroDivisionError:
#     print("cant divided by zero")
# else:
#     print(f"Result = {result}")
# finally:
#     print("This will print always")

# Raising Exceptions #

# x=-5
# if x<5:
#     raise ValueError("Negative number not allowed")

# Custom Exceptions #

class NegativeNumberError(Exception):
    pass
def check_number(num):
    if num < 0:
        raise NegativeNumberError("Negative numbers are not allowed!")
# try:
#     check_number(-10)
# except NegativeNumberError as e:
#     print(e)


