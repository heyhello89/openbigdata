import re

p = re.compile('\section')
# dest_str='\selction'
m = p.findall('\section')
m = p.findall(' ection')

p=re.compile('\\section')
m = p.findall('\section')
print(m)