a=int(input("enter 1st number:"))
b=int(input("enter 2nd number:"))
option=input("""select an option
1. add
2. mul
""")
if(option=="1"):
    print(a+b)
elif(option=="2"):
    print(a*b)
else:
    print("invalid option")
