'''TUPLEISA COLLECTION of same plus diffrent diffrent datatype values  tuple is immutable means or unchangeble touple is also a contructor tuple is smane as list in terms of order indexing and allow duplicate elements refrence variable name = (ele,eles,eless,elsesss)'''

a = (1,2,2)
print(a)

print(type(a))

print(max(a))
print(min(a))
print(len(a))

# a.append(5)
'''    a.append(5)
    ^^^^^^^^
AttributeError: 'tuple' object has no attribute append'''

# tuple to list 
b = list(a)
b.append(5)
print(b)

# list to tuple 
a = tuple(b) 
print(a)

'''
packing in tuple mutliple value ko single variable me krna : it is imutable the processing of assign pass mutliple to single values or argues


'''

# def se funciton 
# packing in tuple
# x ek value lega 
# *x se tuple bna skte h 
def demo(*x):
    print(x)
    

demo(10)
demo(20,30)
demo(1,2,2)


# unpacking of tuple 
'''to extract the into the single varaible is called unpacking bahar lana 

(val,valtwo,valthree,.....)= refrence name 
'''
# packing
name = ("j","k","l")
(x,y,z) = name
print(x)
print(y)
print(z)
# jitni value itne variable varible == value if not use *valaue..
name = ("j","k","kj","hello","bye")
(x,y,z,*o) = name 
print(o)
print(x)
print(y)
print(z)