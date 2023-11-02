# 1.write a python program to merge two lists.
'''lst_1 = eval(input("Enter list one : "))
lst_2 = eval(input("Enter list two : "))
lst_1.extend(lst_2)
print(lst_1)

# 2.write a python program to find the sum of list elements.
ls = eval(input("Enter The list : "))
result = sum(ls)
print(result)

# 3.write a python program to print even and odd numbers seperatly in list.
lst = eval(input("Enter the list : "))
even = []
odd = []
for i in lst:
    if i%2 != 0:
        odd.append(i)
    else:
        even.append(i)
print("odd list : ",odd)
print("even list : ",even)

# 4.write a python program to delete element of given index in list.
l_1 = eval(input("Enter the list : "))
l_1.pop(2)
print(l_1)

# 5.write a python program to delete given elemet from the list 
l1 = eval(input("Enter the list : "))
l1.remove(3)
print(l1)

# 6.write a python program to insert an elemet  at given index location.
l2 = eval(input("Enter the list : "))
l2.insert(5,100)
print(l2)

# 7.write a python program to check the sizes of given two lists are same.
list_1 = eval(input("Enter the list one : "))
list_2 = eval(input("Enter the list two : "))
if len(list_1) == len(list_2):
    print("Yes list one and list two lengths are same")
else:
    print("No list one and list two lengths are not same")

# 8.Write a Python function that takes two lists and returns True if they have at least one common member.
list1 = eval(input("Enter the list one : "))
list2 = eval(input("Enter the list two : "))
for x in list1:
    if x in list2:
        print("letter",x,"is commen letter in both lists")

9.Write a Python program to remove a specified column from a given nested list.
list_one = eval(input("Enter the list one : "))
main_list = []
for i in range(0,len(list_one)):
    result=[]
    for j in range(1,len(list_one)):
        result.append(list_one[i][j])
    main_list.append(result)
print(main_list)

10. Write a Python program to convert a list of multiple integers into a single integer.
list_two = eval(input("Enter the list one : "))
s = ""
for i in list_two:
    s = s+str(i)
print(int(s))

10.Write a Python program to remove duplicates from a list.
list_l = eval(input("Enter the list one : "))
res = []
for i in list_l:
    if i not in res:
        res.append(i)
print(res)
