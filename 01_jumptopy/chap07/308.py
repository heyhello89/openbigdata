import re
p = re.compile('aaa|bbb+')
dest_str = """aaa
bbb"""

m = p.match(dest_str)

p=re.compile('aaa.bbb',re.DOTALL)
m = p.match(dest_str)

p =re.compile('[a-z]+',re.I)
m = p.match('python')
m = p.match('Python')
m = p.match('PYTHON')
print(m)
