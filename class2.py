class Computer:

    def __init__(self,cpu,ram):
        self.c = cpu
        self.r = ram


    def config(self):
        print('Config is =',self.c,self.r)


com1 = Computer('i5',16)
com2 = Computer('Ryzen',16)

com1.config()
com2.config()