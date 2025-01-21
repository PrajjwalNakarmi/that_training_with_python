import json
import os


json_file='employee_data'

def user_choice():
    while True:
        print("Employee Detail")
        print("1. Add Employees")
        print("2. Edit Employees")
        print("3. Delete Employees")
        print("4. Read Employees")
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
    if not os.path.exists(json_file):
        file=open(json_file,"w")
        json.dump([], file) 
    
    try:
        file=open(json_file,"r")
        return json.load(file)
    except json.JSONDecodeError:
        
        file=open(json_file,"w")
        json.dump([], file)
        return []


def save_employees(employee_detail):
    file= open(json_file,"w")
    json.dump(employee_detail, file, indent=2)

def add_employees():
    employee_detail=employee_file()

    name=input("Enter the employee name:")
    designation=input("Enter the employee designation:")
    company_email=input("Enter the employee email:")
    contact=input("Enter the employee contact:")

    employee = {
        "name": name,
        "designation": designation,
        "company_mail": company_email,
        "contact": contact
    }
    employee_detail.append(employee)
    save_employees(employee_detail)
    print("Added successfully!!")


def edit_employees():
    employee_detail=employee_file()
    #Starts From 0 so if u want to accsess first employee give id=0
    employee_id=int(input("Enter the employee ID ").format(len(employee_detail)-1))
    if employee_id<0 or employee_id>=len(employee_detail):
        print("Invalid Input")
        return
    print("Editing employee:", employee_detail[employee_id])
    name = input("Enter new name (leave blank to keep current): ")
    designation = input("Enter new designation (leave blank to keep current): ")
    company_email = input("Enter new company email (leave blank to keep current): ")
    contact = input("Enter new contact number (leave blank to keep current): ")


    if name:
        employee_detail[employee_id]['name'] = name
    if designation:
        employee_id[employee_id]['designation'] = designation
    if company_email:
        employee_id[employee_id]['company_email'] = company_email
    if contact:
        employee_id[employee_id]['contact'] = contact

    save_employees(employee_detail)
    print("Edited successfully!!")

def delete_employee():
    employee_detail=employee_file()
    #Starts From 0 so if u want to accsess first employee give id=0
    employee_id=int(input("Enter the employee ID to be edited ").format(len(employee_detail)-1))
    if employee_id<0 or employee_id>=len(employee_detail):
        print("Invalid Input")
        return
    employee_detail.pop(employee_id)
    save_employees(employee_detail)
    print("Deleted successfully.")

def read_employee_detail():
    employee_detail=employee_file()
    print("Employee Details:")
    for i, employee in enumerate(employee_detail, start=1):
        print(f"Employee {i}:")
        print(f"  Name: {employee['name']}")
        print(f"  Designation: {employee['designation']}")
        print(f"  Company Email: {employee['company_mail']}")
        print(f"  Contact: {employee['contact']}")
        print()
    print("Read has been done Successfully!!")

user_choice()