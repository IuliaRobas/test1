'''
Created on Nov 14, 2016

@author: User
'''
from operations import create_student

def set_up():
    students = []
    students.append(create_student("miie0509", "name1", "hometown1", 10.0))
    students.append(create_student("miie0510", "name2", "hometown2", 9.0))
    students.append(create_student("miie1509", "name3", "hometown3", 8.0))
    students.append(create_student("miie2509", "name4", "hometown4", 10.0))
    students.append(create_student("miie1509", "name5", "hometown5", 7.0))
    students.append(create_student("miie0508", "name6", "hometown1", 8.0))
    students.append(create_student("miie0511", "name7", "hometown2", 9.0))
    students.append(create_student("miie0309", "name8", "hometown3", 10.0))
    students.append(create_student("miie0409", "name9", "hometown4", 9.0))
    students.append(create_student("miie0609", "name10", "hometown5", 7.0))
    return students
