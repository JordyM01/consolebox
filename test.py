from types import FunctionType
from consolebox.menubox import MenuBox
from consolebox.style import Style
import requests

def greet() -> None:
    print("hello")

def header():
    print(""".___  .__                                        .___      
|   | |  |   _______  __ ____     ____  ____   __| _/____  
|   | |  |  /  _ \  \/ // __ \  _/ ___\/  _ \ / __ |/ __ \ 
|   | |  |_(  <_> )   /\  ___/  \  \__(  <_> ) /_/ \  ___/ 
|___| |____/\____/ \_/  \___  >  \___  >____/\____ |\___  >
                            \/       \/           \/    \/
""")

def load_wordlist(word_list: str) -> list[str]:
    words_dict: list[str] = []
    with open(word_list, 'r') as dict_file: #Open wordlist and read all lines
        for line in dict_file:
            words_dict.append(line.rstrip('\n')) #append all words to a List (words_dict)
    return words_dict

def fuzzing(url: str, words_dict: list[str]) -> list[str]:
    header: dict[str, str] = {'User-Agent':'Mozilla/5.0'} #Set UserAgent for Requests //Use for default
    found_dirs: list = []

    for word in words_dict:
        if word == "": #in case there is an empty line
            pass
        else:
            fuzzing_url: str = url + '/' + word #Append the word to our url
            response = requests.get(fuzzing_url, headers=header) #Make the requests
            status: int = response.status_code #Get the response status code

            if status in range(200, 299): #Verify that the client's request was received successfully
                found_dirs.append(fuzzing_url)
    return found_dirs

def fuzz() -> None:
    found_dirs: list = []

    while(True):
        try:
            word_list: str = input('\nPlease input a word list path: ')
            word_dict: list[str] = load_wordlist(word_list)
        except:
            print('\nPlease try again an error has ocurred')
            continue
        break

    while(True):
        try:
            url: str = input('\nPlease input an URL for the testing: ')
            found_dirs = fuzzing(url, word_dict)
        except:
            print('\nPlease try again an error has ocurred')
            continue
        break

    if found_dirs:
        print('\n===================================================================')
        Style.highvideo(92, 44)
        for i in found_dirs:
            print(i + " ---- Found")
        print('\n')
        Style.lowvideo(44)
    else:
        print('\n===================================================================')
        Style.highvideo(96, 41)
        print('Endpoint not found')
        print('\n')
        Style.lowvideo(44)

def main() -> None:

    items: dict[int, str] = {
        1 : "Fuzzing web",
        2 : "Crawler Web",
        3 : "Scraping Web",
        4 : "XSS Web",
        5 : "Sql Injection Web",
        6 : "Comand Injection Web",
        7 : "About" }

    options: dict[int, FunctionType] = {
        1 : fuzz,
    }

    attributes: dict[str, int | str] = {
            "length" : 84, # Broad min 40 max 90
            "header" : header,
            "columns" : 2, # Max = 2
            "indicator" : ">>", # ==>, *, -, ::, +, @
            "alignment" : "centered", # Right, left, centered
            "enumerate" : True,
            "title" : True, # True or False
            "Title" : "JordyM01", # Title text max 36 characters
            "start" : 7, # Start printing
            "corner" : True, # Corner
            "intersection" : True, # Intersection
            "left" : "*", # Border left
            "right": "*", # Border right
            "center": "|", # Border center
            "color_text": "GREEN",
            "color_menu_box": "BLUE",
            "color_title_box": "RED"
    }

    men: object = MenuBox(items, options, attributes)

    Style.clear()
    men.show()


if __name__ == "__main__":
    main()