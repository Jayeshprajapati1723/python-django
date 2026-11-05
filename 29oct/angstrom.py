# angstrome number three digit ko alg kro or teeno ke cube krke sum jo aye vo uske hi wqual hi hona chahiye us no ke 

n = int(input("enter a no to check angstrome"))
temp = n 
# d1 = n%10 
# n = n//10

# d2 = n%10
# d3 = n//10


# rs  = ((d3**3))+((d2**3))+(d1**3) 

# print(rs)

c = 0
while(n!=0) : 
              a= n%10
              c += a**3
              n =n//10
             





if(temp == c) :
                print("no is angstrome",c)
else : print("NOT ANGSTROME ")                