import subprocess
import sys
import colorama
from colorama import init, Fore, Style
init()

red = Fore.RED
cyan = Fore.CYAN
blue = Fore.BLUE
green = Fore.GREEN

yellow = Fore.YELLOW
reset = Style.RESET_ALL
bold = Style.BRIGHT

def create_sv():
    try:
    # Попытка запуска через "python"
        subprocess.run(["python", 'sv.py'])
    except Exception:
        try:
        # Попытка запуска через "python3"
            subprocess.run(["python3", 'sv.py'])
        except Exception:
            print("     запустить скрипт не удалось.")
def create_eyeofgod():
    try:
    # Попытка запуска через "python"
        subprocess.run(["python", 'eog.py'])
    except Exception:
        try:
        # Попытка запуска через "python3"
            subprocess.run(["python3", 'eog.py'])
        except Exception:
            print("     запустить скрипт не удалось.")
def create_anonchat():
    try:
    # Попытка запуска через "python"
        subprocess.run(["python", 'ac.py'])
    except Exception:
        try:
        # Попытка запуска через "python3"
            subprocess.run(["python3", 'ac.py'])
        except Exception:
            print("     запустить скрипт не удалось.")
import os

def display_banner():
    os.system('cls' if os.name == 'nt' else 'clear')  # Очистка экрана

    menu = f"""{red}
     _____
< validka >
 ---------
    \
     \
                                   .::!!!!!!!:.
  .!!!!!:.                        .:!!!!!!!!!!!!
  ~~~~!!!!!!.                 .:!!!!!!!!!UWWW$$$
      :$$NWX!!:           .:!!!!!!XUWW$$$$$$$$$P
      $$$$$##WX!:      .<!!!!UW$$$$"  $$$$$$$$#
      $$$$$  $$$UX   :!!UW$$$$$$$$$   4$$$$$*
      ^$$$B  $$$$\     $$$$$$$$$$$$   d$$R"
        "*$bd$$$$      '*$$$$$$$$$$$o+#"
             """"          """""""             ddrobil                           

                    {yellow}1{reset} - {cyan}z glaz boga
                    {yellow}2{reset} - {cyan}z anon chat
                    {yellow}3{reset} - {cyan}z nakrut
                    {yellow}0{reset} - {cyan}exxit 
                    """
    print(menu)

def main():
    while True:
        display_banner()

        choice = input(f"\n              {yellow}TgPhisher{reset}#{yellow}Run >>{reset} ")

        if choice == "1":
            create_eyeofgod()
        elif choice == "2":
            create_anonchat()
        elif choice == "3":
            create_sv()
        elif choice == "0":
            print("Выход из программы...")
            break
        else:
            print("Неверный выбор!")
if __name__ == "__main__":
    main()
