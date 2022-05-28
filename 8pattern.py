a= int(input("enter number"))
for i in range(1,a+1):
    b=a
    for c in range(i,b):
        print(" ",end="")
    j=1
    for j in range (j,i+1):
        print("*",end=" ")
    print()
for i in range (0,a):
    j=0
    for c in range (j,i):
        print(" ",end="")
    for d in range(i,a):
        print("*",end=" ")
    print()
