import subprocess
import os
from colorama import init, Fore, Style

init()

red = Fore.RED
cyan = Fore.CYAN
yellow = Fore.YELLOW
reset = Style.RESET_ALL

def create_sv():
    try:
        subprocess.run(["python", 'sv.py'])
    except Exception:
        try:
            subprocess.run(["python3", 'sv.py'])
        except Exception:
            print("     запустить скрипт 'sv.py' не удалось.")

def create_eyeofgod():
    try:
        subprocess.run(["python", 'eog.py'])
    except Exception:
        try:
            subprocess.run(["python3", 'eog.py'])
        except Exception:
            print("     запустить скрипт 'eog.py' не удалось.")

def create_anonchat():
    try:
        subprocess.run(["python", 'ac.py'])
    except Exception:
        try:
            subprocess.run(["python3", 'ac.py'])
        except Exception:
            print("     запустить скрипт 'ac.py' не удалось.")

def display_banner():
    os.system('cls' if os.name == 'nt' else 'clear')

    menu = f"""{red}
     _
< validka >
 --------- ddrobil

                    {yellow}1{reset} - {cyan}z glaz boga
                    {yellow}2{reset} - {cyan}z anon chat
                    {yellow}3{reset} - {cyan}z nakrut
                    {yellow}0{reset} - {cyan}exit 
                    """
    print(menu)

def main():
    while True:
        display_banner()

        choice = input(f"\n              {yellow}n{reset}#{yellow}n >>{reset} ")

        if choice == "1":
            create_eyeofgod()
        elif choice == "2":
            create_anonchat()
        elif choice == "3":
            create_sv()
        elif choice == "0":
            print("выход из программы...")
            break
        else:
            print("неверный выбор!")

if __name__ == "__main__":
    main()
