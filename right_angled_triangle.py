# printing a right angled triangle made of asteriks
x= int(input("Enter the no. of rows: "))
for i in range(0,x):
    for j in range(0,i+1):
        print("*", end=' ')
    print("\r")