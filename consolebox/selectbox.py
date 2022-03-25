from .itemlist import ItemList
from .box import Box
from .style import Style
from .keyboard import Keyboard
from .keylist import KeyList
from types import FunctionType
from typing import Any
from colorama import init

class SelectBox:
    _quantity: int = 0

    def __init__(self, items: dict[int,str], attributes: dict[str,Any] = {}):
        init()

        self._attributes: dict[str, Any] = {
            "length": 65,  # Broad min 40 max 90
            "start" : 1,
            "size": len(items),  # Quantity of items
            "columns": 1,  # Max = 2
            "header" : None,
            "enumerate": False,  # True or False
            "indicator": "■",  # ->, ==>, *, -, ::, +, @
            "alignment": "centered",  # Right, left, centered
            "title": False,  # True or False
            "Title": "Main menu",  # Title text max 36 characters
            "pause_message" : "Press Any key to continue",
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
            "separation_sub_menu": "",
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

        self._attributes["color_menu_box"] = self._attributes["color_box"]
        self._attributes["color_title_box"] = self._attributes["color_menu_box"]
        self._attributes["color_menu_text"] = self._attributes["color_text"]
        self._attributes["color_title_text"] = self._attributes["color_menu_text"]
        self._attributes["color_text_title_background"] = self._attributes["color_background"]
        self._attributes["color_box_title_background"] = self._attributes["color_background"]

        if attributes.__len__() != 0:
            for i in attributes: # Data dump
                self._attributes[i] = attributes[i]

        self.position: dict[str,int] = {
            # "up" : 1,
            # "down" : 25,
            "centered": 15,
            "left": 1,
            "right": 47
        }

        self.keyboard = Keyboard() # For read keyboard

        self.row_printing: int = self._attributes['start']  # pointer_position_row

        self.item_list = ItemList(items) # Items list object instantiation

    def _pause_class(self, msg: str, option: int = 0) -> None:
        """Pause the program"""
        print(msg, end='')
        self.keyboard.read()
        Style.clear() # Clear screen
        self.row_printing = self._attributes["start"] # Set print line
        self._static_menu() # Load static menu after clear screen
        self._menu(option, 1) # Load de selected item

    def _static_menu(self) -> None:
        """Menu interface"""
        Style.lowvideo(self._attributes["color_text"],
                            self._attributes["color_background"]) # Color text

        # Point from which to start printing
        alig: int = self.position[self._attributes["alignment"]]
        length: int = self._attributes["length"]  # Table size to print
        z: int = 0
        x: int = 0  # regulates the printing on the x-axis representing the column

        # Print headers
        if self._attributes["header"] != None:
            if type(self._attributes["header"]) == FunctionType:
                Style.gotoxy(1,1)
                self._attributes["header"]()
            elif type(self._attributes["header"]) == str:
                Style.printxy(1, 1, self._attributes["header"])

        # Title
        x = alig  # regulates the printing on the x-axis representing the column
        if self._attributes["title"]:
            title__attributes: dict[str,Any] = {
                "length": self._attributes["length"],
                "start" : self.row_printing,
                "size": 1,
                "title": True,
                "columns": 1,
                "alignment": self._attributes["alignment"],  # Right, left, centered
                "left": self._attributes["left"],
                "right": self._attributes["right"],
                "center": self._attributes["center"],
                "up": self._attributes["up"],
                "down": self._attributes["down"],
                "corner": self._attributes["corner"],
                "corner_left_up": self._attributes["corner_left_up"],
                "corner_right_up": self._attributes["corner_right_up"],
                "corner_left_down":  self._attributes["corner_left_down"],
                "corner_right_down": self._attributes["corner_right_down"],
                "intersection": False,
            }

            Style.lowvideo(self._attributes["color_title_box"],
                            self._attributes["color_box_title_background"]) # Color box title
            box_title: Box = Box(title__attributes, self.row_printing)
            box_title.show()

            Style.lowvideo(self._attributes["color_title_text"],
                            self._attributes["color_text_title_background"]) # Color text title

            self.row_printing += 1
            # Title text
            z = len(self._attributes["Title"])  # title length
            z = (length - z) - 2  # panel size - 2 edges - title size
            if z > 1:
                x = int(z / 2)  # spare space / 2
            else:
                x = 1
            x += alig  # excess + alignment

            Style.gotoxy(x, self.row_printing)
            print(self._attributes["Title"], end='')

            self.row_printing += 1  # increase the print row

        Style.lowvideo(self._attributes["color_menu_box"],
                            self._attributes["color_text_title_background"]) # Color menu box

        box_menu: Box = Box(self._attributes, self.row_printing) # Instantiate an object of class box
        box_menu.show() # Show the box on the screen

        Style.lowvideo(self._attributes["color_menu_text"],
                            self._attributes["color_text_title_background"]) # Color menu items

        # Items
        self.item_list.setposition( # calculate the coordinates of the items
            self._attributes['length'],
            self._attributes['columns'],
            self.row_printing,
            self.position[self._attributes['alignment']]
        )
        self._print_items()

    def _print_items(self) -> None:
        msg: str
        position: tuple[int,int]
        size: int = self._attributes["size"]

        for i in range(1, size + 1): # Print the items
            if self._attributes["enumerate"]:
                msg = f"    {i}. {self.item_list[i - 1]}"
            else:
                msg = f"       {self.item_list[i - 1]}"
            position = self.item_list[i - 1].getposition
            Style.printxy(position[0], position[1], msg)

    def _menu(self, options: int, previous: int) -> None:
        self._view(previous)
        self._select(options)

    def _msg(self, item: int, indi: str = None) -> str:
        msg: str

        if indi == None: # If indicator was not sent
            indi = '  '

        if self._attributes["enumerate"]:
            msg = f" {indi} {item}. {self.item_list[item - 1]}"
        else:
            msg = f" {indi}    {self.item_list[item - 1]}"

        return msg

    def _view(self, item: int) -> None:
        msg: str
        position: tuple[int,int] = self.item_list[item - 1].getposition

        msg = self._msg(item)

        Style.lowvideo(self._attributes["color_menu_text"],
                            self._attributes["color_background"])
        Style.printxy(position[0], position[1], msg)

    def _select(self, item: int) -> None:
        msg: str
        position: tuple[int,int] = self.item_list[item - 1].getposition
        indi: str = self._attributes["indicator"]

        msg = self._msg(item, indi)

        Style.highvideo(self._attributes["color_menu_text"],
                            self._attributes["color_selecter"])

        Style.printxy(position[0], position[1], msg)

        Style.lowvideo(self._attributes["color_menu_text"],
                            self._attributes["color_background"])

    def _sub_menu(self, option: int) -> None:
        position: int = self.row_printing
        size: int = self._attributes["size"]
        columns: int = self._attributes["columns"]
        half_size: int = int((size/columns) + 0.5)

        position += int(half_size)
        if self._attributes["title"]:
            position += 2
        if columns % 2 == 1:
            position += 1

        Style.gotoxy(1, position)
        Style.lowvideo(self._attributes["color_text"],
                            self._attributes["color_background"])

        #print(position)
        print(self._attributes["separation_sub_menu"])

        self._sub_menu_action(option) # Run the submenu action

    def _sub_menu_action(self, option: int) -> None:
        Style.cursoron()
        self._pause_class(self._attributes['pause_message'], option)

    def exit_return(self) -> None:
        print('') # Space for an outgoing message

    def exit_(self) -> Any:
        position: int = self.row_printing
        size: int = self._attributes["size"]
        columns: int = self._attributes["columns"]
        half_size: int = int((size/columns) + 0.5)

        position += int(half_size)
        if self._attributes["title"]:
            position += 2
        if columns % 2 == 1:
            position += 1

        Style.gotoxy(1, position)
        return self.exit_return()

    # -----------------------------[----Show box----]------------------------------------------------

    def show(self) -> Any:
        size: int = self._attributes["size"]
        columns: int = self._attributes["columns"]
        previus_manual: int = 0
        control: tuple[int,int]
        Style.clear()
        keylist = KeyList(size, columns)

        Style.cursoroff()
        self._static_menu()

        while True:
            control = keylist.listening(previus_manual)
            previus_manual = 0 # Reset previus to its default state
            if control[1] == 0:
                if control[0] == -1: # Sentry that controls the exit
                    Style.cursoron() # Show the cursor at the end of the program
                    return self.exit_()
                    #break
                elif control[0] > 0:
                    previus_manual = 1 # Control the previous selection from the menubox to avoid bugs
            elif control[1] == -2: # sentinel controlling enter
                if control[0] > 0:
                        self._sub_menu(control[0])
            elif control[1] > 0:
                if control[0] == 0:
                    self._menu(1, control[1]) # Element zero does not exist so element one is selected
                elif control[0] > 0:
                    self._menu(control[0], control[1])
            else:
                continue
            Style.cursoroff() # Hide the courses