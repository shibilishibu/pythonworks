limit=int(input("enter the row"))
for i in range(1,limit+1):
    for j in range(i,0,-1):
        print(j,end=" ")
    print()
    