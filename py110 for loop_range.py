for x in range(1,5): #default step-->+1
    print(x)

print('---------------------')

for x in range(5):  #default start-->0, step-->+1
    print(x)

print('---------------------')

for x in range():
    print(x)    #error

print('---------------------')

for x in range(1,5,0):
    print(x)    #error

print('---------------------')
    
for x in range(1,5,.1):
    print(x)    #error
