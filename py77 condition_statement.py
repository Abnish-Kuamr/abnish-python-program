#match condition (added in 3.10 version)
option="hi"
match(option):
    case 1:
        print("apple")
    case 2:
        print("mango")
    case 5.5:
        print("orange")
    case "hi":
        print("banana")
    case _:
        print("invalid option")
print("bye")        
