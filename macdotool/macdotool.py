import pyautogui

import click


@click.group()
def commands():
    pass


@commands.command()
@click.argument("x", type=float)
@click.argument("y", type=float)
def mousemove(x, y):
    pyautogui.moveTo(x, y)


@commands.command(name="click")
@click.argument(
    "button", type=int,
)
def click_command(button):
    button = {1: pyautogui.LEFT, 2: pyautogui.MIDDLE, 3: pyautogui.RIGHT}[button]
    pyautogui.click(button=button)


@commands.command("mousemove_relative")
@click.argument("x", type=float)
@click.argument("y", type=float)
def mousemove_relative(x, y):
    pyautogui.move(x, y)


def main():
    commands()
