# diffrent calculation based 
# types diffrent types of area 
print("press 1 for km to meter ")
print("press 2 for  meter to  km  ")
print("press 3 for ferhanite to calcius ")
print("press 4 for calcius to ferhanite ")
print("press 5 for kg to gm")
print("press 6 for gm to kg")
print("exit for press 7")

while(ch!=7)  :   ch= int(input("enter your choice"))

if(ch==1) : 
             val = float(input("enter km to cal get meters"))
             res = val *1000 
             print(val,"to meter",res)

if(ch==2) : 
             val = float(input("enter km to cal get meters"))
             res = val/1000 
             print(val,"to kmmeter",res)

if(ch==3) : 
             val = float(input("enter km to cal get meters"))
             res = (val-32)*(5/9) 
             print(val,"to calcius",res)             

if(ch==4) : 
             val = float(input("enter to celcius to get fehranite "))
             res = ((val*1.8)+32) 
             print(val,"to fehranite ",res)


if(ch==5) : 
             val = float(input("kg to grams"))
             res = val*1000 
             print(val,"to gram",res)

if(ch==6) : 
             val = float(input("gram to kilograms"))
             res = val/1000 
             print(val,"to meter",res)

if(ch==7) : 
          print("ended chat")
          exit ;    
                      