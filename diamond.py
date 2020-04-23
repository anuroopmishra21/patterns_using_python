# diamond pattern using python
x= int(input("Enter the width of the diamond "))
m=x-1
for i in range(0,x):
    for k in range(0,m):
        print(end=" ")
    for j in range(0,i+1):
        print("*", end=' ')
    print("\r")
    m=m-1
m=1
y=x-1
for i in range(0,x-1):
    for k in range(0,m):
        print(end=" ")
    for j in range(0,y):
        print("*", end=' ')
    print("\r")
    m=m+1
    y=y-1s