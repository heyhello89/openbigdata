import re

p=re.compile('.+[.]...')
# m = p.match('a.txt')
m = p.match('bk3.py')
m = p.match('python.doc')
print(m)