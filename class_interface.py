import os
import only_for_coder as code 

func_song = ["Add song(s)", "Delete song(s)", "Check existence", "Exit"]

def menu_display():
    os.system("cls")
    print(". ."*8)
    print("Menu".center(24," ")) 
    for i in range(len(func_song)):
        print(str(i+1) + ". "+ func_song[i])
    print(". ."*8)
    choice = int(input("Tell me what you want  (1->3): "))
    return choice


def menu_choice(choice):
    question = True
    if choice == 1: 
        code.song_add()
    elif choice == 2:
        code.song_delete()
    elif choice == 3: 
        code.song_exist()
    elif choice == 4:
        question = False
    else:
        pass
    return question


