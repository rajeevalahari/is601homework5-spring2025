"""Tests for the App functionality and its command modules."""

import pytest
from app import App
from app.plugins.greet import GreetCommand
from app.plugins.goodbye import GoodbyeCommand
from app.plugins.thanks import ThanksCommand
from app.plugins.discord import DiscordCommand
from app.commands import CommandHandler

# --- Plugin Command Tests ---

def test_plugin_greet_command(capfd):
    """Test that the GreetCommand prints the correct greeting."""
    command = GreetCommand()
    command.execute()
    out, _ = capfd.readouterr()
    assert out == "Hello, World!\n", "GreetCommand output mismatch"


def test_plugin_goodbye_command(capfd):
    """Test that the GoodbyeCommand prints the correct farewell."""
    command = GoodbyeCommand()
    command.execute()
    out, _ = capfd.readouterr()
    assert out == "Goodbye\n", "GoodbyeCommand output mismatch"


def test_plugin_thanks_command(capfd):
    """Test that the ThanksCommand prints the correct message."""
    command = ThanksCommand()
    command.execute()
    out, _ = capfd.readouterr()
    assert out == "Thankyou for executing\n", "ThanksCommand output mismatch"


def test_plugin_discord_command(capfd):
    """Test that the DiscordCommand prints the correct message."""
    command = DiscordCommand()
    command.execute()
    out, _ = capfd.readouterr()
    assert out == "I WIll send something to discord\n", "DiscordCommand output mismatch"


# --- CommandHandler Unknown Command Test ---
def test_execute_unknown_command(capsys):
    """Test that executing an unknown command prints an error message."""
    handler = CommandHandler()
    handler.execute_command("nonexistent")
    captured = capsys.readouterr()
    assert "No such command: nonexistent" in captured.out


# --- REPL Behavior Tests for App ---
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
