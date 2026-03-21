class student:
    grade = 9
    name = "Abdul"

    def introduce(self):
        print("Hi i am a student")
        
    def details(self):
        print("Welcome to grade", self.grade)
        print("My name is", self.name)

ob = student()
ob.introduce()
ob.details()