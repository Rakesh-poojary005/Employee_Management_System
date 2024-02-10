import json

class Employee:
    def __init__(self, name, emp_id, title, department):
        """
        Initialize an Employee object with provided attributes.

        Parameters:
        name (str): The name of the employee.
        emp_id (str): The employee ID.
        title (str): The job title of the employee.
        department (str): The department to which the employee belongs.

        """
        self.name = name
        self.emp_id = emp_id
        self.title = title
        self.department = department

    def display_employee_details(self):
        """
        Display the details of the employee.
        """
        print(f"Name: {self.name}, ID: {self.emp_id}, Title: {self.title}, Department: {self.department}")

    def __str__(self):
        """
        Return a string representation of the employee.
        """
        return f"{self.name} - {self.emp_id}"

class Department:
    def __init__(self, name):
        """
        Initialize a Department object with the provided name.

        Parameters:
        name (str): The name of the department.
        """
        self.name = name
        self.employees = []

    def add_employee(self, employee):
        """
        Add an employee to the department.

        Parameters:
        employee (Employee): The Employee object to be added to the department.
        """
        self.employees.append(employee)

    def remove_employee(self, employee):
        """
        Remove an employee from the department.

        Parameters:
        employee (Employee): The Employee object to be removed from the department.
        """
        if employee in self.employees:
            self.employees.remove(employee)
            print(f"{employee.name} removed from {self.name}")
        else:
            print(f"{employee.name} not found in {self.name}")

    def list_employees(self):
        """
        List all employees in the department.
        """
        print(f"Employees in {self.name}:")
        for emp in self.employees:
            print(emp)

class Company:
    def __init__(self):
        """
        Initialize a Company object with an empty dictionary to store departments.
        """
        self.departments = {}

    def add_department(self, department_name):
        """
        Add a department to the company.

        Parameters:
        department_name (str): The name of the department to be added.
        """
        if department_name not in self.departments:
            self.departments[department_name] = Department(department_name)
            print(f"Department '{department_name}' added.")
        else:
            print("Department already exists.")

    def remove_department(self, department_name):
        """
        Remove a department from the company.

        Parameters:
        department_name (str): The name of the department to be removed.
        """
        if department_name in self.departments:
            del self.departments[department_name]
            print(f"Department '{department_name}' removed.")
        else:
            print("Department does not exist.")

    def display_departments(self):
        """
        Display the names of all departments in the company.
        """
        print("Departments:")
        for dept_name in self.departments:
            print(dept_name)

def save_data(company):
    """
    Save the company data to a JSON file.

    Parameters:
    company (Company): The Company object containing the data to be saved.
    """
    with open('company_data.json', 'w') as file:
        data = {dept.name: [emp.__dict__ for emp in dept.employees] for dept in company.departments.values()}
        json.dump(data, file, indent=4)

def load_data():
    """
    Load company data from a JSON file.

    Returns:
    company (Company): The Company object containing the loaded data, or a new Company object if the file is not found.
    """
    try:
        with open('company_data.json', 'r') as file:
            # Load data from the JSON file
            data = json.load(file)
            company = Company()
            for dept_name, employees in data.items():
                department = Department(dept_name)
                for emp_data in employees:
                    employee = Employee(emp_data['name'], emp_data['emp_id'], emp_data['title'], dept_name)
                    department.add_employee(employee)
                company.departments[dept_name] = department
            return company
    except FileNotFoundError:
        return Company()

def menu():
    print("\nEmployee Management System Menu:")
    print("1. Add Department")
    print("2. Remove Department")
    print("3. Add Employee")
    print("4. Remove Employee")
    print("5. List Employees in Department")
    print("6. Display Departments")
    print("7. Save Data")
    print("8. Exit")

def main():
    company = load_data()

    while True:
        menu()
        choice = input("Enter your choice: ")

        if choice == '1':
            department_name = input("Enter department name: ")
            company.add_department(department_name)
        elif choice == '2':
            department_name = input("Enter department name: ")
            company.remove_department(department_name)
        elif choice == '3':
            department_name = input("Enter department name: ")
            if department_name in company.departments:
                name = input("Enter employee name: ")
                emp_id = input("Enter employee ID: ")
                title = input("Enter employee title: ")
                employee = Employee(name, emp_id, title, department_name)
                company.departments[department_name].add_employee(employee)
            else:
                print("Department not found.")
        elif choice == '4':
            department_name = input("Enter department name: ")
            if department_name in company.departments:
                employee_id = input("Enter employee ID: ")
                for emp in company.departments[department_name].employees:
                    if emp.emp_id == employee_id:
                        company.departments[department_name].remove_employee(emp)
                        break
                else:
                    print("Employee not found.")
            else:
                print("Department not found.")
        elif choice == '5':
            department_name = input("Enter department name: ")
            if department_name in company.departments:
                company.departments[department_name].list_employees()
            else:
                print("Department not found.")
        elif choice == '6':
            company.display_departments()
        elif choice == '7':
            save_data(company)
            print("Data saved.")
        elif choice == '8':
            save_data(company)
            print("Exiting program.")
            break
        else:
            print("Invalid choice. Please enter a number between 1 and 8.")

if __name__ == "__main__":
    main()
