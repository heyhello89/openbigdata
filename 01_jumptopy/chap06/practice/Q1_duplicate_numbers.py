string=input()
list_str=string.split()
for index in list_str:
    for num in range(0, 10):
        match=index.count(str(num))
        if match!=1:
            print("False ", end="")
            break
        elif num==9 and match==1:
            print("True ", end="")