# largest elemets of list 
l = []

n = int(input("ENTER SIZE OF LIST"))
for i in range(n) : 
    data = int(input("ENTER DATA"))
    l.append(data)

largest = l[0]
sl = None
for i in l :
    if(largest<i):
        largest = i

    elif(sl == None or i> sl):
        sl = i    


print("largest elements of list ",l,"=",largest)


print("second largest ",sl)