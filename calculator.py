def add(x,y):
    return x+y

def substration(x,y):
    return x-y

def multiplecation(x,y):
    return x*y

def division(x,y):
    return x/y

print("select operation: ")
print("1.Add")
print("2.Substration")
print("3.Multiplecation")
print("4.Division")

while True:
    choose = input("Select Operation(1/2/3/4): ")
    if choose in ('1','2','3','4'):
        try:
            num1 = float(input("Enter X value : "))
            num2 = float(input("Enter Y value : "))
        
        except ValueError:
            continue

        if choose =='1':
            print(num1, " + ", num2, " = ", add(num1,num2))
        elif choose == '2':
            print(num1, " - ", num2, " = ", substration(num1,num2))
        elif choose == '3':
            print(num1, " * ",num2, " = ", multiplecation(num1,num2))
        elif choose == '4':
            print(num1, " / ", num2, " = ", division(num1,num2))

        
    else:
        print("Invalid Input ")