import re

p=re.compile('[a-c]')
# m=p.match('glob')
m=p.match('able')
print(m)