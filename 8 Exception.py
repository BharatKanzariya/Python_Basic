a = 5
b = 0

try:
    print('Resource open.')
    print('Division=', a/b)
    k = int(input('Enter number:'))
    print(k)

except ZeroDivisionError as e:
    print("You can't devide by zero to",a,'  Error type=',e)

except ValueError as e:
    print('Invalid input.','  Error type=',e)
finally:
    print('Resource closed.')