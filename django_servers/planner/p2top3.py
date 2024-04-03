class MyNumber:
    def __init__(self, value):
        self.value = value

class MyDivisor:
    def __truediv__(self, other):
        if other.value == 0:
            raise ZeroDivisionError("Division by zero is not allowed.")
        return other.value / self.value

# Create instances of MyNumber and MyDivisor
num1 = MyNumber(10)
divisor = MyDivisor()

# Use the overloaded division operator
result = num1 / divisor
print(result)  # Output: 1.0


















class MyNumber:
    def __init__(self, value):
        self.value = value

    def __truediv__(self, other):
        if other == 0:
            raise ZeroDivisionError("Division by zero is not allowed.")
        return self.value / other

# Create instances of MyNumber
num1 = MyNumber(10)
num2 = MyNumber(2)

# Use the overloaded division operator
result = num1 / num2
print(result)  # Output: 5.0




# 8-}b?Eg}Bnnq;X=

    

