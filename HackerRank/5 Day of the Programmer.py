y = int(input())

if y == 1918:
    print("26.09.1918")
elif (y < 1918) and (y % 4 == 0):
    print("12.09.%s" % y)
elif (y > 1918) and (y % 400 == 0 or (y % 4 == 0 and y % 100 != 0)):
    print("12.09.%s" % y)
else:
    print("13.09.%s" % y)
