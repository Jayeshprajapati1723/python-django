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
         fact = []

            
         for j in range(2,m+1):
              if(i==1):                 
                      break 
                    
              while(i%j==0):
                     i= i//j

                     fact.append(j)
         lcm.append(fact)              


print(lcm,"lcm")                     
final = 1
for i in [2,3,5,7,11,13] :
       counts =[]
       for j in lcm :
         counts.append(j.count(i))
       print(i, counts, max(counts))   
       final *= i ** max(counts) 




print(counts)
print(final,"final lcm ")