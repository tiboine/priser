import re

mydict = {'120x30': 123, '110x40': 123}

ny = {}

for i, val in mydict.items():
    i = str(i).split('x')
    ny[f"{i[1]}x{i[0]}"] = val

print(ny)
