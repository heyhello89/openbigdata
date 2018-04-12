import re

p=re.compile('a.b')
m = p.match('akb')
m = p.match('a3b')
m = p.match('a&b')

p=re.compile('330.py')
m = p.match('330,py')
m = p.match('330.py')
p=re.compile('330[.]py')
m = p.match('330.py')
m = p.match('330,py')

print(m)