# 1. Adding Two Lists :

numbers1 = [1, 2, 3]
numbers2 = [4, 5, 6]

result = map(lambda x, y: x + y, numbers1, numbers2)
print(list(result)) 

# 2. 
l = ['sat', 'bat', 'cat', 'mat']

test = list(map(list, l))
print(test)

# 3. 
def double_even(num):
	if num % 2 == 0:
		return num * 2
	else:
		return num

numbers = [1, 2, 3, 4, 5]
result = list(map(double_even, numbers))
print(result) # [1, 4, 3, 8, 5]

