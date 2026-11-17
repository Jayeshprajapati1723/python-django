# middle among three using fnc 

def mid():
    a = int(input("enter a "))
    b = int(input("enter b "))
    c = int(input("enter c "))

    if((a<b and a<c)  or (a>b and a>c)):
        print("a is mid",a)
    
    if((b<a and b<c) or (b>a and b>c)):
        print("b is mid",b)    
    
    if((c<a and c<b) or (c>a and c>b)):
        print("c is mid",c)    


mid()        
# no return type with arguemnt passing 
def add(a,b,c):
    add=a+b+c
    print(a,"+",b,"+",c,"=",add)


add(2,3,5)










