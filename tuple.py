# creating tuple #

# A=(1,2,3,4)
# print(A)

# a=(1,) # single tuple
# print(a)

# Accesing Tuple Items #

# A=('apple', 'banana','cherry', 'orange')
# print(A[1])
# print(A[-1])

# slicing tuple

# A=[10,20,30,40,50,60]
# print(A[1:3])

# Updating a Tuple #

# Re-assigning tuple
# A=(10,20,30,40,50,60)
# A=(1,2,3,4,5,6)
# print(A)

# Convert Tuple to List
A=(10,20,30,40,50,60)
a=list(A)
a[2]=3
a=tuple(a)
print(a)



# unpacking #

# A= ('apple', 'banana', 'cherry')
# (f1, f2, f3) = A
# print(f1) 
# print(f2) 
# print(f3)

# Using * (asterisk)
# A=(1,2,3,4,5,6,7)
# (n1,*n2,n3)=A
# print(n1)
# print(n2)
# print(n3)


# joining tuple
# a=(1,2,3,4)
# b=(5,6,7,8)
# c=a+b
# print(c)

# count() #
# a=(1, 2, 3, 4, 5, 1, 7, 8)
# print(a.count(1))

# index() #
# a=(1, 2, 3, 4, 5, 1, 7, 8)
# print(a.index(3))

# Deleting a Tuple #
# a=(1, 2, 3, 4, 5, 1, 7, 8)
# del a
# print(a)