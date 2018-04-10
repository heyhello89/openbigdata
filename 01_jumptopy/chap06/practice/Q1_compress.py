#책의 출력 예시대로 할것
string = input()
count=1

try:
    for size in range(0,len(string)):
        if string[size]==string[size+1]:
            count+=1
        elif size==0:
            continue
        elif string[size]!=string[size+1]:
            print(string[size]+str(count), end="")
            count=1
except IndexError:
    print(string[size]+str(count), end="")