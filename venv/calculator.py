class Calculator:
    # [1]
    # def Sum(self, Num1, Num2):
    #     return f' Sum is : {Num1+Num2}\n subtract is {Num1 - Num2}\n Multyply is {Num1 * Num2}\n and divide will be {Num1 / Num2}'

    # [2]
    # def Sum(self, Num1, Num2):
    #     return f'Summing those two will give us  : {Num1 + Num2}\n'
    # def Subtract(self, Num1, Num2):
    #     return f'Substracting those two will give us : {Num1 - Num2}'
    # def divide(self, Num1, Num2):
    #     return f'Dividing those two will give us : {Num1 / Num2}'
    # def multyply(self, Num1, Num2):
    #     return f'Multyplying those two will give us : {Num1 * Num2}'

    # [3]
    def __init__(self,Num1,Num2):
        self.sum = Num1 + Num2
        self.substract = Num1 - Num2
        self.multyply = Num1 * Num2
        self.divide = Num1 / Num2

s = Calculator(1,2)
print(s.sum)
print(s.substract)
print(s.multyply)
print(s.divide)
