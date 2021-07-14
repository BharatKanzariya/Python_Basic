# We can return 2 value using function

def add_sub(x,y):
    c = x + y
    d = x - y
    return c,d

result1,result2 = add_sub(8,3)
print(result1)
print(result2)

result = add_sub(9,3)
print(result)