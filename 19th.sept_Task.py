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

def print_employee_details():
    empid = input("Enter Employee ID to print details: ")
    if empid in employees:
        print("Employee Details:")
        for key, value in employees[empid].items():
            print(f"{key}: {value}")
    else:
        print("Employee not found.")

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
