# write a python program that allows you to add an employee with domain, name, empid, and email details using user input and then print the employee's details.
'''
id = eval("Enter Employee Id : ")
if( id== True):
    print("Employee already exists")
     
else:
    name = eval("Enter Employee Name : ")
    designation = eval("Enter Employee Post : ")
    salary = eval("Enter Employee Salary : ")
    Data = {ID:id,NAME:name,Designation:designation,Salary:salary}



    print(Data)

'''

# Create an empty dictionary to store employee details
employees = {}

# Function to add an employee
def add_employee():
    domain = input("Enter employee domain: ")
    name = input("Enter employee name: ")
    empid = input("Enter employee ID: ")
    email = input("Enter employee email: ")

    # Create a dictionary to store employee details
    employee_details = {
        "Domain": domain,
        "Name": name,
        "Employee ID": empid,
        "Email": email
    }

    # Add employee details to the employees dictionary
    employees[empid] = employee_details

# Function to print employee details
def print_employee_details():
    empid = input("Enter Employee ID to print details: ")
    if empid in employees:
        print("Employee Details:")
        for key, value in employees[empid].items():
            print(f"{key}: {value}")
    else:
        print("Employee not found.")

# Main program loop
while True:
    print("Options:")
    print("1. Add Employee")
    print("2. Print Employee Details")
    print("3. Exit")
    
    choice = input("Enter your choice (1/2/3): ")

    if choice == '1':
        add_employee()
    elif choice == '2':
        print_employee_details()
    elif choice == '3':
        break
    else:
        print("Invalid choice. Please try again.")
