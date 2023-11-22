# find greatest number:
# n1 = 88
# n2 = 9
# n3 = 10

# if n1 >= n2 and n1>= n3:
#     print(n1," is greatest")
# if n2>=n1 and n2>=n3:
#     print(n2," is greatest")
# if n3>=n1 and n3>=n2:
#     print(n3," is greatest")

# if n1>= n2 and n1>=n3:
#     print(n1," is greatest")
# elif (n2 >= n3 and n2>=n1):
#     print(n2," is greatesh")
# else:
#     print(n3," is greatesh")


# swapping of two numbers :
# a = 100
# b = 200
# c = a
# a = b
# b = c 
# print("value of a is : ", a)
# print("value of b is : ", b)


# swapping of two numbers without using third number
# a = 20
# b = 5
# a=a-b
# b=a+b
# a=b-a
# print("value of a is : ", a)
# print("value of b is : ", b)

# check number is even or odd :
# n = 13
# if n %2 ==0:
#     print(n," is even number")
# else:
#     print(n," is odd number")

# print table:
# n = 13
# for i in range(1,11):
#     print(n,"*",i,"=",n*i)

# print 20 tables :
# for i in range(1,21):
#     print("Print Table number : ",i)
#     for j in range(1,11):
#         print(i,"*",j,"=",i*j)

# print n prime numbers :
# lower = 1
# upper = 99
# for n in range(lower, upper +1):
#     if n > 1:
#         for i in range(2,n):
#             if (n % i)==0:
#                 break
#         else:
#             print(n,end=",")

# n = 9
# count = 0
# for a in range(1,n+1):
#     if a > 1: 
#         for i in range(2,a):
#             if (a % i)==0:
#                 count = count + 1
#                 break
#         else:
#             print(a,end=",")
#             # print(count)
# print("\ntotal prime numbers : ",count)


# remove element from string :
# s = "santoshkumar"
# e = 'k'
# print(s.replace(e,""))

# count occurrence of given character in string:
# s = "abcbcabcabcacbaac"
# c = 'a'
# count = 0
# for i in range(len(s)):
#     if(s[i] == c):
#         count = count +1
# print(count)

# check anagram program :
# def check(s1,s2):
#     if (sorted(s1) == sorted(s2)):
#         print("YES")
#     else:
#         print("NO")
# s1 = "santosh"
# s2 = "toshans"
# check(s1,s2)

# check vowel or consonant :
# a = 'x'
# vowels = ['a','e','i','o','u','A','E','I','O','U']
# if a in vowels:
#     print(a," is Vowel")
# else:
#     print(a," is consonant")

# def vowel(ch):
#     vowels =  ['a','e','i','o','u','A','E','I','O','U']

#     if ch in vowels:
#         print(ch," is vowel")
#     else:
#         print(ch," is consonant")

# ch = 'a'

# vowel(ch)

# digit or not :
# d = '8'
# if (d.isdigit()):
#     print("YES")
# else:
#     print("NO")

# replace with space with given string:
# str = "Hey i am Santosh kumar "
# ch = '@'
# print(str.replace(" ",ch))

# count vowels & consonants :
# st = "Hey i am Santosh kumar  i am learning python "
# vowels = 0
# consonants = 0
# for i in st:
#     if i in ('a', 'e', 'i', 'o', 'u','A', 'E', 'I', 'O', 'U'):
#         vowels = vowels + 1
#     else:
#         consonants = consonants + 1
# print("No of vowels : ",vowels)
# print("No of consonants : ",consonants)

# most occurance element in string :
str = "aaabbbbbbbccccccccccc"
most_coman = max(set(str),key=str.count)
print(most_coman)
print(str.count(most_coman))

# find largest item in list :
# my_list = [15,16,19]
# res = max(my_list)
# print(res)