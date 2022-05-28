a= int(input("enter number"))
b=0
for i in range (1,a+1):
    for j in range(0,i,2):
        b=b+1
        print(b,end=" ")
    print()