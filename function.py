# # def keyword using for function #
# def greet():
#     print("hello")
# greet()

# # with arguments and parameters
# def greet(name,place):
#     print(f"my name is {name} i am from {place}")
# greet("susmi","valanchery")

# with return statements
# def sum(a,b):
#     return a+b
# result=sum(3,4)
# print(result)

# with default parameters
# def greet(name,place="malappuram"):
#     print(f"my name is {name} i am from {place}")
# greet("susmi")

# Docstrings in Functions #

# def sum(a, b):
#  """This function adds two numbers."""
#  return a + b
# result=sum(3,4)
# print(result)
# print(sum.__doc__)

# Lambda functions are anonymous functions in Python
# syntax: lambda arguments: expression #

# add=lambda a,b:a+b
# print((add(3,5)))

# Lambda Functions with map(), filter(), and reduce()
# using map():

# a=[1,3,5,6]
# square=map(lambda x:x**2,a)
# print(list(square))

# using filter():

# a=[1,2,3,4,5,6,7,8]
# even=filter(lambda x:x%2==0,a)
# print(list(even))

# using reduce()
# from functools import reduce

# a=[1,2,3,4,5,6,7,8]
# sum=reduce(lambda x,y:x+y,a)
# print(sum)


# Higher order function #

# def sum(a,b,operator):
#     return operator(a,b)

# add=lambda a,b:a+b
# mul=lambda a,b:a*b

# print(sum(2,3,add))
# print(sum(2,3,mul))

# Function Scope #

# x=10  #global scope
# def abc():
#     x=20 #enclosing scope
#     print(x)
#     def xyz():
#         x=30 #local scope
#         # print(x)
#     xyz()    
        
# abc()
# print(x)


# arbitrary arguments #

# def num(*a):
#     print(a)
#  num(1,2,3) # error
# num(1,2,3,4) # after giving single star(*) in parameter it will take all the element as tuple

# eg:
# def sum(*a):
#     total=0
#     for i in a:
#         total+=i
#     return total
# result = sum(1, 2, 3, 4, 5)
# print(result)



# keyword arguments #

# def stud(**a):
#     print(a)
# stud(name="susmi",age="20",place="delhi")  # give double star(**) in parameter


# eg:
# def stud(**kwa):
#     for key,value in kwa.items():
#         print(f"{key}:{value}")
# stud(name="susmi",age="20",place="delhi")

# full function example #

# def full_function(para,*args,**kwa):
#     print("regular parameters:",para)
#     print("arbitrary arguments:",args)
#     print("keyword argumets:",kwa)

# full_function(0,20,30,40,50,name="susmi",age="20")


# recursion : A function call itself #

# def fact(n):
#     if n==0 or n==1:
#         return 1
#     else:
#         return n*fact(n-1)
# print(fact(5))


# factorial using loop #

# n=int(input("enter the number: "))

# fact=1
# for i in range(1,n+1):
#     fact=fact*i
    
# print(f"factorial of {n} is {fact}")


# Tail recursion #

# def fact(n,accumulator=1):
#     if n==0 or n==1:
#         return accumulator
#     else:
#         return fact(n-1,accumulator * n)

# print(fact(5))

# example 1 #
# Fibonacci

# def Fibonacci(n):
#     if n==0:
#         return 0
#     elif n==1:
#         return 1
#     else:
#         return Fibonacci(n-1) + Fibonacci(n-2)
# print(Fibonacci(5))

# example 2 #
# sum of list

# def sum(list):
#     if not list:
#         return 0
#     else:
#         return list[0] + sum(list[1:])
# print(sum([1,2,3,4]))


   
