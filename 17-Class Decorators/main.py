def add_greeting (cls):
    def greet(self):
        return "Hello!"
    cls.greet = greet
    return cls
@add_greeting
class Person:
    def __init__(self,name):
     self.name = name
p = Person('kashaf')
print(p.greet())