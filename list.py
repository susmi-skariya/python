# Creating List #

# L= [1, 2, 3, 'Python', 4.5]
# print(L)

# Acsessing List #
# l=["apple","orange","Dog"]
# print(l[1])

# Range of Indexes: You can use a range of indexes to access multiple items (slicing).
# l=[10,20,30,40,50,60]
# print(l[1:5])

# Changing List Items #

# L= [1, 2, 3, 'Python', 4.5]
# L[1]='HTML'
# print(L)

# Adding Items to a List # several ways to add elements to a list

# Append() #
# L= [1, 2, 3, 'Python', 4.5]
# L.append('HTML')  #Adds an item to the end of the list#
# print(L)


# Insert() #
# L= [1, 2, 3, 'Python', 4.5]
# L.insert(2,'CSS')
# print(L)

# Extend() #
# L= [1, 2, 3, 'Python', 4.5]
# L1=['HTML','CSS','JS']
# L.extend(L1)
# print(L)

# Removing Items from a List #

# Remove() #
# L= [1, 2, 3, 'Python', 4.5]
# L.remove('Python')
# print(L)

# POP() #
# L= [1, 2, 3, 'Python', 4.5]
# L.pop(1)
# print(L)

# DEL #
# L= [1, 2, 3, 'Python', 4.5]
# del L[3]
# print(L)

# CLEAR() #
# L= [1, 2, 3, 'Python', 4.5]
# L.clear()
# print(L)

# List Methods #

# count(): Returns the number of occurrences of a specific value. #

# L= [1, 2, 3, 'Python',4,3, 4.5]
# L.count(3)
# print(L)

# index(): Returns the index of the first occurrence of a specific value. #

# L = ['apple', 'banana', 'cherry']
# L.index('banana')
# print(L)

# reverse(): Reverses the order of the list. #

# L = [1, 2, 3]
# L.reverse()
# print(L)

# sort(): Sorts the list in ascending order.#
# L = [3, 1, 2]
# L.sort()
# print(L)

# copy(): Returns a shallow copy of the list.#
# OL = [1, 2, 3]
# CL = OL.copy()
# print(CL) 

# Sorting a List #
numbers = [3, 5, 1, 4, 2]
numbers.sort()
print(numbers) # Ascending order

numbers = [3, 5, 1, 4, 2]
numbers.sort(reverse=True)  #Descending order
print(numbers)


# Joining Lists

l1 = ['apple', 'banana']
l2 = ['cherry', 'orange']
combined_list = l1 + l2
print(combined_list)