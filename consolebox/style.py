from .keyboard import Keyboard
from colorama import init

class Style():
    low_color_text = {
        "BLACK" : 30,
        "RED" : 31,
        "GREEN" : 32,
        "YELLOW" : 33,
        "BLUE" : 34,
        "MAGENTA" : 35,
        "CYAN" : 36,
        "WHITE" : 37,
        "DEFAULT": 00
    }
    high_color_text = {
        "BLACK" : 90,
        "RED" : 91,
        "GREEN" : 92,
        "YELLOW" : 93,
        "BLUE" : 94,
        "MAGENTA" : 95,
        "CYAN" : 96,
        "WHITE" : 97,
        "DEFAULT": 00
    }
    low_color_background = {
        "BLACK" : 40,
        "RED" : 41,
        "GREEN" : 42,
        "YELLOW" : 43,
        "BLUE" : 44,
        "MAGENTA" : 45,
        "CYAN" : 46,
        "WHITE" : 47,
        "DEFAULT": 00
    }
    high_color_background = {
        "BLACK" : 100,
        "RED" : 101,
        "GREEN" : 102,
        "YELLOW" : 103,
        "BLUE" : 104,
        "MAGENTA" : 105,
        "CYAN" : 106,
        "WHITE" : 107,
        "DEFAULT": 00
    }

    def __init__(self):
        init()
        self.keyboard = Keyboard()

    """Clean screen with ANSI Scape Sequence"""
    @classmethod
    def clear(cls): return print("\033[2J\033[1;1f")
    """Position the pointer at the x and y coordinates with ANSI Scape Sequence"""

    @classmethod
    def cursoroff(cls): return print("\033[?25l")

    @classmethod
    def cursoron(cls): return print("\033[?25h")

    @classmethod
    def get_cursorposition(cls): # Not functional

        console = input("\033[6n") # Incomplete
        console = console[2:]
        x = console.find(';')
        temp = console
        console = console[:x]
        x = int(console)
        temp = temp[3:]
        temp = temp.replace('R', '')
        y = int(temp)
        position = (x,y)
        return position

    @classmethod
    def gotoxy(cls,
               x = 1, y = 1): return print("%c[%d;%df" % (0x1B, y, x), end='')

    @classmethod
    def highvideo(cls, text_color = "DEFAULT", background_color = "DEFAULT"):
        """Highlight a text area"""
        print("%c[%d;%d;%dm" % (0x1B, 1, cls.high_color_background[background_color],
                                            cls.high_color_text[text_color]), end='')

    @classmethod
    def lowvideo(cls, text_color = "DEFAULT", backgroud_color = "DEFAULT"):
        """Sets the color in low contrast mode"""
        print("%c[%d;%dm" % (0x1B, cls.low_color_background[backgroud_color],
                                    cls.low_color_text[text_color]), end='')

    @classmethod
    def pause(cls, msg = "Press any key to continue"):
        print(msg)
        cls.keyboard.read()

    @classmethod
    def printxy(cls, x = 1, y = 1, msg = "Text"):
        cls.gotoxy(x, y)
        print(msg)
