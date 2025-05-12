
# 2. Using 
class counter:
    count = 0

    def __init__(self):
        counter.count += 1
    
    @classmethod
    def display_count(cls):
        print(f"the total count : {cls.count}")
    
obj1 = counter()
obj2 = counter()
obj3 = counter()

counter.display_count()