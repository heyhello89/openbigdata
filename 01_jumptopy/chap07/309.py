import re
p = re.compile('python\s\w+')
dest_str = """python one python debug
life is too short
python two
you need python
python three"""
m = p.findall(dest_str)
print(m)