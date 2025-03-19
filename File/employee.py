f_name = "employee.text"
def add_employee():
    with open(f_name, 'a') as file:
        emp_id = input("Enter Employee ID: ")
        name = input("Enter Name: ")
        age = input("Enter Age: ")
        department = input("Enter Department: ")
        salary = input("Enter Salary: ")

        file.write(f'\n{emp_id},{name},{age},{department},{salary}')
        print("✅ Employee added successfully!\n")


def view_employees():
    try:
        with open(f_name, 'r') as file:
            employees = file.readlines()

            if not employees:
                print("No employee records found!\n")
                return

            print("\n Employee Records ")
            for emp in employees:
                emp = emp.strip()
                emp_data = emp.split(',')

                if len(emp_data) >= 5:  # Ensure a valid record
                    print(
                        f"ID: {emp_data[0]}, Name: {emp_data[1]}, Age: {emp_data[2]}, Department: {emp_data[3]}, Salary: {emp_data[4]}")
                else:
                    print(f"Invalid record format: {emp}")
            print()

    except FileNotFoundError:
        print("No employee records found! The file does not exist.\n")


# with open(f_name,'w') as file:
#     file.write('emp_id,name,age,department,salary')

while True:
    print("📂 Employee Management System 📂")
    print("1️⃣ Add Employee")
    print("2️⃣ View Employees")
    print("3️⃣ Search Employee")
    print("4️⃣ Update Employee")
    print("5️⃣ Delete Employee")
    print("6️⃣ Exit")

    choice = int(input("Enter your Choice : "))
    if choice == 1:
        add_employee()
    elif choice == 2:
        view_employees()
    # elif choice == 3:
    #     search_employee()
    # elif choice == 4:
    #     update_employee()
    # elif choice == 5:
    #     delete_employee()
    # elif choice == 6:
    #     print("🔴 Exiting Program... Goodbye!")
    #     break
    # else:
    #     print("⚠ Invalid Choice! Please try again.\n")
