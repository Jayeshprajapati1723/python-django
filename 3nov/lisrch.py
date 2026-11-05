'''linear search'''
a = [3,1,2,9,7]
found = 0 
s = int(input("search here : "))
for i in range(0,len(a)) :
  if(a[i]==s) : 
     found =1 
     break
if(found==1) :
     print("founded result ",s)
else : 
 print("no founn in pages")              