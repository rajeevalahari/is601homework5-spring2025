"""Tests for the calculator commands (add, sub, mul, div) and the exit command."""

from app.plugins.add import AddCommand
from app.plugins.sub import SubtractCommand
from app.plugins.mul import MultiplyCommand
from app.plugins.div import DivideCommand
from app.plugins.menu import MenuCommand

def test_plugin_add_command_valid(capfd, monkeypatch):
    """Test that the AddCommand correctly adds two numbers."""
    inputs = iter(["3", "4"])
    monkeypatch.setattr("builtins.input", lambda _: next(inputs))
    command = AddCommand()
    command.execute()
    out, _ = capfd.readouterr()
    assert "Result: 7.0" in out, "AddCommand output mismatch"

def test_plugin_add_command_invalid(capfd, monkeypatch):
    """Test that the AddCommand handles invalid input gracefully."""
    inputs = iter(["three", "4"])
    monkeypatch.setattr("builtins.input", lambda _: next(inputs))
    command = AddCommand()
    command.execute()
    out, _ = capfd.readouterr()
    assert "Invalid input" in out

def test_plugin_subtract_command_valid(capfd, monkeypatch):
    """Test that the SubtractCommand correctly subtracts two numbers."""
    inputs = iter(["10", "4"])
    monkeypatch.setattr("builtins.input", lambda _: next(inputs))
    command = SubtractCommand()
    command.execute()
    out, _ = capfd.readouterr()
    assert "Result: 6.0" in out, "SubtractCommand output mismatch"

def test_plugin_subtract_command_invalid(capfd, monkeypatch):
    """Test that the SubtractCommand handles invalid input gracefully."""
    inputs = iter(["ten", "4"])
    monkeypatch.setattr("builtins.input", lambda _: next(inputs))
    command = SubtractCommand()
    command.execute()
    out, _ = capfd.readouterr()
    assert "Invalid input" in out

def test_plugin_multiply_command_valid(capfd, monkeypatch):
    """Test that the MultiplyCommand correctly multiplies two numbers."""
    inputs = iter(["3", "5"])
    monkeypatch.setattr("builtins.input", lambda _: next(inputs))
    command = MultiplyCommand()
    command.execute()
    out, _ = capfd.readouterr()
    assert "Result: 15.0" in out, "MultiplyCommand output mismatch"

def test_plugin_multiply_command_invalid(capfd, monkeypatch):
    """Test that the MultiplyCommand handles invalid input gracefully."""
    inputs = iter(["three", "5"])
    monkeypatch.setattr("builtins.input", lambda _: next(inputs))
    command = MultiplyCommand()
    command.execute()
    out, _ = capfd.readouterr()
    assert "Invalid input" in out

def test_plugin_divide_command_valid(capfd, monkeypatch):
    """Test that the DivideCommand correctly divides two numbers."""
    inputs = iter(["20", "4"])
    monkeypatch.setattr("builtins.input", lambda _: next(inputs))
    command = DivideCommand()
    command.execute()
    out, _ = capfd.readouterr()
    assert "Result: 5.0" in out, "DivideCommand output mismatch"

def test_plugin_divide_command_division_by_zero(capfd, monkeypatch):
    """Test that the DivideCommand handles division by zero."""
    inputs = iter(["20", "0"])
    monkeypatch.setattr("builtins.input", lambda _: next(inputs))
    command = DivideCommand()
    command.execute()
    out, _ = capfd.readouterr()
    assert "Division by zero" in out or "not allowed" in out

def test_plugin_divide_command_invalid(capfd, monkeypatch):
    """Test that the DivideCommand handles invalid input gracefully."""
    inputs = iter(["twenty", "4"])
    monkeypatch.setattr("builtins.input", lambda _: next(inputs))
    command = DivideCommand()
    command.execute()
    out, _ = capfd.readouterr()
    assert "Invalid input" in out

def test_plugin_menu_command(capfd):
    """Test that the MenuCommand prints the expected menu."""
    command = MenuCommand()
    command.execute()
    out, _ = capfd.readouterr()
    assert "Available commands:" in out, "Menu header missing"
    assert "add" in out, "Add command not listed"
    assert "sub" in out, "Subtract command not listed"
    assert "mul" in out, "Multiply command not listed"
    assert "div" in out, "Divide command not listed"
    assert "exit" in out, "Exit command not listed"
    assert "menu" in out, "Menu command not listed"
