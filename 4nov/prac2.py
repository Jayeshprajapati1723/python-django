'''join elements of an iterable into a single string ............    
word = ['python", is ,"easy"]

'''
word = ["python","is",'easy']
print('wow'.join(word))
date =['2026',"11","04"]
print("-".join(date))

str = "jayesh ji goodu"
# imutable ==> mutable  join or replace 
a= list(str)
a[0] = "x"
a.insert(0,"j")

print(a)
nw = " ".join(a)
print(nw,"before replace")
ne=nw.replace("x","j")
print(ne,"after replace")
print(nw,type(nw))

# find() method string me se not found ke case me -1
a = "jayesh"
print(a.find("y"))