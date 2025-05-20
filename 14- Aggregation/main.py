class Employee:
    def __init__(self,name):
        self.name = name
class Departure :
    def __init__(self,employee):
        self.employee = employee
    
    def emp_detail(self):
        print(f" Employee in departure: {self.employee.name}" )

if __name__ == "__main__":
    emp = Employee("kashaf")
    dep = Departure(emp)
    dep.emp_detail()
        
        