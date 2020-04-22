# printing a pyramid triangle of numbers
x= int(input("Enter the no. of rows: "))
m=x-1
for i in range(0,x):
    for k in range(0,m):
        print(end=" ")
    for j in range(0,i+1):
        print(j+1, end=' ')
    print("\r")
    m=m-1