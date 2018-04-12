import re

p = re.compile('[a-z][0-9]-case')
l = p.match('a1-case')
m = p.match('b1-case')
n = p.match('b9-case')

print(l)
print(m)
print(n)