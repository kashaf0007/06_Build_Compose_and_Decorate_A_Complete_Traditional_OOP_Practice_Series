
# 7. Access Modifiers: Public, Private, and Protected

class Employee:
    def __init__(self,name ,salary,ssn):
     self.name = name
     self.salary =salary
     self.ssn = ssn 

     def display(self):
        print(f"Name: {self.name}")
        print(f"Salary: {self.salary}")
        print(f"SSN: {self.ssn}")

emp = Employee("Kashaf",30000,"763499-34378-42")
print("Public:", emp.name)
print("Protected:", emp.salary)

try:
    print("Private:", emp.__ssn)
except:
    print("Private: Cannot access directly")