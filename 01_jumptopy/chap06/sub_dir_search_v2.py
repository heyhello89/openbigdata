import os

for (path, dir, file) in os.walk("C:/"):
    for filename in file:
        ext=os.path.splitext(filename)[-1]
        if ext=='.py':
            print("%s/%s"%(path,filename))