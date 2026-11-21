n= int(input("enter n to find sum of factorial series "))
if(n<=0):
    print("invalid number")
else:
    fact = []
    for i in range(1,n+1):
     if(i!=n):
        print(i,"!+",end=" ")
     else:
        print(n,"!")    

    f=1
    for j in range(i,0,-1):
        f*=j
    fact.append(f)

    s =sum(fact)
    print("=",s)

