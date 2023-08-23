#meber ship Operator:
print("Member Ship operator : ")
a="Hey, Hello Santosh please do learn python bocz it's easy language"
print("Hey" in a)
print("Hi" in a)
print("Bye" not in a)


# Removing Spaces from String 
print("    ")
print("Removing Spaces :")
string ="       Hey, Hello Santosh please do learn python bocz it's easy language     "
c=string.strip()
d=string.rstrip()   # Remove Right spaces
e=string.lstrip()   # Remove left Spaces 
print(len(string), string)
print(len(c),c)
print(len(d),d)
print(len(e),e)

#comparing string:
print("    ")
print("Comparing String :")
str_1 ="Hey, Hello"
str_2 ="Good Morning"
str_3 ="Good Morning"
print(str_1 == str_2)
print(str_2 == str_3)


#find substring index:
print("    ")
print("Find Substring :")
main_string = "Hey, Hello Santosh please do learn python bocz it's easy language"
sub_string = "Santosh"
print(main_string.find(sub_string))

#Replace Funcation :
print("    ")
print("Replace Function :")
z="Good Morning Guys"
print(z.replace("Morning","Evening"))



#Split Function :
print("    ")
print("Split Function :")
y = "Hey, Hello Santosh please do learn python bocz it's easy language"
print(y.split())



#join Function :
print("    ")
print("join Function :")
x = "Hey, Hello Santosh please do learn python bocz it's easy language"
print("-".join(x))
print("-".join(x.split()))