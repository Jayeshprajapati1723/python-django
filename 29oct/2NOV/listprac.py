li = ["j","k",1,2,3]
# jo value remove krnah  
li.remove("k")
print((li))

a =[5,6,9,12,2.5]
a.sort()
print(a)


# DESCENDING K LIYE 
a.sort(reverse=True) 
print(a)

a.reverse()
print(a)

# insert() if the index not found no error but add in last 
# (index,value)
a.insert(100,100)
print(a)
a.insert(1,2.5)
# count the iteration of duplicate elements count(value)
print(a.count(2.5))

# clear element remove hoga sturcuttre whi rhega clear () 
# sb clear ho jayenge ..
a.clear()
print(a)

# coppy : coppy () : coppy list as a refrence
b = li.copy() 
print(b)
# index : return index of specific value 
print(b.index("j"))

# extend : addd element fform another list dusri list k element add kr deta h (list 1 passs kro )
b.extend(a)
print(a) 
print(b)