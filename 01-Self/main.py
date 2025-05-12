# 1. Using self

class student:
    def __init__(self,name,mark):
       self.name = name
       self.mark = mark 
    def display(self):
        print(f"Student Name: {self.name}")
        print(f"Marks: {self.marks}")                      

students = student("Kashaf Aman" , 86)
students.display()   