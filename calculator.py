class calculator():

   def __init__(self,input_01,input_02):
      self.a=input_01
      self.b=input_02

   def add(self):
      return self.a+self.b
   def multiply(self):
      return self.a*self.b
   def divide(self):
      return self.a/self.b
   def subtract(self):
      return self.a-self.b
   
input_1 = int(input("Enter the first number: "))
input_2 = int(input("Enter the second number: "))
print("The entered first and second numbers are : ")
print(input_1, input_2)

my_instance = calculator(input_1,input_2)
choice=1

while choice!=0:
   print("0. Exit")
   print("1. Addition")
   print("2. Subtraction")
   print("3. Multiplication")
   print("4. Division")
   choice=int(input("Enter your choice... "))

   if choice==1:
      print("The computed addition result is : ",my_instance.add())
   elif choice==2:
      print("The computed subtraction result is : ",my_instance.subtract())
   elif choice==3:
      print("The computed product result is : ",my_instance.multiply())
   elif choice==4:
      print("The computed division result is : ",round(my_instance.divide(),2))
   elif choice==0:
      print("Exit")
   else:
      print("Sorry, invalid choice!")
print()