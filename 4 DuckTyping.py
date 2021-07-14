class Chainees:

    def eat(self):
        print('chainees food is weard.')


class Indian:

    def eat(self):
        print('indian food is good.')


class Mans:

    def dish(self,type):
        type.eat()

type = Chainees()

m1 = Mans()
m1.dish(type)