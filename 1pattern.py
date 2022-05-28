a=int(input("enter number"))
b=0
for i in range(0,a):
    for j in range(0,i+1):
        b=b+1
        print(b,end=" ")
    print()