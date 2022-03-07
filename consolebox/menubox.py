from .itemlist import ItemList
from .box import Box
from .style import Style
from .keyboard import Keyboard
from .keylist import KeyList
from types import FunctionType
from typing import Any
from colorama import init


class MenuBox():

    def __init__(self, items: dict[int,str], option: dict[int, FunctionType], attributes: dict[str,Any]):
        init()
        self.options = option

        self.menu_attributes: dict[str, Any] = {
            "length": 65,  # Broad min 40 max 90
            "start" : 1,
            "size": len(items),  # Quantity of items
            "columns": 1,  # Max = 2
            "header" : None,
            "enumerate": False,  # True or False
            "indicator": "->",  # ==>, *, -, ::, +, @
            "alignment": "centered",  # Right, left, centered
            "title": False,  # True or False
            "Title": "Main menu",  # Title text max 36 characters
            "color_box": "GREEN",
            "color_text": "GREEN",
            "color_background": "DEFAULT",
            "color_selecter": "BLUE",
            "color_menu_box": "",
            "color_title_box": "",
            "color_menu_text": "",
            "color_title_text": "",
            "color_text_title_background": "",
            "color_box_title_background": "",
            "side": " ",  # True or False
            "left": "║",
            "right": "║",
            "center": "║",
            "up": "═",
            "down": "═",
            "corner": False,
            "corner_left_up": "╔",
            "corner_right_up": "╗",
            "corner_left_down":  "╚",
            "corner_right_down": "╝",
            "intersection": False,
            "inter_left": "╠",
            "inter_right":  "╣",
            "inter_up": "╦",
            "inter_down": "╩"
        }
        self.menu_attributes["color_menu_box"] = self.menu_attributes["color_box"]
        self.menu_attributes["color_title_box"] = self.menu_attributes["color_menu_box"]
        self.menu_attributes["color_menu_text"] = self.menu_attributes["color_text"]
        self.menu_attributes["color_title_text"] = self.menu_attributes["color_menu_text"]
        self.menu_attributes["color_text_title_background"] = self.menu_attributes["color_background"]
        self.menu_attributes["color_box_title_background"] = self.menu_attributes["color_background"]

        for i in attributes: # Data dump
            self.menu_attributes[i] = attributes[i]

        self.position: dict[str,int] = {
            # "up" : 1,
            # "down" : 25,
            "centered": 15,
            "left": 1,
            "right": 47
        }

        self.keyboard = Keyboard() # For read keyboard

        self.row_printing: int = self.menu_attributes['start']  # pointer_position_row

        self.item_list = ItemList(items)

    def pause_class(self, option: int = 0) -> None:
        """Pause the program"""
        print('Pres any key to continue   ')
        self.keyboard.read()
        Style.clear()
        self.row_printing = self.menu_attributes["start"]
        self.static_menu()
        self.menu(option, 1)

    def static_menu(self) -> None:
        """Menu interface"""
        Style.lowvideo(self.menu_attributes["color_text"],
                            self.menu_attributes["color_background"]) # Color text

        # Point from which to start printing
        alig: int = self.position[self.menu_attributes["alignment"]]
        length: int = self.menu_attributes["length"]  # Table size to print
        size: int = self.menu_attributes["size"]
        z: int = 0
        x: int = 0  # regulates the printing on the x-axis representing the column

        # Print headers
        if self.menu_attributes != None:
            if type(self.menu_attributes["header"]) == FunctionType:
                Style.gotoxy(1,1)
                self.menu_attributes["header"]()
            elif type(self.menu_attributes["header"]) == str:
                Style.printxy(1, 1, self.menu_attributes["header"])

        # Title
        x = alig  # regulates the printing on the x-axis representing the column
        if self.menu_attributes["title"]:
            title_attributes: dict[str,Any]={
                "length": self.menu_attributes["length"],
                "start" : self.row_printing,
                "size": 1,
                "title": True,
                "columns": 1,
                "alignment": self.menu_attributes["alignment"],  # Right, left, centered
                "left": self.menu_attributes["left"],
                "right": self.menu_attributes["right"],
                "center": self.menu_attributes["center"],
                "up": self.menu_attributes["up"],
                "down": self.menu_attributes["down"],
                "corner": self.menu_attributes["corner"],
                "corner_left_up": self.menu_attributes["corner_left_up"],
                "corner_right_up": self.menu_attributes["corner_right_up"],
                "corner_left_down":  self.menu_attributes["corner_left_down"],
                "corner_right_down": self.menu_attributes["corner_right_down"],
                "intersection": False,
            }

            Style.lowvideo(self.menu_attributes["color_title_box"],
                            self.menu_attributes["color_box_title_background"]) # Color box title
            box_title: Box = Box(title_attributes, self.row_printing)
            box_title.show()

            Style.lowvideo(self.menu_attributes["color_title_text"],
                            self.menu_attributes["color_text_title_background"]) # Color text title

            self.row_printing += 1
            # Title text
            z = len(self.menu_attributes["Title"])  # title length
            z = (length - z) - 2  # panel size - 2 edges - title size
            if z > 1:
                x = int(z / 2)  # spare space / 2
            else:
                x = 1
            x += alig  # excess + alignment

            Style.gotoxy(x, self.row_printing)
            print(self.menu_attributes["Title"], end='')

            self.row_printing += 1  # increase the print row

        Style.lowvideo(self.menu_attributes["color_menu_box"],
                            self.menu_attributes["color_text_title_background"]) # Color menu box
        box_menu: Box = Box(self.menu_attributes, self.row_printing)
        box_menu.show()

        Style.lowvideo(self.menu_attributes["color_menu_text"],
                            self.menu_attributes["color_text_title_background"]) # Color menu items
        # Items
        self.item_list.setposition( # calculate the coordinates of the items
            self.menu_attributes['length'],
            self.menu_attributes['columns'],
            self.row_printing,
            self.position[self.menu_attributes['alignment']]
        )

        msg: str
        position: tuple[int,int]
        for i in range(1, size + 1): # Print the items
            if self.menu_attributes["enumerate"]:
                msg = f"    {i}. {self.item_list[i - 1]}"
            else:
                msg = f"       {self.item_list[i - 1]}"
            position = self.item_list[i - 1].getposition
            Style.printxy(position[0], position[1], msg)


    def menu(self, options: int, previous: int) -> None:
        self.view(previous)
        self.select(options)

    def view(self, item: int):
        msg: str
        position: tuple[int,int] = self.item_list[item - 1].getposition
        if self.menu_attributes["enumerate"]:
            msg = f"    {item}. {self.item_list[item - 1]}"
        else:
            msg = f"       {self.item_list[item - 1]}"

        Style.lowvideo(self.menu_attributes["color_menu_text"],
                            self.menu_attributes["color_background"])
        Style.printxy(position[0], position[1], msg)

    def select(self, item: int):
        msg: str
        position: tuple[int,int] = self.item_list[item - 1].getposition
        indi: str = self.menu_attributes["indicator"]
        if self.menu_attributes["enumerate"]:
            msg = f" {indi} {item}. {self.item_list[item - 1]}"
        else:
            msg = f" {indi}    {self.item_list[item - 1]}"

        Style.highvideo(self.menu_attributes["color_menu_text"],
                            self.menu_attributes["color_selecter"])

        Style.printxy(position[0], position[1], msg)

        Style.lowvideo(self.menu_attributes["color_menu_text"],
                            self.menu_attributes["color_background"])

    def sub_menu(self, option: int) -> None:
        position: int = self.row_printing
        size: int = self.menu_attributes["size"]
        columns: int = self.menu_attributes["columns"]
        half_size: int = int((size/columns) + 0.5)

        position += int(half_size)
        if self.menu_attributes["title"]:
            position += 2

        Style.gotoxy(1, position)
        Style.lowvideo(self.menu_attributes["color_text"],
                            self.menu_attributes["color_background"])
        print('===============================================================================')

        Style.cursoron()
        if option in self.options:
            self.options[option]()
        self.pause_class(option)

    # --------------------------------------------------------------------------------

    def show(self) -> None:
        size: int = self.menu_attributes["size"]
        columns: int = self.menu_attributes["columns"]
        previus_manual: int = 0
        control: tuple[int,int]
        Style.clear()
        keylist = KeyList(size, columns)

        Style.cursoroff()
        self.static_menu()

        while True:
            control = keylist.listening(previus_manual)
            previus_manual = 0 # Reset previus to its default state
            if control[1] == 0:
                if control[0] == -1: # Sentry that controls the exit
                    break
                elif control[0] > 0:
                    previus_manual = 1 # Control the previous selection from the menubox to avoid bugs
            elif control[1] == -2: # sentinel controlling enter
                if control[0] > 0:
                        self.sub_menu(control[0])
            elif control[1] > 0:
                if control[0] == 0:
                    self.menu(1, control[1]) # Element zero does not exist so element one is selected
                elif control[0] > 0:
                    self.menu(control[0], control[1])
            else:
                continue
            Style.cursoroff() # Hide the courses
        Style.cursoron() # Show the cursor at the end of the program



