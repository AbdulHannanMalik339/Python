from abc  import ABC, abstractmethod
class AnimalDetail(ABC):
    @abstractmethod
    def move(self):
        pass

class Human(AnimalDetail):
    def move(self):
        print("I can walk and run")

class Snake(AnimalDetail):
    def move(self):
        print("I can slither on the ground")

class Dog(AnimalDetail):
    def move(self):
        print("I can bark")

class Lion(AnimalDetail):
    def move(self):
        print("I can roar")

R = Human()
R.move()

K= Snake()
K.move()

R = Dog()
R.move()

K = Lion()
K.move()