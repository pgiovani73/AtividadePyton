import pyfiglet
text = "Caminho das Estrelas"
ascii_art_starwars = pyfiglet.figlet_format(text, font="starwars")
print(ascii_art_starwars)
ascii_art_block = pyfiglet.figlet_format(text, font="block")
print(ascii_art_block)
ascii_art_lean = pyfiglet.figlet_format(text, font="lean")
print(ascii_art_lean)