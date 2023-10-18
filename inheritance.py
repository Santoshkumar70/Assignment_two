# Single Inheritance:

class company:
    def companyname(self):
        print("Marolix")

class Employee(company):
    def display(self):
        # self.companyname()
        print("Santosh Kumar")
        
e = Employee()
e.companyname()
e.display()

# Multiple Inheritance :
class company1:
    def companyname1(self):
        print("Marolix")

class company2:
    def companyname2(self):
        print("TCS")

class Employee(company1,company2):
    def method2(self):
        self.companyname1()
        self.companyname2()
        print("Santosh Kumar")

e = Employee()
e.method2()

# Multileve Inheritance:
class grandfather:
    def land(self):
        print("50 Acrs Land")

class father(grandfather):
    def money(self):
        self.land()
        print("1000000 rupees ")

class son(father):
    def car(self):
        self.money()
        print("ferari car")
s = son()
s.car()

# Hirechal Inheritance :
class company:
    def companyname(self):
        print("Marolix")

class Employee1(company):
    def emp1(self):
        # self.companyname()
        print("Santosh Kumar")

class Employee2(company):
    def emp2(self):
        # self.companyname()
        print("Meena Rao")

e1=Employee1()
e1.companyname()
e1.emp1()
e2=Employee2()
e2.emp2()

