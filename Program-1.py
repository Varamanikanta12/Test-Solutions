class Calculator:
    def __init__(self, a, b):
        self.a = a
        self.b = b

    def calculate(self, operation):
        if operation == "add":
            return self.a + self.b
        elif operation == "subtract":
            return self.a - self.b
        elif operation == "multiply":
            return self.a * self.b
        elif operation == "divide":
            if self.b != 0:
                return self.a / self.b
            else:
                return "Error: Cannot divide by zero"
        else:
            return "Invalid operation"


# Example run
x = float(input("Enter first number: "))
y = float(input("Enter second number: "))
op = input("Enter operation (add/subtract/multiply/divide): ").lower()

calc = Calculator(x, y)
print("Result:", calc.calculate(op))
