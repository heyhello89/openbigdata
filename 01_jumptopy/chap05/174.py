class Calculator:
    def __init__(self):
        self.result=0
    def adder(self,num):
        self.result+=num
        return self.result

cal1 = Calculator()
cal2 = Calculator()

print(cal1.addr(3))
print(cal1.addr(4))
print(cal2.addr(3))
print(cal2.addr(7))
