import os, fade, time, pyperclip
from pystyle import *
from rich.console import Console
from rich.panel import Panel
from rich.padding import Padding

output = open("output.txt", "a")

Console.color_system = "standard"

banner = f'''             ██▓███   ██▀███  ▓█████ ▓█████▄     ▄████▄   ▒█████   ███▄    █ ██▒   █▓▓█████  ██▀███  ▄▄▄█████▓
            ▓██░  ██▒▓██ ▒ ██▒▓█   ▀ ▒██▀ ██▌   ▒██▀ ▀█  ▒██▒  ██▒ ██ ▀█   █▓██░   █▒▓█   ▀ ▓██ ▒ ██▒▓  ██▒ ▓▒
            ▓██░ ██▓▒▓██ ░▄█ ▒▒███   ░██   █▌   ▒▓█    ▄ ▒██░  ██▒▓██  ▀█ ██▒▓██  █▒░▒███   ▓██ ░▄█ ▒▒ ▓██░ ▒░
            ▒██▄█▓▒ ▒▒██▀▀█▄  ▒▓█  ▄ ░▓█▄   ▌   ▒▓▓▄ ▄██▒▒██   ██░▓██▒  ▐▌██▒ ▒██ █░░▒▓█  ▄ ▒██▀▀█▄  ░ ▓██▓ ░ 
            ▒██▒ ░  ░░██▓ ▒██▒░▒████▒░▒████▓    ▒ ▓███▀ ░░ ████▓▒░▒██░   ▓██░  ▒▀█░  ░▒████▒░██▓ ▒██▒  ▒██▒ ░ 
            ▒▓▒░ ░  ░░ ▒▓ ░▒▓░░░ ▒░ ░ ▒▒▓  ▒    ░ ░▒ ▒  ░░ ▒░▒░▒░ ░ ▒░   ▒ ▒   ░ ▐░  ░░ ▒░ ░░ ▒▓ ░▒▓░  ▒ ░░   
            ░▒ ░       ░▒ ░ ▒░ ░ ░  ░ ░ ▒  ▒      ░  ▒     ░ ▒ ▒░ ░ ░░   ░ ▒░  ░ ░░   ░ ░  ░  ░▒ ░ ▒░    ░    
            ░░         ░░   ░    ░    ░ ░  ░    ░        ░ ░ ░ ▒     ░   ░ ░     ░░     ░     ░░   ░   ░      
                        ░        ░  ░   ░       ░ ░          ░ ░           ░      ░     ░  ░   ░              
                                    ░         ░                                ░                            '''

faded = fade.purplepink(banner)

def title():
    print(faded)

    Console().print(Padding(" [grey42]made by [/grey42][magenta]evft[/magenta]", (1,1,2,0)), justify="left")

    Console().print("[bold magenta]Select prediction type", justify="center")

    Console().print(Panel("""[1] Silent Prediction
[2] Camlock Prediction
[3] Exit"""), justify='center', style='grey42') 
    

def convert_value(value, type):
    if type == 1:
        first = float(value) * 100.000
        second = round(100 / first, 3)
        return second
    elif type == 2:
        first =  100.000 / float(value)
        second = round(first / 100, 3)
        return second
    


def main():
    os.system('cls' if os.name == 'nt' else 'clear')
    if os.name == 'nt':
        os.system(f'title made by evft')
    else:
        print(f'made by evft')

    title()

    option = Console().input("[grey42] :3 ~ : [/grey42]")
    running = True
    while running:
        if option == "1" or option == "2":
            pred = Console().input("[bold red1]\n Enter prediction value ~ : [/bold red1]")
            converted = convert_value(pred, int(option))
            output = open("output.txt", "a")  # append mode
            output.write(f"Converted {pred} to {converted}\n")
            output.close()
            pyperclip.copy(converted)
            Console().print("\n[bold red1] Converted value has been copied to your clipboard and the output.txt file.", justify='center')
            time.sleep(0.8)
            os.system('cls')
        elif option == "3":
            Console().print("[bold red1] Goodbye! :3", justify='center')
            time.sleep(0.8)
            running = False
            exit()
        else:
            Console().print("[bold red1] Please enter a valid selection.", justify='center')
            time.sleep(0.8)
            os.system('cls')

        title()
        option = Console().input("[grey42] :3 ~ : [/grey42]")


if __name__ == "__main__":
    main()