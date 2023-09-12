# 1. Find Power Value : 

def power(num, topwr):
    if topwr == 0:
        return 1
    else:
        return num * power(num, topwr - 1)

a = int(input("Enter base value : "))
b= int(input("Enter Power value : "))
print("4 power of 7 value is : ",power(a,b)) 


# 2. Fibonacci Sequence : 

def fibonacci(n):
    if n <= 1:
        return n
    else:
        return fibonacci(n - 1) + fibonacci(n - 2)
    
number = int(input("Enter Number : "))
print('Fibonacci sequence:')
for i in range(number):
    print(fibonacci(i))

# 3. 
def sumnums(n):
    if n == 1:
        return 1
    return n + sumnums(n - 1)

x = int(input("Enter Number : "))
print("sum of ",x," : ",sumnums(x))

# 4. 
def reverse(string):
    if len(string) == 0:
        return string
    else:
        return reverse(string[1:]) + string[0]

reverseme = input("Enter String : ")
print(reverse(reverseme))
