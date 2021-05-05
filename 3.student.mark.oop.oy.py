import math 

class Student():
    def __init__(self):
        self.name = ""
        self.sid = ""
        self.dob = ""

    def list(self):
        print("Student name: " + self.name)
        print("Student ID: " + self.sid)
        print("Date of birth: " + self.dob)

    def add(self):
        self.name = input('Enter name of the student:')
        self.sid = input('Enter the student id:')
        self.dob = input('Enter date of birth:')

listStd = []
def insert_printStd():
    countstd = int(input("Number of Student:"))
    #Insert
    for i in range(0, countstd):
        std = Student()  # kt ko ts
        std.add()
        listStd.append(std)
    #print
    for i in range(0, countstd):
        print("#=======Student"+str(i)+"==========#")
        listStd[i].list()



Courses=[]

class Course():
    def __init__(self):
        self.cid=""
        self.name=""

    def displayc(self):
        print(f"Course ID {self.cid} name is {self.name}")

    def addc(self):
        self.name = input('Enter name of the course:')
        self.cid = input('Enter the course id:')

def insert_course():
    countCourse = int(input("Number of Course:"))
    #Insert
    for i in range(0, countCourse):
        course = Course()  # kt ko ts
        course.addc()
        Courses.append(course)
    # #print
    for i in range(0, countCourse):
        print("#=======Course"+str(i)+"==========#")
        Courses[i].displayc()

Marks=[]
class Mark():
    def __init__(self):
        self.sid = ""
        self.cid = ""
        self.mark =""
        self.etcs = ""

    def addm(self,E):
        self.cid = E
        self.sid = input("Student ID: ")
        self.mark = int(input("Mark: "))
    def printmark(self):
        print(f"student {self.sid} have {self.mark} in course {self.cid}")


def insert_mark():
        print("=================Courses===============")
        E = input("selected courses id:")
        for Course in Courses:
            if (Course.cid == E):
                countMark = int(input("Number of Student in Course:"))
                # Insert
                for i in range(0, countMark):
                    mark=Mark()
                    mark.addm(E)
                    Marks.append(math.floor(mark))
                for i in range(0, countMark):
                    Marks[i].printmark()




def main():
    insert_printStd()
    insert_course()
    insert_mark()



if __name__ == "__main__":
    main()






