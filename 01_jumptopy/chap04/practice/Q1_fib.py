def fib(n):
    if n==0:
        return 0
    if n==1:
        return 1
    return fib(n-2)+fib(n-1)

n=int(input("숫자를 입력하세요: "))
for i in range(n):
    print(fib(i), ", ", end='')

print(fib(n))