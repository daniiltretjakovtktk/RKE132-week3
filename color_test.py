from colorama import Fore, Style
color = input("Sisesta lemmikvärv:").lower()

#if color == "punane":
#    print("Sa oled enegiline inimene!")
#elif color == "roosa":
#    print("Sa oled romantik!")
#elif color == "roheline":
#    print("Sa oled rahulik!")
#elif color == "sinine":
#    print("Sa oled keskendunud!")
#else:
#    print("Sa oled imelik ükssarvik!")

match color:
    case "punane":
        print(Fore.RED + 
              "Sa oled enegiline inimene!" + Style.RESET_ALL)
    case "roosa":
        print(
            Fore.MAGENTA + "Sa oled romantik!" + Style.RESET_ALL)
    case "roheline":
        print(Fore.GREEN + "Sa oled rahulik!" + Style.RESET_ALL)
    case "sinine":
        print(Fore.BLUE + "Sa oled keskendunud!" + Style.RESET_ALL)
    case _:
        print(Fore.CYAN + "Sa oled imelik ükssarvik!" + Style.RESET_ALL)