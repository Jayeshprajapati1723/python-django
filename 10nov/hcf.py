num = [2,4,6]

'''
2 = 2x1
4 = 2 x 2
6 = 2 x 3

'''
hcf =[]
end=max(num)
for n in num :
    factors = []
    for i in range(2,end+1):
        while(n%i==0):
            n=n//i
            factors.append(i)
    hcf.append(factors)        

print(hcf)
