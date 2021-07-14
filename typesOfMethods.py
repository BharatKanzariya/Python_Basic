class Student:
    collage = 'VGEC'

    def __init__(self, m1, m2, m3):
        self.m1 = m1
        self.m2 = m2
        self.m3 = m3

    def avg(self):
        return (self.m1 + self.m2 + self.m3) / 3

    @classmethod
    def GetCollageName(cls):
        return cls.collage

    @staticmethod
    def info():
        print('this is staticmethod')


s1 = Student(34, 98, 65)
s2 = Student(78, 66, 98)


print(s1.avg())
print(Student.collage)
Student.info()