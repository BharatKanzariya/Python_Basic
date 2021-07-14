s  = input()

if s[8:] == 'PM':
    if s[:2] == "12":
        print(s[:8])
    else:
        h = int(s[:2])
        h = 12 + h
        n = str(h) + s[2:8]
        print(n)
else:
    if s[:2] == "12":
        h = '00'
        n = h + s[2:8]
        print(n)
    else:
        print(s[:8])
