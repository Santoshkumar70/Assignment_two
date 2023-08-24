# 1.Write a python program to remove a given  character from string.

str_1 = input("Enter string : ")
remove_word = input("Enter Removing Character : ")
print(str_1.replace(remove_word,""))

# 2.Write a program to check String is Palindrome or not.

Palindrome_string = input("Enter Palindrome String : ")
Empty_string = ""
for i in Palindrome_string:
    Empty_string = i+Empty_string
if(Palindrome_string == Empty_string):
    print("Yes, Given string is Palindrome")
else:
    print("No, Given string is not a palindrome")

# 3.Write a python program to check given character is vowel or consonant.

vowel_list = ['a','e','i','o','u','A','E','I','O','U']
Char = input("Enter Character : ")
if Char in vowel_list:
    print( Char," is vowel")
else:
    print(Char," is consonant")

# 4.Write a python program to replace string space with given character in Python.

p = input("Enter String : ")
Character = input("Enter Replace Character : ")
print(p.replace(" ",Character))

# 5.Write a python program to count alphabets, digits, and special characters in the string.

String_1 = input("Enter String : ")
alphabets = digits = special_charcters = 0

for i in range(len(String_1)):
    if(String_1[i].isalpha()):
        alphabets = alphabets +1
    elif(String_1[i].isdigit()):
        digits = digits +1
    else:
        special_charcters = special_charcters +1
print("Total Number of Alphabets : ",alphabets)
print("Total Number of Digits : ",digits)
print("Total Number of Special Characters : ",special_charcters)


# 6.Write a python program to remove all the blank spaces in a given string.

str_one = input("Enter string : ")
print(str_one.replace(" ",""))


# 7.Write a python program to find sum of integers in the string.

string1 = input("enter string : ")
sum = 0
for i in string1:
    if(i.isdigit()):
        sum = sum + int(i)
print(sum)

# 8.Write a python program to Remove Repeated Character from String.

st = input("Enter String : ")
ept = ""
for i in st:
    if i not in ept:
        ept = ept + i
print(ept)

# 9.Write a python program to count occurrence of given character in string. 

x = input("Enter string : ")
chr = input("Enter Character : ")
count = 0
for i in x:
    if(i == chr):
        count = count + 1
print(count)



# 10.Write a python program to check string is anagrams or not in Python.

s1 = input("Enter String 1 : ")
s2 = input("Enter String 2 : ")

s3=sorted(s1.lower())
s4=sorted(s2.lower())

if(s3 == s4):
    print("given string is Anagram")
else:
    print("given string is not a anagram")

    
