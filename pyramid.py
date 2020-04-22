# printing a pyramid triangle
x= int(input("Enter the no. of rows: "))
m=x-1
for i in range(0,x):
    for k in range(0,m):
        print(end=" ")
    for j in range(0,i+1):
        print("*", end=' ')
    print("\r")
    m=m-1