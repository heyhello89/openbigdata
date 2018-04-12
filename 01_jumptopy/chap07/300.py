import re

p=re.compile('ca*t')
m = p.match('ct')
m = p.match('cat')
m = p.match('caaaat')
print(m)