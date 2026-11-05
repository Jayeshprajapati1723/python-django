n= int(input("enter n to check it is prime "))
found = 0 
if(n!=1 or n!=0 ) :
    for i in range(2,n):
       
      if(n%i==0) : 
            found =1 
            break 

if(found ==1  ) : 
                  print("NON PRIME")
else : 
        print("yeah it is prime no ",n)                        