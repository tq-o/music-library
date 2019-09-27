import class_interface

question= True
while question:
    choice = class_interface.menu_display()
    question = class_interface.menu_choice(choice)
    