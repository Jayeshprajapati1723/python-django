# numeridal stirg is compatible full stirng is not compatible 
num = "45" 
print(int(num)) 
# num = "12abc"
# print(int(num))

# assignment operator
a=5 
b= 6
c = 7
d = 8
e = 9
f = 10
g = 11
a -= 5 
print(a) 
b += 5
print(b) 
c *= 5 
print(c) 
d /= 5 
print(d) 
e //= 5
print(e) 
f %= 5
print(f) 
g **= 5 
print(g) 

num =int(input("enter a no" )) 
f=num%10 
s = num//10
rev = (f*10)+s 
print(rev)

# average of three integer number 

num1 = 5
num2 =7 
num3 =11
n= 3
sum = num1 + num2 +num3
avg = sum/n 
print("average is ",avg )


# total and percentage 5 subject marks 
m1 = 100 
m2 = 100 
m3 = 100 
m4 = 100 
m5 = 100 
n= 5 
sumMARKS = m1+m2+m3+m4+m5
percentage = sum/n
print("TOTAL MARKS = ",sumMARKS)