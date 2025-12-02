class Employee:
    status = "Active"
    number_of_employees = 0

    def __init__(self, employee_id, name):
        self.employee_id = employee_id
        self.name = name
        Employee.number_of_employees += 1

    def give_info(self):
        print(f" Employee ID :- {self.employee_id} | Name :- {self.name}")


e1 = Employee("1","Gokul")
e1.give_info()