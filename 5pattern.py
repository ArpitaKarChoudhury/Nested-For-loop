a= int(input("enter number"))
for i in range (0,a):
    j=0
    for c in range (j,i):
        print(" ",end="")
    for d in range(i,a):
        print("*",end=" ")
    print()