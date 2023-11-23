# Replace first occurrence of Vowel with ‘-‘ in String
st = "Hy gaoogle"
vowels = "aeiouAEIOU"
for i in st:
    if i in vowels:
        st=st.replace(i,"_")
        break
print(st)

# count alphabets & digits & special characters :
st = "Hi @ santoshkumar & my mobile is : 8897445420"
alpha = 0
digits = 0
spcl_char = 0
for i in st:
    if i.isalpha():
        alpha+= 1
    elif i.isdigit():
        digits += 1
    else:
        spcl_char +=1
print("alphanets : ",alpha)
print("numbers : ",digits)
print("special_characters : ",spcl_char)

# remove blankspace :
st = "Hi @ santoshkumar & my mobile is : 8897445420"
print(st.replace(" ",""))

print("".join(st.split()))

def remove(str):
    ns = ""
    for i in str:
        if(not i.isspace()):
            ns +=i
    return ns
st = "Hi @ santoshkumar & my mobile is : 8897445420"
print(remove(st))

# remove repeated characters from string:
st = "Hi @ santoshkumar & my mobile is : 8897445420"
emp = ""  
for i in st:
    if i not in emp:
        emp = emp + i
print(emp)

# most occurance of element in list :
list = [1,2,3,4,5,6,7,8,5,3,2,3,1,2,3,4,1,1,1,1,1,1,1,1]
print(max(list,key=list.count))

# find sum of integers in string :
st = "santosh88974454"
sum = 0
for i in st:
    if i.isdigit():
        sum = sum + int(i)
print(sum)

# print & count non repeating characters :
st = "santosh"
count = 0
b = list(dict.fromkeys(st))
print("".join(b))
print(len(b))

# Acending decending order string 
s = "santosh"
res = ''.join(sorted(s))
print("Acending : ",res)
print("Decending : ",res[::-1])

lst = list(s)
lst.sort()
print(''.join(lst))

# convert lower case to upper case :
st = "Hi This is santosh Kumar"
vowels = "aeiouAEIOU"
for i in st:
    if i in vowels:
        upper = i.upper()
        st = st.replace(i ,upper)
print(st)


# calculate qube of number:
num = 13
print(num * num * num)

# print table using for loop & while loop :
n = 17
for i in range(1,11):
    print(n,"*",i,"=",n*i)

num = 19
count = 1
while count <=10:
    num = num* 1
    print(num,"*",count,"=",num*count)
    count = count+ 1

# conditional statements:
marks =99

if marks > 85 and marks <101:
    print("is got a",marks," and his grade is A")
elif marks > 64 and marks < 85:
    print("is got a",marks," and his grade is B")
elif marks > 39 and marks < 65:
    print("is got a",marks," and his grade is C")
elif marks > 27 and marks < 40:
    print("is got a",marks," and his grade is D")
elif marks >= 0 and marks <28:
    print("is got a",marks," So his Faild")
else:
    print("Your are entered Worng Marks")

# logiacal operator :
# AND :
a = 94
print(a<12 and a>5)
print(a<100 and a>5)
print(a<10 and a>500)

# OR :
print(a>99 or a<99 )
print(a<100 and a>5)
print(a<1 and a>5)

# Relational operatror :
x=10
y=20
print(x<y)
print(x>y)
print(x<=y)
print(x>=y)
print(x == y)
print(x != y)


# member ship operator :
a="Hey, Hello Santosh please do learn python bocz it's easy language"
print("Hey" in a)
print("Hi" in a)
print("Bye" not in a)

# find substring :
main_string = "Hey, Hello Santosh please do learn python bocz it's easy language"
sub_string = "Santosh"
print(main_string.find(sub_string))
print(sub_string in main_string)
print(main_string.index(sub_string))

# split function :
y = "Hey, Hello Santosh please do learn python bocz it's easy language"
print(y.split())

# merge two lists :
lst1 = [1,2,4,5,6,7,89,99,1,5,6,7,2,1,1,1,1,1,1]
lst2 = [00,12,11,13,10,9,8,7,5]
lst1.extend(lst2)
print(lst1)

res = sum(lst1)
print(res)

a = lst1.pop(1)
print(a)
print(lst1)

lst1.remove(1)
print(lst1)

lst2.insert(5,100)
print(lst2)

# remove duplicates from list :
empt = []
for i in lst1:
    if i not in empt:
        empt.append(i)
print(lst1)
print(empt)


# multiple to single integer :
s = ""
for i in lst1:
    s = s+str(i)
print(int(s))