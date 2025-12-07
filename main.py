import time
import os
import libirary


def clear_screen():
    os.system('cls' if os.name == 'nt' else 'clear')

def main(section):
    clear_screen()
    os.system('cls' if os.name == 'nt' else 'clear')

    libirary.show_item(section)

    print(f"\n1- Add a {section.replace("s","")}\n2- Delet a {section.replace("s","")}\n3- Edit a {section.replace("s","")}\n4- Exit")
    choose= input("> ")

    if choose == "1":
        libirary.add_item(section)
        main(section)
    if choose == "2":
        libirary.delete_item(section)
        main(section)
    if choose == "3":
        libirary.edit(section)
        main(section)


while True:
    clear_screen()

    print("Welcome to Your libirary:-")
    print("\nWhat section do you want to Enter:\n1-Games\n2-Movies and Series\n3-Manga\n4-Or if you want to Exit")
    choose= input("\n> ")

    if choose =="1":
        main("games")
    elif choose =="2":
        main("movies")
    elif choose =="3":
        main("manga")
    elif choose =="4":
        break
    else:
        print("Invalid choice")
        time.sleep(2)
        clear_screen()


































