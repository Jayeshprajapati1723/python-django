n = int(input("enter size of no of list "))
num =[]
for i in range(n):
    data= int(input("enter your data  "))
    num.append(data)
    

print(num,"your numbers")
'''
2 = 2x1
4 = 2 x 2
6 = 2 x 3
6 = 2x 3

'''

hcf =[]
end=max(num)
for n in num :
    factors = []
    for i in range(2,end+1):
        while(n%i==0):
            n=n//i
            factors.append(i)
    hcf.append(factors)        

print(hcf)
cn =[]
ansofhcf= 1
for i in [2,3,5,7]:
    count =[]
    for j in hcf :
     count.append(j.count(i))
     print(j,"=",count,"itni bar aya ")
    if(min(count)!=0):
        ansofhcf *= i*min(count)
        print(ansofhcf)
       
   
    cn.append(count)     

print(cn)
print(ansofhcf,"hcf")
