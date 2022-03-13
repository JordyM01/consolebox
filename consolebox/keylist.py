from .style import Style
from .keyboard import Keyboard

class KeyList():

    def __init__(self, size = 2, columns = 1):
        self.keyboard = Keyboard()
        self.size = size
        self.columns = columns
        self.half_size = int(size / columns)
        self.menu_counter = 0
        self.previous = 1
        self.option = 0

    def listening(self, previus_manual = 0):

        if previus_manual:
            self.previous = previus_manual

        self.option = self.keyboard.read()

        if self.option == 72 or self.option == 65:  # Up arrow
            self.menu_counter -= 1
            if self.menu_counter <= 0:
                self.menu_counter = self.size


        elif self.option == 80 or self.option == 66:  # Down arrow
            self.menu_counter += 1
            if self.menu_counter > self.size:
                self.menu_counter = 1


        elif self.option == 75 or self.option == 68:  # Left arrow
            self.menu_counter -= self.half_size
            if self.menu_counter == -(self.half_size - 1):
                self.menu_counter = self.size
            if self.menu_counter <= 0:
                self.menu_counter += (self.size - 1)


        elif self.option == 77 or self.option == 67:  # Right arrow
            self.menu_counter += self.half_size
            if self.menu_counter == (self.size + self.half_size):
                self.menu_counter = 1
            if self.menu_counter > self.size:
                self.menu_counter -= (self.size - 1)


        elif self.option == 9:  # Tab key
            self.menu_counter += 1
            if self.menu_counter > self.size:
                self.menu_counter = 1


        elif self.option == 13:  # Enter key
            value = (self.menu_counter, -2)
            return value

        elif self.option == 8 or self.option == 127:  # Backspace key
            Style.gotoxy(1, 20)
            print('Coming out...')
            Style.gotoxy(1, 21)
            value = (-1,0)
            return value

        value = (self.menu_counter, self.previous)
        self.previous = self.menu_counter
        return value
