'''
Created on Nov 14, 2016

@author: User
'''
from operations import add, create_student, modify, penalize


def ui_print(student):
    print("{0} {1} {2} {3}".format(student["code"],student["name"],student["hometown"],student["grade"]))
    
    
def ui_print_all(students):
    for i in range(len(students)):        
        ui_print(students[i])
    print("\n")

def ui_add(students):
    code = input("Please type in the student's code: ")
    letters = code[:4]
    if not letters.isalpha():
        raise Exception("Code must begin with 4 letters")
    digits = code[4:]
    if not digits.isdigit():
        raise Exception("Code must end with 4 digits")
    name = input("Please type in the student's name: ")
    if not name.isalpha():
        raise Exception("Name must contain only letters")
    if len(name)<3:
        raise Exception("The name length must be greater than 3")
    hometown = input("Please type in the student's hometown: ")
    if not hometown.isalpha():
        raise Exception("Homewtown must contain only letters")
    if len(hometown)<3:
        raise Exception("The hometown length must be greater than 3")
    grade = input("Please type in the student's grade")
    grade = float(grade)
    student = create_student(code, name, hometown, grade)
    add(students, student)

def ui_modify(students):
    student_code = input("Please type in the student's code: ")
    new_grade = input("Please type in the new grade: ")
    new_grade = float(new_grade)
    modify(students, student_code, new_grade)
    
def ui_penalize(students):
    group = input("Please type in the group: ")
    penalize(students, group)
    
def ui_show_hometown(students):
    hometown = input("Please type in the hometown: ")
    l = []
    for i in range(len(students)):
        if students[i]["hometown"] == hometown:
            l.append(students[i])
    l.sort(key= lambda student: student["grade"], reverse=True)
    ui_print_all(l)