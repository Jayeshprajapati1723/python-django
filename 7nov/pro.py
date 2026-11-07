'''lcm of multiple n '''
l = []
n = int(input("enter size of list "))
while(n!=0) :
       d = int(input("enter data"))
       l.append(d) 
       n-=1


print(l)
ln = len(l)
m = max(l)
lcm = []
for i in l :
       while(i!=1):     
         for j in range(2,m):
              if(i%j==0):
                     i= i//j
                     lcm.append(j)


print(lcm,"lcm")                     