#2. Write a program to enter employee details and also filter the stored employee  details  with name and empid and designation and email. 

# write a python program that allows you to add an employee with domain, name, empid, and email details using user input and then print the employee's details.


employees = {}

def add_employee():
    domain = input("Enter employee domain: ")
    name = input("Enter employee name: ")
    empid = input("Enter employee ID: ")
    email = input("Enter employee email: ")

    employee_details = {
        "Domain": domain,
        "Name": name,
        "Employee ID": empid,
        "Email": email
    }

    employees[empid] = employee_details
    employees[name] = employee_details
    employees[domain] = employee_details
    employees[email] = employee_details

def print_employee_details():

    def serach_by_id():
        empid = input("Enter Employee Id to print Employee Details : ")
        if empid in employees:
            print("Employee Details : ")
            for key, value in employees[empid].items():
                print(f"{key}: {value}")
        else:
            print("Employee not found.")

    def serach_by_name():
        name = input("Enter employee name to print Employee Details : ")
        if name in employees:
            print("Employee Details : ")
            for key, value in employees[name].items():
                print(f"{key}:{value}")
        else:
            print("Employee not found.")

    def serach_by_domain():
        domain = input("Enter employee domain to print Employee Details : ")
        if domain in employees:
            print("Employee Details : ")
            for key, value in employees[domain].items():
                print(f"{key}: {value}")
        else:
            print("Employee not found")

    def search_by_email():
        email = input("Enter Email to print Employee Details : ")
        if email in employees:
            print("Employee Details : ")
            for key, value in employees[email].items():
                print(f"{key}: {value}")
        else:
            print("EMployee not found")

    while True:
        print("Options : ")
        print("1. search by employee id : ")
        print("2. Search by name : ")
        print("3. search by domain : ")
        print("4. search by email id : ")

        choose = input("Enter your choice (1/2/3/4) : ")
        
        if choose == '1':
            serach_by_id()

        elif choose == '2':
            serach_by_name()
        
        elif choose =='3':
            serach_by_domain()
        
        elif choose == '4':
            search_by_email()
         
        else:
            print("Invalid option. ")     
            
      

def view_Employee_detail():
    if((len(employees ))>= 1):
        print(employees)
    else:
        print("No Data in this Dictionary, Please Add Data")

while True:
    print("Options:")
    print("1. Add Employee")
    print("2. Print Employee Details")
    print("3. View")
    print("4. Exit")
    
    choice = input("Enter your choice (1/2/3/4): ")

    if choice == '1':
        add_employee()
    elif choice == '2':
        print_employee_details()
    elif choice == '3':
        view_Employee_detail()
    elif choice == '4':
        break
    else:
        print("Invalid choice. Please try again.")


        
