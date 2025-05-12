# 3. Public Variables and Methods
class car:
    def __init__(self,brand):
        self.brand = brand
    def start(self):
      print(f"The {self.brand} car in starting...")
my_car = car("Totyota")
print("brand:", my_car.brand)

my_car.start()