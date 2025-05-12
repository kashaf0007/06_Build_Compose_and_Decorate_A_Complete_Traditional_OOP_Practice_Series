# 10. Instance Methods
class dog :
   def __init__(self,name,breed):
      self.name = name
      self.breed = breed
    
   def bark(self):
      print(f"{self.name} is barking! Woof woof!")

my_dog = dog("Dog", "Golden Retriever")
my_dog.bark()
