class Calculator:
    def add(self, a, b):
        print(f"{a} + {b} = {a + b}")

    def subtract(self, a, b):
        print(f"{a} - {b} = {a - b}")

    def multiply(self, a, b):
        print(f"{a} * {b} = {a * b}")

    def divide(self, a, b):
        if b != 0:
            print(f"{a} / {b} = {a / b}")
        else:
            print("Cannot divide by zero.")