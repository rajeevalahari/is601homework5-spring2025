"""Tests for the App functionality and its command modules."""

import pytest
from app import App
from app.commands.goodbye import GoodbyeCommand
from app.commands.greet import GreetCommand


def test_greet_command(capfd):
    """Test that the GreetCommand prints the correct greeting."""
    command = GreetCommand()
    command.execute()
    out, _ = capfd.readouterr()
    assert out == "Hello, World!\n", "The GreetCommand should print 'Hello, World!'"


def test_goodbye_command(capfd):
    """Test that the GoodbyeCommand prints the correct farewell."""
    command = GoodbyeCommand()
    command.execute()
    out, _ = capfd.readouterr()
    assert out == "Goodbye\n", "The GoodbyeCommand should print 'Goodbye'"


def test_app_greet_command(capfd, monkeypatch):
    """Test that the REPL correctly handles the 'greet' command."""
    inputs = iter(['greet', 'exit'])
    monkeypatch.setattr('builtins.input', lambda _: next(inputs))
    app = App()
    with pytest.raises(SystemExit) as e:
        app.start()
    assert str(e.value) == "Exiting...", "The app did not exit as expected"


def test_app_menu_command(capfd, monkeypatch):
    """Test that the REPL correctly handles the 'menu' command."""
    inputs = iter(['menu', 'exit'])
    monkeypatch.setattr('builtins.input', lambda _: next(inputs))
    app = App()
    with pytest.raises(SystemExit) as e:
        app.start()
    assert str(e.value) == "Exiting...", "The app did not exit as expected"
