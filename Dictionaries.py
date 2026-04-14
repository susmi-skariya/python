#Creating a Dictionary
# a={"name":"susmi","age":20,"city":"valanchery"}
# print(a)

# b=dict(name="susmi",age=20,city="valanchery")
# print(b)

# #Empty Dictionary
# c={}
# print(c)

#Accessing Dictionary Items

#Accessing with Brackets
# a={"name":"susmi","age":20,"city":"valanchery"}
# print(a["name"])

#Using get()
# a={"name":"susmi","age":20,"city":"valanchery"}
# print(a.get("age")) 

#Changing Dictionary Items
# a={"name":"susmi","age":20,"city":"valanchery"}
# a["name"]="Aami"
# print(a)

#adding new elements
# a={"name":"susmi","age":20,"city":"valanchery"}
# a["fname"]="Susmi"
# print(a)

#Removing Items from a Dictionary

# pop(key)
# a={"name":"susmi","age":20,"city":"valanchery"}
# age=a.pop("age")
# print(a)

# popitem()
# a={"name":"susmi","age":20,"city":"valanchery"}
# item = a.popitem()
# print(a)

#del statement:
# a={"name":"susmi","age":20,"city":"valanchery"}
# del a["age"]
# print(a)

#clear:
# a={"name":"susmi","age":20,"city":"valanchery"}
# a.clear()
# print(a)

#  Copying a Dictionary

# Using copy():
# a={"name":"susmi","age":20,"city":"valanchery"}
# copy=a.copy()
# print(copy)

# Using dict() constructor:
# a={"name":"susmi","age":20,"city":"valanchery"}
# copy= dict(a)
# print(copy) 

# Nested Dictionaries
# a = {
#  "p1": {"name": "John", "age": 30},
#  "p2": {"name": "Alice", "age": 25}
# }

# # print(a["p1"]["name"])
# a["p1"]["name"]="aami"
# a["p2"]["fname"]="jhon"  #adding fname as new element
# print(a)

#Dictionary Methods
# keys():

a={"name":"susmi","age":20,"city":"valanchery"}
print(a.keys())

#value():
print(a.values())

#items():
print(a.items())

# update():
# a={"name":"susmi","age":20,"city":"valanchery"}
# a.update({"name":"Aami","age": 31})
# print(a)

# fromkeys():
# keys = ["name", "age", "city"]
# new= dict.fromkeys(keys, "Unknown")
# print(new)

# setdefault(key, value):
a={"name":"susmi","age":20,"city":"valanchery"}
city=a.setdefault("city","Malappuram")
print(a)

b={"name":"susmi","age":20}
city=b.setdefault("city","Malappuram")
print(b)