class A:

    def featture1(self):
        print('feature 1 is working')

    def featture2(self):
        print('feature 2 is working')

# Single level inheritance
class B(A):

    def featture3(self):
        print('feature 3 is working')

    def featture4(self):
        print('feature 4 is working')

# Multi level inheritance
class C(B):

    def featture5(self):
        print('feature 5 is working')

    def featture6(self):
        print('feature 6 is working')

a1 = A()

b1 = B()

c1 = C()
