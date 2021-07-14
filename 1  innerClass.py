class Student:

    def __init__(self, name, roll):
        self.name = name
        self.roll = roll
        self.lap = self.Laptop()

    def show(self):
        print(self.name, self.roll)
        self.lap.con()

    class Laptop:

        def __init__(self):
            self.brand = 'hp'
            self.cpu = 'i5'
            self.ram = 8

        def con(self):
            print(self.brand, self.cpu, self.ram)


s1 = Student('Bharat', 45)
s2 = Student('Hiren', 44)

s1.show()