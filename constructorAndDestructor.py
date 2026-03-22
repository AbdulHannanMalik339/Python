class Employee :
    def __init__(self) :
        print("Employee created")

    def __del__(self) :
        print("Employee destroyed")

obj = Employee()
del obj