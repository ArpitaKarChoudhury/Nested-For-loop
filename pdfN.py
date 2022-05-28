a= int(input("enter number"))
c=1
for i in range (0,a+1):
    c=c+2
    for j in range(0,i+1):
        print(i*j,end=" ")
    print()