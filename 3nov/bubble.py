# bubble sorting 
# phle ek ko uthao or compare kro sbse 
''' 5 4 3 2 1
     4 5 3 2 1
      4 3 5 2 1 
      4 3  5 2 1 

 
 '''
r =[]
a = [1,2,3,3,9,8,11,1005,1.2913,2.91231]
lens = len(a)
for i in range(0,len(a)):
    for j in range(0,lens-1-i) :
        if(a[j]>a[j+1]):
            temp = a[j]
            a[j] = a[j+1]
            a[j+1] =temp

print(a,"sorted")