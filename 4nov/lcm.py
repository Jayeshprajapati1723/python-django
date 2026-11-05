# lcm of given no 
n = int(input("enter a"))
m = int(input("enter b"))
temp = m 
tempp = n
lcm =1 
if(n>m):
    e =n
else:
    e =m    
while(n!=1):
    for i in range(2,n+1):
        if(n%i==0):
            n=n//i
            lcm *=i



while( m!=1):
    for i in range(2,m+1):
        if(m%i==0):        
            m=m//i
            lcm *=i            
l =1
print(e) 
n1 = tempp
n2 = temp
while(temp!=1 and tempp!=1):
              for i in range(2,e+1):
                if(temp%i==0):
                        temp = temp//i
                        l*=i
                if(tempp%i==0):
                     tempp= tempp//i 
                     l*=i
                                        

print("method2:",l,"is the lcm of ",n1,",",n2)


print(lcm,"is the lcm of ",n1,",",n2)
