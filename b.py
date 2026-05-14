# import mymodule

# print(mymodule.greet("susmi"))
# print(mymodule.greet1("Aami"))
# print(mymodule.greet3("susmi"))

# import mymodule as mm 

# print(mm.greet("susmi"))
# print(mm.greet1("Aami"))
# print(mm.greet3("susmi"))

# from mymodule import greet,greet1,greet3

# print(greet("susmi"))
# print(greet1("Aami"))
# print(greet3("susmi"))

# Built-in Modules #

# import math
# print(math.sqrt(36))
# print(math.factorial(5))


# from datetime import datetime
# now=datetime.now()
# print(now)

# import os
# x=os.getcwd()
# print(x)

# import numpy as np

# arr = np.array([1, 2, 3])
# print(arr)


# import pandas as pd 

# data = {'Name': ['Alice', 'Bob'], 'Age': [25, 30]}
# df=pd.DataFrame(data)

# print(df)


import matplotlib.pyplot as plt
x = [1, 2, 3, 4]
y = [10, 20, 25, 40]
plt.plot(x, y)
plt.show()
