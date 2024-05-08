a=int(input("enter 1st number:"))
b=int(input("enter 2nd number:"))
option=input("""select an option
1. add
2. mul
""")
match(option):
    case "1":
        print(a+b)
    case "2":
        print(a*b)
    case _:
        print("invalid option")
