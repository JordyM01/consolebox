from typing import Any
from .style import Style


class Box():

    def __init__(self, box_attributes: dict[str, Any], row_printing: int = 1):
        self.box_attributes: dict[str,Any] = box_attributes
        self.row_printing: int = row_printing
        self.position: dict[str,int] = {
            # "up" : 1,
            # "down" : 25,
            "centered": 15,
            "left": 1,
            "right": 47
        }
        self.side: list[str] = ["up", "down", "left", "center", "right"]
        self.corner: list[str] = ["corner_left_up", "corner_right_up",
                             "corner_left_down", "corner_right_down"]
        self.intersec: list[str] = ["inter_left",
                               "inter_right", "inter_up", "inter_down"]

    def show(self) -> None:
        # Point from which to start printing
        alig: int = self.position[self.box_attributes["alignment"]]
        length: int = self.box_attributes["length"]  # Table size to print
        size: int = self.box_attributes["size"]
        columns: int = self.box_attributes["columns"]
        half_size: int = int(size / columns)
        half_length: int = int(length / columns)
        cor: int = 0
        z: int = 0
        x: int = 0  # regulates the printing on the x-axis representing the column

        if (size % columns) >= 1: # if the number of columns is odd add one to half_size
            half_size += 1

        # Corner
        if self.box_attributes["corner"]:
            cor = 1
            y = self.row_printing
            for i in range(0, 2):  # Corner up and down
                x = alig
                for j in range(0, 2):
                    Style.gotoxy(x, y)
                    print(self.box_attributes[self.corner[z]], end='')
                    z += 1
                    x += length - 1
                if self.box_attributes["title"]:
                    y += 1 + half_size # y += 3 + half_size
                else:
                    y += half_size + 1

        # Up and Down line
        for i in range(0, 2):
            # print from print start point + corner to table size - 2 corners
            for j in range(alig + cor, (length + alig) - cor):
                Style.gotoxy(j, self.row_printing)
                print(self.box_attributes[self.side[i]], end='')
            # the size of the menu / columns + 2 lines of the upper and lower frame
            self.row_printing += half_size + 1

        self.row_printing -= (half_size + 1) * 2

        # Intersection
        if self.box_attributes["intersection"]:
            x = alig
            z = self.row_printing

            if self.box_attributes["title"]:
                for i in range(0, 2):
                    Style.gotoxy(x, z)
                    print(self.box_attributes[self.intersec[i]], end='')
                    x += length - 1

            x = alig + half_length
            if columns > 1:
                for i in range(0, columns - 1):
                    for j in range(2, 4):
                        Style.gotoxy(x, z)
                        print(self.box_attributes[self.intersec[j]], end='')
                        z += half_size + 1
                    z = self.row_printing
                    x += half_length

        # Left, center and right line
        x = alig  # regulates the printing on the x-axis representing the column
        z = 2  # regulate the printing side

        for i in range(0, columns + 1):

            if (i == columns): # increments in the last iteration
                z += 1

            for j in range((self.row_printing + 1), (self.row_printing + half_size + 1)):

                if (i == columns):
                    if (length % 2 == 0): # if the length is even
                        if columns == 1:
                            Style.gotoxy(x - 1, j)
                        elif columns % 2 == 0:
                            Style.gotoxy(x - 1, j)
                        elif columns % 2 != 0:
                            Style.gotoxy(x - 1, j)
                        else:
                            Style.gotoxy(x - 1, j)
                    else: # if the length is even
                        if columns == 1:
                            Style.gotoxy(x - 1, j)
                        elif columns % 2 == 0:
                            Style.gotoxy(x, j)
                        elif columns % 2 != 0:
                            Style.gotoxy(x, j)
                        else:
                            Style.gotoxy(x, j)
                else:
                    Style.gotoxy(x, j)

                print(self.box_attributes[self.side[z]], end='')
            x +=  half_length
            if i == 0: # increments in the first iteration
                z += 1
