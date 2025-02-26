import sys
from app.commands import Command

class SubtractCommand(Command):
    def execute(self):
        try:
            a = float(input("Enter first number: "))
            b = float(input("Enter second number: "))
            print(f"Result: {a - b}")
        except ValueError:
            print("Invalid input. Please enter numeric values.")
