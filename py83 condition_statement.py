#Question--> if cost price and delling price of an item is input through keyboard.Write a program to determine how muvh profit he made or how much loss he got?

cp=float(input("enter cp:"))
sp=float(input("enter sp:"))
d=sp-cp
if(d>0):
    print("profit",d)
elif(d<0):
    print("loss",d)    #print("loss",abs(d))
else:
    print("no profit no loss")
