def sum_many(*args):
    sum=0

    for i in args:
        sum=sum+i

    return sum

result = sum_many(1,2,3)
print(result)

result=sum_many(1,2,3,4,5,6,7,8,9,10)
print(result)