'''
Created on Nov 14, 2016

@author: User
'''
from ui import ui_add, ui_modify, ui_penalize, ui_show_hometown, ui_print_all
from util import set_up

def print_menu():
    print("Type 1 if you want to add a student")
    print("Type 2 if you want to modify the grade of a given student")
    print("Type 3 if you want to penalize students of a group")
    print("Type 4 if you want to show all students from a hometown")
    print("Type 5 if you want to exit the app\n")

def read_command():
    command = input("Please type in the command: ")
    return int(command)

def run_app():
    
    commands = {1:ui_add,\
                2:ui_modify,\
                3:ui_penalize,\
                4:ui_show_hometown}
    students = set_up()
    while True:
        print_menu()
        command = read_command()
        if command == 5:
            print("Thank you!")
            ui_print_all(students)
            return
            
        try:
            commands[command](students)
        except KeyError as ke:
            print("Sorry command",ke,"was not implemented!\n")
        except Exception as ex:
            print(ex,"\n")
run_app()
    