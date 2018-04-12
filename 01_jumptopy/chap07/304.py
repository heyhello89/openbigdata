import re

p=re.compile('[a-z]+')
m = p.match("python")
m = p.match("3 python")

m = p.search("python")
m = p.search("3 python")

m = p.match("liff is too short")
m = p.search("life is too short")
m = p.findall("life is too short")
print(m)

result = p.finditer("life is too short")
for r in result:
    print(r)