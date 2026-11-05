'''
n = 795 




'''


n = int(input("enter a no to get its reverse")) 
temp = n 
r = 0 
a = 0
while(n!=0) : 
              a = n%10 
              r = (r*10)+a 
              n = n//10


print("before reverse ",temp)
print("r no after reverse  ",r)