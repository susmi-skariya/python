a=int(input("enter a number"))
b=int(input("enter a number"))
c=(input("enter a operator"))
if c=="+":
    result= f"result is {a+b}"
    print(result)

elif c=="-":
    result= f"result is {a-b}"
    print(result)

elif c=="*":
    result= f"result is {a*b}"
    print(result)

elif c=="/":
    result= f"result is {a/b}" if c=="/" else "can't divided by 0"
    print(result)

