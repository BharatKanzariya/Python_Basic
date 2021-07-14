def person(name,**data):
    print(name)
    print(data)
    for i,j in data.items():
        print(i,j)
person('bharat',age=19,city='kenedi',mo=9726869684)