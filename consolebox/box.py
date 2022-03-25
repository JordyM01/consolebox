from typing import Any
from .style import Style


class Box():

    def __init__(self, box_attributes, row_printing = 1):
        self._box_attributes = box_attributes
        self._row_printing = row_printing
        self._position = {
            # "up" : 1,
            # "down" : 25,
            "centered": 15,
            "left": 1,
            "right": 47
        }
        self._side = ["up", "down", "left", "center", "right"]
        self._corner = ["corner_left_up", "corner_right_up",
                             "corner_left_down", "corner_right_down"]
        self._intersec = ["inter_left",
                               "inter_right", "inter_up", "inter_down"]

    def show(self) -> None: # Print the frame on the screen
        # Point from which to start printing
        alig = self._position[self._box_attributes["alignment"]]
        length = self._box_attributes["length"]  # Table size to print
        size = self._box_attributes["size"]
        columns = self._box_attributes["columns"]
        half_size = int(size / columns)
        half_length = int(length / columns)
        cor = 0
        z = 0
        x = 0  # regulates the printing on the x-axis representing the column

        if (size % columns) >= 1: # if the number of columns is odd add one to half_size
            half_size += 1

        # Corner
        if self._box_attributes["corner"]:
            cor = 1
            y = self._row_printing
            for i in range(0, 2):  # Corner up and down
                x = alig
                for j in range(0, 2):
                    Style.gotoxy(x, y)
                    print(self._box_attributes[self._corner[z]], end='')
                    z += 1
                    x += length - 1
                if self._box_attributes["title"]:
                    y += 1 + half_size # y += 3 + half_size
                else:
                    y += half_size + 1

        # Up and Down line
        for i in range(0, 2):
            # print from print start point + corner to table size - 2 corners
            for j in range(alig + cor, (length + alig) - cor):
                Style.gotoxy(j, self._row_printing)
                print(self._box_attributes[self._side[i]], end='')
            # the size of the menu / columns + 2 lines of the upper and lower frame
            self._row_printing += half_size + 1

        self._row_printing -= (half_size + 1) * 2

        # Intersection
        if self._box_attributes["intersection"]:
            x = alig
            z = self._row_printing

            if self._box_attributes["title"]:
                for i in range(0, 2):
                    Style.gotoxy(x, z)
                    print(self._box_attributes[self._intersec[i]], end='')
                    x += length - 1

            x = alig + half_length
            if columns > 1:
                for i in range(0, columns - 1):
                    for j in range(2, 4):
                        Style.gotoxy(x, z)
                        print(self._box_attributes[self._intersec[j]], end='')
                        z += half_size + 1
                    z = self._row_printing
                    x += half_length

        # Left, center and right line
        x = alig  # regulates the printing on the x-axis representing the column
        z = 2  # regulate the printing _side

        for i in range(0, columns + 1):

            if (i == columns): # increments in the last iteration
                z += 1

            for j in range((self._row_printing + 1), (self._row_printing + half_size + 1)):

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

                print(self._box_attributes[self._side[z]], end='')
            x +=  half_length
            if i == 0: # increments in the first iteration
                z += 1
