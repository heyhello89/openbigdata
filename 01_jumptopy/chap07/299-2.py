import re

p=re.compile('[a-c]-case')
m=p.match('able')
m=p.match('a-case')
m=p.match('b-case')
m=p.match('c-case')
m=p.match('b-case sdfsdfsd')
print(m)