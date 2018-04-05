with open('learning_python.txt','r') as original:
    lines=original.read()

fix=lines.replace("python", "C")
print(fix)

with open('learn_python_copyed.txt','w') as revision:
    revision.write(fix)
