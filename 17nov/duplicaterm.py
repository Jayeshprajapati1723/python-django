# duplicate remove from list
l= [1,1,1,2]
print(l)

a = list(dict.fromkeys(l))
# remove kr skte h list k duplicate se remove kro fromkeys 

print(a,type(a))