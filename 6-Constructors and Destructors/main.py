# 6. Constructors and Destructors

class Logger:
    def __init__(self):
     print("Logger initialized: Object created.")

    def __del__(self):
     print("Logger finalized: Object destroyed.")

log  = Logger()
print(log)