# reading files #

# read() #

# file=open("sample.txt","r")
# print(file.read())
# file.close()



# readline() #

# file=open("sample.txt","r")
# print(file.readline())
# file.close()

# readlines() #

# file=open("sample.txt","r")
# print(file.readlines())
# file.close()

# file = open("sample.txt", "r+")
# file.write("hellooo.\n")
# file.seek(0)
# print(file.read())
# file.close()

# writing to file #

# write()

# file=open("sam.txt","w")
# file.write("Hello world") # over write the exsisting content
# file.close()

# file=open("sample.txt","w")
# file.write("Hello world") # over write the exsisting content
# file.close()

# writelines()

# file=open("sample.txt","w")
# file.writelines(["Hello\nPython programming \n"]) 
# file.close()

# file = open("sample.txt", "w+")
# file.write("helloooi.\n")
# file.seek(0)
# print(file.read())
# file.close()

# Appending Data #

# file = open("sample.txt", "a")
# file.write("hello aami.\n")
# file.close()

# file = open("sample.txt", "a+")
# file.write("hello susmi.\n")
# file.seek(0)
# print(file.read())
# file.close()

# with statements

# with open("sample.txt",r)
# print(file.read())

# seek & tell #

# seek()

# file = open("sample.txt", "w")
# file.write("hello")
# print(file.seek(1))   
# file.close()

# tell()

# file = open("sample.txt", "w")
# file.write("hello")
# print(file.tell())   
# file.close()

# relative path & absolute path #

# relative path

# file=open("sample.txt","r")
# print(file.read())
# file.close()

# absolute path

# file=open("c:/Users/HP/Desktop/susmi/python/sample.txt","r")
# print(file.read())
# file.close()

