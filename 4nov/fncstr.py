# to convert any stirng to uppercase 
s = "jay"
print(s.upper())

s = "rAJU"
l = s.lower()
print(l)

s = "capital"
SS=s.capitalize()
print(SS)

ss=s.title()
# capital first letter only
print(ss)

ss=s.swapcase()
print(ss)
# inverts uper to lower and vice vresa 

# remove the extra whitespaces left and right 
data= "         jayesh jprafjofjsf      "
print(data,len(data))
nd=data.strip()
print(nd ,len(nd))

# replace("old string with new string ")
s = "jayesh is good boy"
res = s.replace("good","handsome")
print(res)



# split for split hte string at sspecified positionn syntax 
# return list = strname.split(position)
s = "2026-11-04"
res = s.split("-")
print(type(res))
print(s,res)

d = res[2]+"/"+res[1]+"/"+res[0]
print(d,"new format using split ")