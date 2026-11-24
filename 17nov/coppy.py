import copy 
a= [1,2,3]
b = a.copy()

# deepcopy() : creates a completely independent copy of the original object including all neasted elements ,changes made to deep-coppied 

l = [["neasted","list hai"],"simple","list hai",123,321]
l2 = copy.deepcopy(l)

print(l)
print(l2,"only deepcoppy se coppy kra to new m hi change hoiga ")

l2[0][0]="nested deep coppy hua "

print(l)
print(l2,"only deepcoppy se coppy kra to new m hi change hoiga ")

# shallow copy 
# a shallow  copy create a new object but original = refrence dono me changes hoga 
n =[["a","aa"],"b","c"]
m= copy.copy(n)
print(n)

m[0][1] ="chch"
# neasted me change krega 
print(n)

print(m)
# faster than deep copy 