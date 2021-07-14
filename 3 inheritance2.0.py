class A:

    def __init__(self):
        print('init in A')

    def featture1(self):
        print('feature 1 is working')

    def featture2(self):
        print('feature 2 is working')


class B(A):

    def __init__(self):
        super().__init__()
        print('init in B')

    def featture3(self):
        print('feature 3 is working')

    def featture4(self):
        print('feature 4 is working')


a1 = B()