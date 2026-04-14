# creating set #

# using curly braces
# a={1,2,3,4,5}
# print(a)

# using set function
# a=set([1,2,3,4,5])
# print(a)

#empty set
# a = set()
# print(type(a))

#Accessing set items
# a={1,2,3}
# print(2 in a)
# print(4 in a)

#Adding Items to a set

#single Item
# a={1,2,3}
# a.add(4)
# print(a)

#Multiple Item
# a={1,2,3}
# a.update([5,6,7])
# print(a)

#REMOVING ITEMS FROM A SET

#remove()
a={1,3,2,4}
# a.remove(2)
# print(a)

#discard()
# a.discard(4)
# print(a)

#pop()
# a.pop()
# print(a)

#clear()
a.clear()
print(a)

# joining set #
# union

# a={1,2,3}
# b={4,5,6}
# r=a.union(b)
# print(r)

#intersection
# a={1,2,3}
# b={2,3}
# r=a & b
# print(r)

#Diference
# a={1,2,3}
# b={2,3}
# r=a - b
# print(r)

#symmetric difference
# a={1,2,3}
# b={2,3,4}
# r=a ^ b
# print(r)

#subset
# a={1,2}
# b={1,2,3,4}
# print(a.issubset(b))

# #Superset
# b={1,2}
# a={1,2,3,4}
# print(b.issubset(a))

# #frozenset
# a=frozenset([1,2,3,4])
# print(a)



