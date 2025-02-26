import sys
from app.commands import Command

class MenuCommand(Command):
    """A command that prints a static list of available commands."""

    def execute(self):
        print("Available commands:")
        print("  add  -> Adds two numbers")
        print("  sub  -> Subtracts the second number from the first")
        print("  mul  -> Multiplies two numbers")
        print("  div  -> Divides the first number by the second")
        print("  exit -> Exits the application")
        print("  menu -> Displays this menu")

