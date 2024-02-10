import unittest
from employee_oops import Employee, Department, Company

class TestEmployeeManagementSystem(unittest.TestCase):

    def test_add_department(self):
        company = Company()
        company.add_department("HR")
        self.assertIn("HR", company.departments)
        print("test added department!!")

    def test_remove_department(self):
        company = Company()
        company.add_department("HR")
        company.remove_department("HR")
        self.assertNotIn("HR", company.departments)
        print("test removed department!!")

    def test_add_employee(self):
        company = Company()
        company.add_department("HR")
        employee = Employee("Rakesh", "001", "Manager", "HR")
        company.departments["HR"].add_employee(employee)
        self.assertIn(employee, company.departments["HR"].employees)
        print("test added employee!!")

    def test_remove_employee(self):
        company = Company()
        company.add_department("HR")
        employee = Employee("Rakesh", "001", "Manager", "HR")
        company.departments["HR"].add_employee(employee)
        company.departments["HR"].remove_employee(employee)
        self.assertNotIn(employee, company.departments["HR"].employees)
        print("test removed employee!!")

if __name__ == '__main__':
    unittest.main()
