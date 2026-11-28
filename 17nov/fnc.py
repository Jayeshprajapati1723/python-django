# user defined fnc : type first 
'''
one : no return type no arguemtn 
def functionname() :
                #    write logic 
functionname()


two : 


'''
# type 1 no return no args 
def findmax():
    x =12
    y=13
    if(x>y):
        print(x ,"is max than",y)
    if(x<y):
            print(y ,"is max than",x)    

findmax()

 #type 2 no return type with args 
def sum(x,y):
     print(x+y,"sum fnc with arg no rtn type ")

x = int(input("enter x"))
y = int(input("enter y"))
sum(x,y)    

# type 3 : with rtn without args
def rtn():
     x = int(input("enter x"))
     y = int(input("enter y"))


     if(x>y):
          return x
     else:
          return y

res = rtn()
print(res)     


# type 4 with return with arguemnts 
def rtn(x,y):
     

     if(x>y):
          return x
     else:
          return y
x = int(input("enter x"))
y = int(input("enter y"))

res = rtn(x,y)
print(res)     

# default argument funciton 
def add(a=100,b=10,c=30):
     print(a+b+c)

add(1)     
add(6,20)
add(777,777,777)
# right to left shift chlta h 
_____________________________________
# draw pattern 
'''
1 2 3 4 5 6 7 8
 7 6 5 4 3 2 1
  1 2 3 4 5 6
   5 4 3 2 1
    1 2 3 4
     3 2 1
      1 2
       0 
    

'''