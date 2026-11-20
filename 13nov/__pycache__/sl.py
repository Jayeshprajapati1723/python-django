l = []
n = int(input("enter size of n "))
for i in range(n):
    d = int(input("enter data "))
    l.append(d)

print("your list is ",l)

fl = l[0]
sl= 1

for i in l :
    if(fl<i):
        sl = fl
        fl=i
    if(i<fl and i>sl):
        sl =i    
        
         


print("second largest",sl)
print("first largest",fl)         
