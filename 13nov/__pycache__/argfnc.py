# middle among three using fnc 

def mid(a,b,c):
    # a = int(input("enter a "))
    # b = int(input("enter b "))
    # c = int(input("enter c "))

    if((a>b and a<c)  or (a>c and a<b)):
        print("a is mid",a)
    
    if((b>a and b<c) or (b<c and b>a)):
        print("b is mid",b)    
    
    if((c<a and c>b) or (c>a and c<b)):
        print("c is mid",c)    


mid(1,1.5,2)        
mid(2.5,3.9,4.22)
mid(22/2,0.53,7.98)
mid(4,5,0)
