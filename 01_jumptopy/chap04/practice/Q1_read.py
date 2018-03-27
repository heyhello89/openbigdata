f=open('sample.txt','r')

lines=f.readlines()

total=0
for line in lines:
    score=int(line)
    total+=score

averge=int(total/len(lines))
f.close()

f=open('result.txt','w')
f.write(str(averge))
f.close()