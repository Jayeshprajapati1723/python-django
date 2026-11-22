'''#alpha h ya nhi isalpha() to check the stirng contain alphabets or not 
#isupper() : to check format of string
# isnumeric() : string is no or not
# isalnum() : check alpha + numeric string h ya nhi 
# islower : string format is lower or not 
# both all above function return type is boolean either true or false'''
# s = input("enter a stirng to check which funciton related OR format chec k: ")
# t=s
s = input("Enter a string: ")

if s.isalpha():
    if s == s.upper():
        print("Uppercase")
    elif s == s.lower():
        print("Lowercase")
    elif s == s.capitalize():
        print("Capitalized")
    else:
        print("Mixed case")

elif s.isnumeric():
    print("Only numeric")

elif s.isalnum():
    print("Contains alphabets and numbers")

else:
    print("Contains special characters or spaces")
# if(t== (s.capitalize())):
#     print("capitalize ",s)
# elif(t==(s.upper())):
#     print("UPPER",s)
# elif(t==(s.lower())):
#     print("lower",s)        













# s= "jayesh"
# print(s.islower())
# t= "jay123"
# print(t.isalnum()) 
# u = "FORMATE UPPER"
# print(u.isupper())
# v = "1234"
# print(v.isnumeric()) 
