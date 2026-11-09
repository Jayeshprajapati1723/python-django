o = input("enter a string : ")
le = len(o)-1
# hseyaj
temp = o 
r =""
for i in range(le,-1,-1):   
      print(o[i],i,end =" ") 
      r += o[i] 

print(r)    
if(r==o):
        print("string is pallindorm",o,"==",r)
else :
      print("not pallindrom") 