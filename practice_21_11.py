# String Methods :
a = "Hey, This is SanTOsh KuMar "
print(a.lower())
print(a.upper())
print(a.title())
print(a.swapcase())
print(a.capitalize())
print(a.center(10))
print(a.center(100,'#'))
print(a.count('h'))
print(a.endswith(' '))

print(a.rfind('is'))
print(a.rindex('is'))
print(a.find('is'))
print(a.index('is'))

print(a.replace('is','REPLACE METHOD'))

x = "sanotsh8897"
y = "santosh"
z = "8897"
m = " "
print("sanotsh8897",x.isalnum())
print("santosh",y.isalnum())
print("sanotsh",y.isalpha())
print("sanotsh8897",x.isalpha())
print("santosh8997",x.isdigit())
print("santosh",y.isdigit())
print("8897",z.isdigit())
print("8897",z.isalnum())
print("8897",z.isalpha())
print("8897",z.isspace())
print(m.isspace())

str = '_'.join('santosh')
print(str)

list_1 = ['s','a','n','t','o','s','h']
print("".join(list_1))

list_2 = "santosh"
print("$".join(list_2))

list_1 = ['s','a','n','t','o','s','h']
print("&".join(list_1))

dic_1 = {'abc':1,'xyz':2,'pqr':3}
print('**'.join(dic_1))

my_string = "          Hello World             "
s = my_string.strip()
r = my_string.rstrip()
l = my_string.lstrip()
print(s)
print(r)
print(l)




# Reverse list :
list = [1,3,4,8,67,3,9]

a = list[::-1]
print(a)

list.reverse()
print(list)

l =[]
for i in list:
    l.insert(0,i)
print(l)

# reverse integer :
n = 123456

rev = 0
while n != 0:
    rev = rev* 10 + n%10
    n = (n//10)
print(rev)

b = str(n)[::-1]
print(b)

# Armstrong Number:
num = 15388
sum = 0
temp = num
count = len(str(num))
while temp > 0:
    digit = temp % 10
    sum = sum + digit ** count
    temp = temp // 10
if num == sum:
    print("YES")
else:
    print("NO")

# check Prime number :
n = 31
if n > 1:
    for i in range(2,n):
        if (n % i) == 0:
            print("Not a Prime Number")
            break
    else:
        print("Prime Number")
else:
    print("Not a Prime Number")

# Fibonacci Sequence:
c = 5
n1 = 0
n2 = 1
count = 0
if c <= 0:
    print("Enter Positive Numbers")
elif c == 1:
    print(n1)
else:
    while count < c:
        print(n1)
        nth = n1+n2
        n1 = n2
        n2 = nth
        count = count + 1


        

