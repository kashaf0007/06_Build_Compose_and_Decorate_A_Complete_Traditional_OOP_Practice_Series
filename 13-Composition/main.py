class Engine :
    def start(self):
        print("Engine has started")
    
class Car:
    def __init__(self,engine):
        self.engine = engine

    def car_started(self):
        self.engine.start()

if __name__ == "__main__":
    engine = Engine()
    my_car = Car(engine)
    my_car.car_started()
        