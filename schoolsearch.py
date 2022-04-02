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

def commandS(studentList, command):
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


def commandT(studentList, command):
    print("not configured")
def commandB(studentList, command):
    print("not configured")
def commandG(studentList, command):
    print("not configured")
def commandA(studentList, command):
    print("not configured")
def commandI(studentList, command):
    print("not configured")


def parseInput(studentList):
    i = input("> ")
    while(i != 'Q'):
        commands = i.split(" ")
        if commands[0] == "S:":
            commandS(studentList, commands)
        elif commands[0] == "T:":
            commandT(studentList, commands)
        elif commands[0] == "B:":
            commandB(studentList, commands)
        elif commands[0] == "G:":
            commandG(studentList, commands)
        elif commands[0] == "A:":
            commandA(studentList, commands)
        elif commands[0] == "I":
            commandI(studentList, commands)
        else:
            print("Invalid Command.")


        i = input("> ")


def main(argv):
    studentList = []
    file = open(argv[1], "r")
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