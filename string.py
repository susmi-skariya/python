# String can enclosed in (" "),('') #
# s="Susmi"
# S="Skariya" 
# print(s)
# print(S)

# String Slicing #

# s="susmi skariya" 
# print(s[1:0]) # Omiting the first letter from the first string #
# print(s[1:6]) # Omiting the letters starting from index 6 #

# Negative Slicing # (Negative numbers can be used to start slicing from the end.)

# print(s[0:-1])  #Omiting the last character only#
# print(s[-6:-1]) #Omiting the first 6 characters and last 1 character#

#skipping character#
# print(s[0:15:2]) #skipping the characters by one

# Reversing String #
# print(s[::-1])  #reverse the string

# Modifying String #
# name=s.replace("susmi","Aami") # "keyword", "replace"
# print(name)

# Upper case and Lower case #
# print(s.upper()) 
# print(s.lower())

#String Concatenation#

# s1="susmi"
# s2="skariya"
# name= s1 + ", " + s2
# print(name)

# using join method # (concatination)
# words=["susmi","k","skariya"]
# name=" ".join(words)
# print(name)

#Format String# (#Python provides several ways to format strings, allowing you to inject values into a string template.#)

# Using % Operator #

# name = "Aami"
# age = 25
# string = "My name is %s, and I am %d years old." %(name, age) #(almost same as c)
# print(string)

# Using format() method #

# name = "Aami"
# age = 25
# string = "My name is {}, and I am {} years old." (name, age) 
# print(string)

# Using f-strings (Python 3.6+):The most modern and efficient way to format strings #

# name = "Ajay"
# age = 26
# string = f"My name is {name}, and I am {age} years old."
# print(string)

# Escape Characters #

# print("Hello\nWorld")
# print("Hello\"World\"")
# print("Hello\tWorld")
# print("Hello\'World")
# print("Hello\\World")

#String Methods#

# len(): Returns the length of the string. 

s = " Hello, World! "
# print(len(s))

# strip(): Removes leading and trailing whitespace.

# print(s.strip())

# split(): Splits the string into a list of substrings based on a separator

# print(s.split(","))

# find(): Returns the index of the first occurrence of a substring. Returns -1 if the substring is not found.

# print(s.find("HELLO"))
# print(s.find("World"))

# count(): Returns the number of times a substring occurs in the string.

# s = "Hello, Hello, World!"
# print(s.count("Hello"))

# startswith() and endswith(): Check if a string starts or ends with a specific substring.

# s = "Hello, World!"
# print(s.startswith("Hello")) # Output: True
# print(s.endswith("world!")) # Output: False

# upper() and lower(): Convert the string to uppercase or lowercase.

# s = "Hello, World!"
# print(s.upper()) # Output: HELLO, WORLD!
# print(s.lower()) # Output: hello, world!

# replace(): Replaces a substring with another substring.

s = "Hello, World!"
print(s.replace("World", "Python")) # Output: Hello, Python!