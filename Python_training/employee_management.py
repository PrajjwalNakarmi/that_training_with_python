import json
import os


json_file='employee_data'

def user_choice():
    while True:
        print("Employee Detail")
        print("1. Add Employee")
        print("2. Edit Employee")
        print("3. Delete Employee")
        print("4. Read Employee")
        print("5. Exit")

        user_choice=int(input("Chose an Opetion:"))
        if user_choice==1:
            add_employees()
        elif user_choice==2:
            edit_employees()
        elif user_choice==3:
            delete_employee()
        elif user_choice==4:
            read_employee_detail()
        elif user_choice==5:
            print("Exiting the Program")
            break
        else:
            print("Invalid Input. Try again.")

def employee_file():
    def employee_file():
        if not os.path.exists(json_file):
            with open(json_file, "w") as file:
                json.dump([], file)

    try:
        with open(json_file, "r") as file:
            data = json.load(file)
        # Convert `employee_id` to an integer for all employees
        for employee in data:
            if "employee_id" in employee:
                employee["employee_id"] = int(employee["employee_id"])
        return data
    except json.JSONDecodeError:
        with open(json_file, "w") as file:
            json.dump([], file)
        return []

def save_employees(employee_detail):
    for employee in employee_detail:
        employee["employee_id"] = int(employee["employee_id"])  # Ensure `employee_id` is an integer
    with open(json_file, "w") as file:
        json.dump(employee_detail, file, indent=2)

def add_employees():
    employee_detail=employee_file()



    while True:
        try:
            employee_id = int(input("Enter a unique employee ID: "))
            if any(int(emp['employee_id']) == employee_id for emp in employee_detail):
                print("Employee ID already exists. Please enter a unique ID.")
            else:
                break
        except ValueError:
            print("Invalid input. Employee ID must be a number.")

    while True:
        name = input("Enter the employee name: ").strip()
        if name:
            break
        print("Name cannot be empty. Please enter a valid name.")
    
    while True:
        designation = input("Enter the employee designation: ").strip()
        if designation:
            break
        print("Designation cannot be empty. Please enter a valid designation.")

    while True:
        company_email = input("Enter the employee email: ").strip()
        if "@" in company_email and "." in company_email:
            break
        print("Invalid email. Please enter a valid email address.")

    while True:
        contact = input("Enter the employee contact number: ").strip()
        if contact.isdigit() and len(contact) >= 10:
            break
        print("Invalid contact number. Please enter a numeric value with at least 10 digits.")


    employee = {
        "employee_id": employee_id,
        "name": name,
        "designation": designation,
        "company_mail": company_email,
        "contact": contact
    }
    employee_detail.append(employee)
    save_employees(employee_detail)
    print("Added successfully!!")


def edit_employees():
    employee_detail = employee_file()

    while True:
        try:
            employee_id = int(input("Enter the employee ID to edit: "))
            employee = next((e for e in employee_detail if e["employee_id"] == employee_id), None)
            if employee:
                break
            print("Employee with this ID does not exist. Please try again.")
        except ValueError:
            print("Invalid input. Employee ID must be a number.")

    print("Leave a field blank to keep it unchanged.")
    
    name = input(f"Enter the new name (current: {employee['name']}): ").strip()
    if name:
        employee["name"] = name

    designation = input(f"Enter the new designation (current: {employee['designation']}): ").strip()
    if designation:
        employee["designation"] = designation

    while True:
        company_email = input(f"Enter the new email (current: {employee['company_mail']}): ").strip()
        if not company_email:
            break
        if "@" in company_email and "." in company_email:
            employee["company_mail"] = company_email
            break
        print("Invalid email. Please enter a valid email address.")

    while True:
        contact = input(f"Enter the new contact number (current: {employee['contact']}): ").strip()
        if not contact:
            break
        if contact.isdigit() and len(contact) >= 10:
            employee["contact"] = contact
            break
        print("Invalid contact number. Please enter a numeric value with at least 10 digits.")

    save_employees(employee_detail)
    print("Employee updated successfully!")


def delete_employee():
    employee_detail = employee_file()
    while True:
        try:
            employee_id = int(input("Enter the employee ID to delete: "))
            employee = next((e for e in employee_detail if e["employee_id"] == employee_id), None)
            if employee:
                break
            print("Employee with this ID does not exist. Please try again.")
        except ValueError:
            print("Invalid input. Employee ID must be a number.")

    confirm = input(f"Are you sure you want to delete employee '{employee['name']}'? (yes/no): ").strip().lower()
    if confirm == "yes":
        employee_detail.remove(employee)
        save_employees(employee_detail)
        print("Employee deleted successfully!")
    else:
        print("Deletion canceled.")
        return

def read_employee_detail():
    employee_detail=employee_file()
    print("\nEmployee Details:")
    for employee in employee_detail:
        print(f"Employee ID: {employee['employee_id']}")
        print(f"  Name: {employee['name']}")
        print(f"  Designation: {employee['designation']}")
        print(f"  Company Email: {employee['company_mail']}")
        print(f"  Contact: {employee['contact']}")
        print()
    print("Read operation completed successfully!")

user_choice()