# 1.Write a Python script to add a key to a dictionary.
d = {'0': 10, '1': 20}
d['2'] = 30
print(d)

# 2.Write a Python script to check whether a given key already exists in a dictionary.

dic = {"Fruits":"cherry", "cars":"BMW"}
b = "car"
if b in dic.keys():
    print("Present")
else: 
    print("not present")

# 3.Write a Python program to iterate over dictionaries using for loops
dic = {"Laptops":"apple", "cars":"Range Rover","Cloths":"Puma"}  
for key,value in dic.items():
    print(key,value)

# 4.Write a Python script to print a dictionary where the keys are numbers between 1 and 15 (both included) and the values are the square of the keys.Sample Dictionary
d=dict()
for x in range(1,16):
    d[x]=x**2
print(d) 

# 5.Write a Python program to create a dictionary from a string.
str = "marolix Technology"
char = {}
for i in str:
    if i in char:
        char[i] += 1
    else:
        char[i] = 1
print(char)

# 6. Write a Python program to sum all the items in a dictionary.
def reSum(dict):
    sum = 0
    for i in dict:
        sum = sum + dict[i]
    return sum
dict = {'a': 100, 'b': 200, 'c': 300}
print("Sum :", reSum(dict))


# 7.Write a Python program to combine two dictionary by adding values for common keys.
d1 = {'a': 100, 'b': 200, 'c':300}
d2 = {'a': 300, 'b': 200, 'd':400}
d = {k: d1.get(k, 0) + d2.get(k, 0) for k in d1.keys() | d2.keys()}
print(d)


# 8.Write a Python program to access dictionary key's element by index.
Dictionary = {'Physics': 99, 'Maths': 90, 'Chemistry': 96}
print(list(Dictionary)[0])
print(list(Dictionary)[1])
print(list(Dictionary)[2])


# 9.Write a Python program to remove a key from a dictionary.
d = {"Yogi":"jani","Hema":"hasini","Mani":"rasi","Keerthy":"suresh"}
remove_word = d.pop("Mani")
print(remove_word)
print(d)

# 10.Write a Python script to merge two Python dictionaries.d
dict_1 = {"santosh":101,"Hasini":102,"Jani":103,"Rohit":104}
dict_2 = {"Harsha":2001,"Joshith":2002,"yogi":1992}
res = {**dict_1,**dict_2}
print(res)
