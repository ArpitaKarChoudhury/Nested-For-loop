a= int(input("enter number"))
for i in range (1,a+1):
    for k in range(i,a):
        print(" ",end=" ")
    for j in range(0,i):
        print(i-j,end=" ")
    print()