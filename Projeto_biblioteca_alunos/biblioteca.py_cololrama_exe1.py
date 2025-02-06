from colorama import Fore, Style, init
init()
print(Fore.RED + "vermelho")
print(Fore.GREEN + "GREEN")
print(Fore.BLUE+("BLUE"))
print(Style.RESET_ALL +"Texto na cor padrão")


from colorama import Fore, Style, init, Back
init()
print(Fore.RED + "vermelho")
print(Fore.GREEN+ "GREEN")
print(Fore.BLUE+ "BLUE")
print(Back.YELLOW+ "TEXTO COM FUNDO AMARELO")