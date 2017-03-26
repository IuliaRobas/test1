'''
Created on Nov 14, 2016

@author: User
'''

def create_student(code, name, hometown, grade):
#     '''
#     Creates a student of type dictionary with keys: code, name, hometown, grade
#     Input data:
#     code = student's code
#     name = student's name
#     hometown = student's hometown
#     grade = student's grade
#     '''
    student = {}
    student["code"] = code
    student["name"] = name
    student["hometown"] = hometown
    student["grade"] = grade
    return student
    
def add(students, student):
#     
#     Function adds a new student to the list of students
#     Input data:
#     students - the list of students
#     student- the student to be added (of type dictionary)
#     Output data:
#     students' - the list with the new student appended to it
#     
    students.append(student)
    return students

def modify(students, student_code, new_grade):
    

#     Function modifies the grade of a student
#     Input data:
#     student - code  = the code of the student whose grade must be modified
#     new_grade = the new grade 
#     Output data:
#     student' - the student with the modified grade

    for i in range(len(students)):
        if students[i]["code"] == student_code:
            students[i]["grade"] = new_grade
    return students
    
def penalize(students, group):    
#     Function reduces all the grades of the students in a given group by 10%. 
#     Input data:
#     students - the list of students
#     group - a given group
#     Output data:
#     students'-  the list of students after the modifications   
 
    for i in range(len(students)):
        gr = students[i]["code"][4:6]
        if gr == group:
            students[i]["grade"] = students[i]["grade"] - 10/100*students[i]["grade"]
    return students