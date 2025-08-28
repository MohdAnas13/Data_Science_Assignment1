# -------------------------------
# Employee Management System (EMS)
# -------------------------------

# Step 1 - Initialize dictionary with some sample employee data
employees = {
    101: {'name': 'Basidh', 'age': 27, 'department': 'HR', 'salary': 50000},
    102: {'name': 'Anas', 'age': 22, 'department': 'IT', 'salary': 60000},
    103: {'name': 'Ashiq', 'age': 25, 'department': 'Finance', 'salary': 55000}
}

# Step 3 - Add Employee Function
def add_employee():
    try:
        emp_id = int(input("Enter Employee ID: "))
        if emp_id in employees:
            print(" Employee ID already exists! Try a different ID.")
            return

        name = input("Enter Employee Name: ")
        age = int(input("Enter Employee Age: "))
        department = input("Enter Employee Department: ")
        salary = float(input("Enter Employee Salary: "))

        employees[emp_id] = {
            'name': name,
            'age': age,
            'department': department,
            'salary': salary
        }
        print(" Employee added successfully!")
    except ValueError:
        print(" Invalid input! Please enter correct values.")


# Step 4 - View All Employees
def view_employees():
    if not employees:
        print("⚠ No employees available.")
        return
    
    print("\n--- Employee List ---")
    print(f"{'ID':<5} {'Name':<15} {'Age':<5} {'Department':<15} {'Salary':<10}")
    print("-" * 55)
    for emp_id, details in employees.items():
        print(f"{emp_id:<5} {details['name']:<15} {details['age']:<5} "
              f"{details['department']:<15} {details['salary']:<10}")
    print("-" * 55)


# Step 5 - Search for Employee by ID
def search_employee():
    try:
        emp_id = int(input("Enter Employee ID to search: "))
        if emp_id in employees:
            details = employees[emp_id]
            print("\n Employee Found:")
            print(f"ID: {emp_id}")
            print(f"Name: {details['name']}")
            print(f"Age: {details['age']}")
            print(f"Department: {details['department']}")
            print(f"Salary: {details['salary']}")
        else:
            print(" Employee not found.")
    except ValueError:
        print(" Invalid input! Employee ID should be a number.")


# Step 2 & 6 - Main Menu System
def main_menu():
    while True:
        print("\n--- Employee Management System ---")
        print("1. Add Employee")
        print("2. View All Employees")
        print("3. Search Employee")
        print("4. Exit")

        choice = input("Enter your choice: ")

        if choice == '1':
            add_employee()
        elif choice == '2':
            view_employees()
        elif choice == '3':
            search_employee()
        elif choice == '4':
            print(" Thank you for using the EMS. Exiting now...")
            break
        else:
            print(" Invalid choice! Please select a valid option.")


# Run the program
if __name__ == "__main__":
    main_menu()
