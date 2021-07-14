# There are 4 types of function
# Position
# Keyword
# Default
# Variable length

# for keyword
print('for keyword')
def person(name,age):
    print(name,age)

person(age=20,name='bharat')
print()
# if we not pass argument in sequance we shoud define like upper function


# for default
print('for default')
def person2(name,age=15):
    print(name,age)

person2('bharat')
print()
# if we dont pass any value it take default value like upper function age


# for variable length
print('for variable length')
def sum(a,*b):
    print(a) # here first argument assign to variable 'a'
    print(b) # And the remain all argument assign as tuppel to '*b'
    c = a
    for i in b:
        c = c + i
    print(c)

sum(1,2,3,4,5)
