li = [1,2,3,4]
li2 = li.copy() 
print(li2) 
# coppy hmesha new list bhi bna skta h 

# extend krta h dusri list k elements ko hmara old list me jisme hm add krna ho merge krna a hoa
li2.extend(li)
print(li2)

# del keyword 
# del is a reserve word or keyword for remove any refrence or deallocate an existing refrence deleted properly no append is perform 

del li 
# if we li print than name error generate 