import re

p=re.compile('ca{2}t')
m = p.match('cat')
m = p.match('caat')
m = p.match('caaaat')

p=re.compile('ca{2,5}t')
m = p.match('cat')
m = p.match('caat')
m = p.match('caaaaat')
m = p.match('caaaat')
print(m)