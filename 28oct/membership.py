# membership oeprator is used to used to check the given dtata is available is given collection or not 

# do type ke 
# in and notin

# in data exit h to true krega
# not in jab data nhi hoga to true return 

# string collectio 
str1= "python is a programing lang"
search = "python"
res =search in str1 
print(res)
print("your searches " ,search)
print("full data",str1)  

search = "lang"
res = search not in str1
print(res)
print("your searches " ,search)
print("full data",str1)  

# id() funciton is a predefined function of python its returns unique memory address of given refrence id value must be unique lifecycle 
# syntactly return address = id (refrence_name) 

# data type samme to address same rhega id ( se niaklne pr ) data bdla value same type same to 

a =10 
print(a) 
print("type of a" ,type(a)) 
print("address of a ",id(a)) 

# value same or data type same tbhi address same 

a =10 
print(a) 
print("type of a" ,type(a)) 
print("address of a ",id(a)) 



# identity operator is used to chekc the given refrence has same or diffrent identity  1 is 2 is not if refrence has same address ture if refrence has diffrent it return true ohterwise false 
# is ture dega jab refrence same hoga 
# is not me 

a = 10 
b = 10
# b= 15 false 
b = 15.5 

rs = a is b 
print (rs) 

rs = a is not b 
print(rs)