# list collection 
# diffrent types of data types + same collection 

'''
list is capable to store multiple values in a single variable 
it is mutable (changeble) in nature : LIC
it is orderd in nature and default index from stat = 
0 
it allow duplicate elements : LIEDUPLICATE
# list is dynamic in nature so no need to define size 
# list is also a constructor 

synatax : refrence variable name = [al,1,1,112, 1112144]








'''
a = [10,20,30,40,50] 
print(type(a),a)

# number function 
print("max",max(a))

print("min",min(a))

print("sum",sum(a))

print("length",len(a))

# list method 
'''
append functionn : add in last 

'''
print("append",a.append(60)) 


# pop : this method remove the element from last of the list with or without index 
# listname.pop() or list.pop(7) 
n = int(input("enter no of legnth "))
a = []
for i in range(0,n) : 
                     data = input("enter your data ")
                     a.append(data) 

a.pop(1)  
print("your list is ready",a)                    


# remove value k liye h remove(value pass kr do )
a.remove("j") 
print()


# sort to arrange in ascending order if we reverse = True than it get to arrange in descending order 
a.sort()