import re

p=re.compile('[0-9]')
# p=re.compile('\d')
m = p.match("7")

# p=re.compile('\D')
# m = p.match('a')

# p=re.compile(' ')
# p=re.compile('\s')
# p=re.compile('\S')
# m = p.match(' ')

p=re.compile('[a-zA-Z0-9]')
p=re.compile('\w')
# m=p.match('9')
p=re.compile('\W')
m=p.match('9')
m=p.match('!')
print(m)