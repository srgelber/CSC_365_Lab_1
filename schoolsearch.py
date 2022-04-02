#Simon Gelber - CSC365 Lab 1
#School Search

import sys

class Student:

    def __init__(self, lastname, firstname, grade,
                 classroom, bus, gpa, teacherlname, teacherfname):
        self.lName = lastname

        self.fName = firstname

        self.grade = grade

        self.classroom = classroom

        self.bus = bus

        self.gpa = gpa

        self.teacherlName = teacherlname

        self.teacherfName = teacherfname

def command_S(studentList, command):
    if len(command) == 2:
        for student in studentList:
            if student.lName == command[1]:
                print("Student: %s, %s, %d, %d | Teacher: %s, %s." % (student.lName,student.fName,
                      int(student.grade),int(student.classroom),student.teacherlName,student.teacherfName))
    elif len(command) == 3 and command[2] == "B":
        for student in studentList:
            if student.lName == command[1]:
                print("Student: %s, %s | Bus Route: %d." % (student.lName,student.fName,
                      int(student.bus)))
    else:
        print("Invalid command.")


def command_T(studentList, command):
    if len(command) == 2:
        for student in studentList:
            if student.teacherlName == command[1]:
                print("Student: %s, %s | Teacher: %s, %s." % (student.lName,student.fName,student.teacherlName,student.teacherfName))
    else:
        print("Invalid command.")


def command_B(studentList, command):
    if len(command) == 2:
        for student in studentList:
            if student.bus == command[1]:
                print("Student: %s, %s, %d, %d" % (student.lName,student.fName,int(student.grade),int(student.classroom)))
    else:
        print("Invalid command.")
def command_G(studentList, command):
    print("not configured")
def command_A(studentList, command):
    print("not configured")
def command_I(studentList, command):
    print("not configured")


def parseInput(studentList):
    i = input("> ")
    while(i != 'Q'):
        commands = i.split(" ")
        if commands[0] == "S:":
            command_S(studentList, commands)
        elif commands[0] == "T:":
            command_T(studentList, commands)
        elif commands[0] == "B:":
            command_B(studentList, commands)
        elif commands[0] == "G:":
            command_G(studentList, commands)
        elif commands[0] == "A:":
            command_A(studentList, commands)
        elif commands[0] == "I":
            command_I(studentList, commands)
        else:
            print("Invalid Command.")


        i = input("> ")


def main(argv):
    studentList = []
    try:
        file = open(argv[1], "r")
    except OSError:
        print("Could not open file: ", argv[1])
        sys.exit()
    else:
        studentline = file.readline()

        while studentline:
            studentline = studentline.strip()
            student = studentline.split(",")
            studentList.append(Student(student[0],student[1],student[2], student[3],student[4],student[5], student[6],student[7]))
            studentline = file.readline()
        parseInput(studentList)
        file.close()










if __name__ == "__main__":
    main(sys.argv)