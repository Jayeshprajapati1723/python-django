'''bitwise operator '''
# & and k liye 
# or k liye ||
# ^ xor
# # ~ not k liye 
# << left shift 
# >> right shift 

a = 4
b = 4 
# and me mutliply  .
# or me add

# same pr zero diffrent pr one 
print(a&b)
print(a|b) 
print(a^b)
print(a+b)

print("left <<",a<<1)
print("left <<",a>>1)

# # assignment operator with bitwisse 
# &= and and assign 
# |= bitwise or and assign
# ^= bitsise xor and assign 
# <<= >>= 

# NOTE :# not aasignment nhi hota h bistwise ~= ye ...xxxx
a= 5
b = 4
a&=b
print(a)
a|=b
print(a)
a^=b 
print(a)

a<<=1
print("left <<",a)

a>>=1
print("left <<",a)