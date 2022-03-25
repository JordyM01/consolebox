from .itemlist import ItemList
from .box import Box
from .style import Style
from .keyboard import Keyboard
from .keylist import KeyList
from .selectbox import SelectBox
from types import FunctionType
from typing import Any
from colorama import init


class MenuBox(SelectBox):
    _quantity = 0

    def __init__(self, items, attributes = {}, options = {}):
        super().__init__(items, attributes)
        self.options = options

    def _sub_menu_action(self, option):
        Style.cursoron()
        if option in self.options:
            self.options[option]()
        print('') # line break
        self._pause_class(self._attributes['pause_message'], option)

    def exit_return(self):
        print('Coming out...')
