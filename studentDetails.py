class person :
    def __init__(self, fname, Iname):
        self.fname = fname
        self.Iname = Iname

        def printname(self):
            print(self.fname, self.Iname)

class student(person):
    def __init__(self, fname, Iname, year):
        super().__init__(fname, Iname)
        self.graduationyear = year

x = student("Abdul", "King", 2024)
print(x.fname)
print(x.graduationyear)