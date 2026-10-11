# Employee Salary System

employees = {
    101: {"name": "Alice", "department": "HR", "salary": 30000},
    102: {"name": "Bob", "department": "IT", "salary": 40000},
    103: {"name": "Charlie", "department": "Finance", "salary": 35000},
    104: {"name": "David", "department": "Marketing", "salary": 32000},
    105: {"name": "Eva", "department": "Sales", "salary": 38000}
}

def calculate_yearly_salary(monthly_salary):
    return monthly_salary * 12

def increase_salary(salary, percent):
    return salary + (salary * percent / 100)

try:
    emp_id = int(input("Enter Employee ID: "))

    if emp_id not in employees:
        raise KeyError

    percent = float(input("Enter salary increase percentage: "))

    employee = employees[emp_id]
    old_salary = employee["salary"]
    new_salary = increase_salary(old_salary, percent)

    print("Old Salary:", old_salary)
    print("New Salary:", new_salary)
    print("Yearly Salary:", calculate_yearly_salary(new_salary))

except KeyError:
    print("Employee ID does not exist.")

except ValueError:
    print("Invalid percentage unit.")
    