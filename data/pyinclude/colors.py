import os

COLORS = {\
    "black": "\u001b[30;1m",
    "red": "\u001b[31m",
    "green": "\u001b[32m",
    "yellow": "\u001b[33;1m",
    "blue": "\u001b[34m",
    "magenta": "\u001b[35m",
    "cyan": "\u001b[36m",
    "white": "\u001b[37m",
    "yellow-background": "\u001b[43m",
    "black-background": "\u001b[40m",
    "cyan-background": "\u001b[46;1m"
}

def color_text(text):
    for color in COLORS:
        text = text.replace("[["+color+"]]", COLORS[color])
    return text