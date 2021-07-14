# in python argument is not pass by value nor pass by refaranc

def update(x):
    print("x=",x)
    print(id(x)) # here value of a is pass to the x but the id of x is remain same
                 # as id of a
    x = 10   # here we update value so id of x is change
    print("x",id(x))

a = 5
print("a=",a)
print(id(a))

update(a)