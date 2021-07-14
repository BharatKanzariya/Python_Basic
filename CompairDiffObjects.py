class Details:

    def __init__(self):
        self.name = 'bharat'
        self.age = 20

    def compair(self,other):
        if self.age == other.age:
            return True
        else:
            return False


h1 = Details()
h2 = Details()

print(h1.age)
h2.age = 33
print(h2.age)

if h1.compair(h2):
    print('Age are same')
else:
    print('Age are differant')