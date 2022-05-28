a = int(input("Enter the number of rows:"))  
for i in range(1,a+1):
    b=a
    for c in range(i,b):
        print(" ",end="")
    j=1
    for j in range (j,i+1):
        print("*",end=" ")
    print()
