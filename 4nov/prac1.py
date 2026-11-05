# s ="logo .jpg" name replace with sunset
s= "logo.jpg"
sp = s.split(".")

print(sp)

sp[0] = "sunset"
print(sp)

op = sp[0]+"."+sp[1]
print(op)