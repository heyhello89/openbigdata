import re

p=re.compile('abc')
m=p.match('ab')
# m=p.match('abc')
# m=p.match('abcd')
print(m)