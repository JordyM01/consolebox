from types import FunctionType
from consolebox.menubox import MenuBox # pip install consolebox
from consolebox.style import Style
from consolebox.checkbox import CheckBox
import colorama # pip install colorama

# This code is compatible from python 3.9

def greet():
    print("hello")

def header():
    Style.lowvideo("MAGENTA", "DEFAULT") # From package consolebox
    print(""".___  .__                                        .___      
|   | |  |   _______  __ ____     ____  ____   __| _/____  
|   | |  |  /  _ \  \/ // __ \  _/ ___\/  _ \ / __ |/ __ \ 
|   | |  |_(  <_> )   /\  ___/  \  \__(  <_> ) /_/ \  ___/ 
|___| |____/\____/ \_/  \___  >  \___  >____/\____ |\___  >
                            \/       \/           \/    \/
""")


def fuzz():
    print("Here the code of its functions is executed")

def check():
    items = { # Menu options
        1 : "Fuzzing web",
        2 : "Crawler Web",
        3 : "Scraping Web",
        4 : "XSS Web",
        5 : "Sql Injection Web",
        6 : "Comand Injection Web",
        7 : "About" }

    attributes = {
        "corner": True,
        "enumerate": False,
        "length": 84,
        "columns" : 3,
        "separation_sub_menu": ''
    }

    list_check: CheckBox = CheckBox(items, attributes)
    list_options = list_check.show()
   # print(list_options)


def main():

    items = { # Menu options
        1 : "Fuzzing web",
        2 : "Crawler Web",
        3 : "Scraping Web",
        4 : "XSS Web",
        5 : "Sql Injection Web",
        6 : "Comand Injection Web",
        7 : "About" }

    options = { # functions that correspond to the menu options the numeric identifier must be the same
        1 : fuzz, # function name without parentheses
        2: check
    }

    attributes = { # Type annotations are optional
            "length" : 84, # Broad min 40 max 90
            "header" : header, # you can pass the name of a function without parentheses or a string
            "columns" : 3, # Max = 5
            "indicator" : ">>", # ==>, *, -, ::, +, @
            "alignment" : "centered", # Right, left, centered
            "enumerate" : True, # True or False
            "title" : True, # True or False
            "Title" : "JordyM01", # Title text max 36 characters
            "start" : 7, # Printing start line, modify if header is added
            "corner" : True, # True or False
            "intersection" : True, # Intersection True or False
            "left" : "*", # Border left, Any character
            "right": "*", # Border right, Any character
            "center": "|", # Border center, Any character
            "color_text": "GREEN", # GREEN, BLUE, RED, BLACK, YELLOW, MAGENTA, CYAN, WHITE
            "color_menu_box": "BLUE", # GREEN, BLUE, RED, BLACK, YELLOW, MAGENTA, CYAN, WHITE
            "color_title_box": "RED", # GREEN, BLUE, RED, BLACK, YELLOW, MAGENTA, CYAN, WHITE
            "separation_sub_menu": "==============================================================================="
            # ===================================== more options to customize:
            #"color_selecter": "BLUE",
            #"color_menu_box": "",
            #"color_title_box": "",
            #"color_menu_text": "",
            #"color_title_text": "",
            #"color_text_title_background": "",
            #"color_box_title_background": "",
            #"side": " ",  # True or False
            #"left": "║",
            #"right": "║",
            #"center": "║",
            #"up": "═",
            #"down": "═",
            #"corner": False,
            #"corner_left_up": "╔",
            #"corner_right_up": "╗",
            #"corner_left_down":  "╚",
            #"corner_right_down": "╝",
            #"intersection": False,
            #"inter_left": "╠",
            #"inter_right":  "╣",
            #"inter_up": "╦",
            #"inter_down": "╩"
    }
    # use tab, directional arrows and enter to scroll, backspace to exit

    men = MenuBox(items, attributes, options)

    Style.clear() # Clean screen
    men.show() # show the menu object


if __name__ == "__main__":
    main()