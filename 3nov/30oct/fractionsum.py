# 1/1+................ +1/n
limit = int(input("enter limit"))
a = 1
sum = 0
while(a<=limit) :
                 sum += 1/a
                 a+=1

print("the fractinal sum upto ",limit ,"=",sum)                 