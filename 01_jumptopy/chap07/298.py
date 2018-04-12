import re

p=re.compile('[abc]')
# m=p.match('a')
# m=p.match('before')
# m=p.match('dude')
m=p.match('glob')    # 매칭이 안된다 --> 첫번째 문자가 맵핑이 되어야함
print(m)