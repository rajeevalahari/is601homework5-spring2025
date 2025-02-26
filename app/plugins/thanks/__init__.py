import sys
from app.commands import Command


class ThanksCommand(Command):
    def execute(self):
        print(f'Thankyou for executing')