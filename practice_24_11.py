
# add a key to a dictionary.:
dct = {'0':"santosh",'1':"Meena Rao",'2':"vasu"}
dct['3'] = "Naveen"
print(dct)


# given key already exists in a dictionary.
dict={'1':"BMW",'2':"SCORPIO",'3':"AUDI"}
c = 'BMW'
if c in dict.values():
    print("YES")
else:
    print("NO")

# iterate over dictionaries
dic = {"Laptops":"apple", "cars":"Range Rover","Cloths":"Puma"}  
for key,value in dic.items():
    print(key,value)

# numbers between 1 and 15 (both included) and the values are the square of the keys
d=dict()
for x in range(1,16):
    d[x]=x**2
print(d)


# create a dictionary from a string.
str = "santosh kumar"
char = {}
for i in str:
    if i in char:
        char[i] = 1
    else:
        char[i] = 1
print(char)

 # sum all the items in a dictionary.
def reSum(dict):
    sum = 0
    for i in dict:
        sum = sum + dict[i]
    return sum
dict = {'a': 100, 'b': 200, 'c': 300}
print("Sum :", reSum(dict))


 # combine two dictionary by adding values for common keys.
d1 = {'a': 100, 'b': 200, 'c':300}
d2 = {'a': 300, 'b': 200, 'd':400}
d = {k: d1.get(k, 0) + d2.get(k, 0) for k in d1.keys() | d2.keys()}
print(d)

# dictionary key's element by index.
Dictionary = {'Physics': 99, 'Maths': 90, 'Chemistry': 96}
print(list(Dictionary)[0])
print(list(Dictionary)[1])
print(list(Dictionary)[2])

# remove a key from a dictionary.
d = {"Yogi":"jani","Hema":"hasini","Mani":"rasi","Keerthy":"suresh"}
remove_word = d.pop("Mani")
print(remove_word)
print(d)

# merge two Python dictionaries.
dict_1 = {"santosh":101,"Hasini":102,"Jani":103,"Rohit":104}
dict_2 = {"Harsha":2001,"Joshith":2002,"yogi":1992}
res = {**dict_1,**dict_2}
print(res)

# Adding two lists :
numbers1 = [1, 2, 3]
numbers2 = [4, 5, 6]

result = map(lambda x, y: x + y, numbers1, numbers2)
print(list(result)) 

# create nested list :
l = ['sat', 'bat', 'cat', 'mat']

test = list(map(list, l))
print(test)

#  double even number:
def double_even(num):
	if num % 2 == 0:
		return num * 2
	else:
		return num

numbers = [1, 2, 3, 4, 5]
result = list(map(double_even, numbers))
print(result)


