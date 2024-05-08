#match condition (added in 3.10 version)
option=3
match(option):
    case 1|2:
        print("apple")
    case 2|3:
        print("orange")
    case "hi":
        print("banana")
    case _:
        print("invalid number")
print("bye")        
