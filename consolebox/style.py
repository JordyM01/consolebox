from .keyboard import Keyboard
from colorama import init

class Style():
    low_color_text: dict[str,int] = {
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
    high_color_text: dict[str,int] = {
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
    low_color_background: dict[str,int] = {
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
    high_color_background: dict[str,int] = {
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
    def clear(cls) -> None: return print("\033[2J\033[1;1f", end='')
    """Position the pointer at the x and y coordinates with ANSI Scape Sequence"""

    @classmethod
    def cursoroff(cls) -> None: return print("\033[?25l", end='')

    @classmethod
    def cursoron(cls) -> None: return print("\033[?25h", end='')

    @classmethod
    def get_cursorposition(cls): # Not functional
        position: tuple[int,int]
        x: int
        y: int
        console: str
        temp: str

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
               x: int = 1, y: int = 1) -> None: return print("%c[%d;%df" % (0x1B, y, x), end='')

    @classmethod
    def highvideo(cls, text_color: str = "DEFAULT", background_color: str = "DEFAULT") -> None:
        """Highlight a text area"""
        print("%c[%d;%d;%dm" % (0x1B, 1, cls.high_color_background[background_color],
                                            cls.high_color_text[text_color]), end='')

    @classmethod
    def lowvideo(cls, text_color: str = "DEFAULT", backgroud_color: str = "DEFAULT") -> None:
        """Sets the color in low contrast mode"""
        print("%c[%d;%dm" % (0x1B, cls.low_color_background[backgroud_color],
                                    cls.low_color_text[text_color]), end='')

    @classmethod
    def pause(cls, msg: str = "Press any key to continue") -> None:
        print(msg)
        cls.keyboard.read()

    @classmethod
    def printxy(cls, x: int = 1, y: int = 1, msg: str = "Text") -> None:
        cls.gotoxy(x, y)
        print(msg)
