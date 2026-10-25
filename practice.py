print("hello")


a=float(input("First number: "))
op=input()
b=float(input("Secound Number: "))
if(op=="*"):
    print(a*b)
elif(op=="/"):
    if b==0:
        print("Error: divisible by zero")
    else:
        print(a/b)
    
elif(op=="+"):
    print(a+b)
elif(op=="-"):
    print(a-b)
else:
    print("unknow operator : ", op)

