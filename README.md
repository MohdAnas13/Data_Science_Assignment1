Employee Management System (EMS)
🎯 Objective

The goal of this project is to create a simplified Employee Management System (EMS) using Python.
This project demonstrates the use of:

Control structures (if-else, loops)

Functions for modular design

Dictionary data structures for storing employee data

Basic object-oriented concepts in a structured program

🛠 Steps to Implement
Step 1 – Data Storage

Used a dictionary to store employee data.

The key is the emp_id (Employee ID).

The value is another dictionary containing:

name: Employee’s name

age: Employee’s age

department: Employee’s department

salary: Employee’s monthly salary

✅ Example:

employees = {
    101: {'name': 'Basidh', 'age': 27, 'department': 'HR', 'salary': 50000},
    102: {'name': 'Anas', 'age': 22, 'department': 'IT', 'salary': 60000},
    103: {'name': 'Ashiq', 'age': 25, 'department': 'Finance', 'salary': 55000}
}

Step 2 – Menu System

A menu is displayed continuously until the user chooses Exit. Options include:

Add Employee

View All Employees

Search Employee

Exit

Step 3 – Add Employee

Prompts the user for Employee ID, Name, Age, Department, and Salary.

Validates if the Employee ID is unique.

Stores the data in the dictionary.

Step 4 – View All Employees

Displays all employees in a table-like format.

If no employees exist, it shows "No employees available.".

Step 5 – Search Employee by ID

Prompts the user for an Employee ID.

If the ID exists, displays full details.

Otherwise, shows "Employee not found.".

Step 6 – Exit

Provides an Exit option in the menu.

Displays a thank-you message before ending the program.

📂 Project Code Structure

main_menu() → Displays the menu & calls functions

add_employee() → Adds a new employee

view_employees() → Displays all employees

search_employee() → Searches employee by ID

▶️ How to Run

Save the project file as ems.py.

Open a terminal/command prompt.

Run the script:

python ems.py


Follow the on-screen menu instructions.

✅ Sample Output
--- Employee Management System ---
1. Add Employee
2. View All Employees
3. Search Employee
4. Exit
Enter your choice: 2

--- Employee List ---
ID    Name            Age   Department      Salary    
-------------------------------------------------------
101   Basidh          27    HR              50000.0
102   Anas            22    IT              60000.0
103   Ashiq           25    Finance         55000.0
-------------------------------------------------------
