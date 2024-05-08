#some values is shared to multiple references

x=10
print(x,id(x))
y=10
print(y,id(y))
z=10
print(z,id(z))

y=20
print(x,id(x))
print(y,id(y))
print(z,id(z))
