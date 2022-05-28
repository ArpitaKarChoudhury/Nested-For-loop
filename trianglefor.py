a=int(input("enter number"))
b=0
for i in range(b,a+1):
    for j in range (i,a):
        print(" ",end="")
    else:
        print("*",end=" ")
    for k in range (b+1,i):
        print(" ",end=" ")
    else:
        print("*",end=" ")     
    print()
c=0
for k in range(c,a+1):
    for j in range (k,c,-1):
        print(" ",end="")
    else:
        print("*",end=" ")
    for j in range (k,a-1):
        print(" ",end=" ")
    else:
        print("*",end="")
    print() 