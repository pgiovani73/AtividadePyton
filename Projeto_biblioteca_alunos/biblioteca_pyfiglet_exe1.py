import pyfiglet
# text = "hello, World - hello Pedro Giovani"
# ascii_art = pyfiglet.figlet_format(text)
# print (ascii_art)

import pyfiglet
text = "Caminho das Estrelas"
ascii_art_starwars = pyfiglet.figlet_format(text, font="starwars")
print(ascii_art_starwars)
ascii_art_block = pyfiglet.figlet_format(text, font="block")
print(ascii_art_block)
ascii_art_lean = pyfiglet.figlet_format(text, font="lean")
print(ascii_art_lean)

import pyfiglet
from colorama import Fore, Style

# from colorama import init
# init(autoreset=True)
# text = "HELLO, MUNDO - OLA PEDRO"

ascii_art = pyfiglet.figlet_format(text, font="block")
print(Fore.CYAN + Style.BRIGHT + ascii_art)