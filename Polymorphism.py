class cat:
    def __init__(self, name, age):
        self.name = name
        self.age = age
        
    def info(self):
        print(f"Cat Name: {self.name}, Age: {self.age}")

    def make_sound(self):
        print("Meow")

class dog:
    def __init__(self, name, age):
        self.name = name
        self.age = age
        
    def info(self):
        print(f"Dog Name: {self.name}, Age: {self.age}")

    def make_sound(self):
        print("Woof")

cat1 = cat("Dodo", 2.5)
dog1 = dog("Tyson", 8)

for animal in (cat1, dog1):
    animal.make_sound()
    animal.info()