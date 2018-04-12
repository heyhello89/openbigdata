import re

p = re.compile('[a-z]+')
a = p.search('5 python')

m=a.start()
n=a.end()
l=m+n

print("%d, %d, %d"%(m,n,l))