class Calc:
    def __init__(self):
        self.__num1 = 0
        self.__num2 = 0

    def set_numbers(self, num1, num2):
        self.__num1 = num1
        self.__num2 = num2

    def add(self):
        return self.__num1 + self.__num2

    def sub(self):
        return self.__num1 - self.__num2

c = Calc()

num1 = float(input("Enter First No : "))
num2 = float(input("Enter Second No : "))

c.set_numbers(num1, num2)

print(f"Addition: {c.add()}")
print(f"Subtraction: {c.sub()}")
