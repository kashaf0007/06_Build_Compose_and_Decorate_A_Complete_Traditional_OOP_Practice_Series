class person :
   def __init__(self,name):
      self.name = name 

class teacher(person) :
   def __init__(self ,name ,subject):
       super().__init__(name)
       self.subject = subject

   def display(self):
     print(f"Name: {self.name}")
     print(f"Subject: {self.subject}")


t1 = teacher("Mr. Ali", "physics")
t1.display()
