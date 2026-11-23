p = float(input("enter marks of phy"))
c = float(input("enter marks of chem"))
m = float(input("enter marks of chem"))
tot = p+c+m 
import sys 
# from ../13.nov/pkg import *
per= tot/3

if(per>=90 and per<=100):
    print("A+")
elif(per>=80 and per<=90):
    print("B+")    
elif(per>=70 and per<=90):
    print("B+")
elif(per>=50 and per<=70):
    print("C+")           
elif(per>=33 and per<=50):
    print("D+")
else:
    print("F YOUR R FAIL")    
