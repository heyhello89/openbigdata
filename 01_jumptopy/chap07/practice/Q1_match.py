import re

p = re.compile('a[.]{3,}b')
a = p.match('acccb')
b = p.match('a....b')
c = p.match('aaab')
d = p.match('a.cccb')

print(a)
print(b)
print(c)
print(d)