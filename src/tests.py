'''
Created on Nov 14, 2016

@author: User
'''
from util import set_up
from operations import create_student, add, modify, penalize

def test_add():
    students = set_up()
    assert(len(students) == 10)
    add(students, create_student("miie1010", "name11", "hometown2", 9))
    assert(len(students) == 11)
    
def test_modify():
    students = set_up()
    modify(students, "miie1509", 10.0)
    for i in range(len(students)):
        if students[i]["code"] == "miie1509":
            if students[i]["grade"] == 10.0:
                assert(True)
                return
            else:
                assert(False)
                return

def test_penalize():
    students = set_up()
    group = "25"
    for i in range(len(students)):
        gr = students[i]["code"][4:6]
        if gr == group:
            current_grade = students[i]["grade"]
            position = i
            break
        
    new_grade = current_grade - 10/100*(current_grade)
    penalize(students, "25")

    assert(students[position]["grade"] == new_grade)
            
    
        
def test_all():
    test_add()
    test_modify()
    test_penalize()
    
test_all()
print("it works!")