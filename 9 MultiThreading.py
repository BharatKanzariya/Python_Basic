from threading import *
from time import *
tim1 = time()

class Hello(Thread):
    def run(self):
        for i in range(10):
            print('Hello')
            sleep(0.5)


class Hi(Thread):
    def run(self):
        for i in range(10):
            print('Hi')
            sleep(0.5)


t1 = Hello()
t2 = Hi()

t1.start()
sleep(0.1)
t2.start()

t1.join()
t2.join()

tim2 = time()
print(tim2-tim1)