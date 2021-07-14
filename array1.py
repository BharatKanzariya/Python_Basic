import array
vals = array.array('f',[2.5,5,6.9,55])
vals.append(54)
print(vals)
print(vals.buffer_info())
print(vals.typecode)