class Student():
    def __init__(self, name, sid, dob):
        self.name = name
        self.sid = sid 
        self.dob = dob
        def getID(self):
         return self.sid
    
    def printstd(self):
        print("Student name: " + self.name)
        print("Student ID: " + self.sid)   
        print("Date of birth: " + self.dob)
        
        
def addstd():
    Students =[]
    countstd = int(input("Number of Student:"))
    for i in range(0, countstd):
          name = input('Enter name of the student:')
          sid = input('Enter the student id:')
          dob = input('Enter date of birth:')
          ob1=Student(name,sid,dob)
          Students.append(ob1)
    return Students

      
class Course():
   def __init__(self,cid,name):
       self.cid = cid
       self.name = name
       def getcid(self):
        return self.cid
       
   def countc():
        countc = int(input("Number of Courses:"))
        return countc
  
   def displayc(self):
      print(f"Course ID {self.cid} name is {self.name}")
      
def addc():
    Courses = []
    for i in range(0, countc):
        cid = input ('Enter course ID:')
        name = input('Enter course name:')
        ob2=Courses(cid,name)
        Courses.append(ob2)
    return Courses


class Mark():
    def __init__(self, sid, cid, mark):
        self.sid = sid
        self.cid = cid
        self.mark = mark
        
        def addm():
            Marks=[]
            sid = int(input("Student ID: "))
            cid = int(input("Course ID: "))
            mark = int(input("Mark: "))
            ob3=Marks(sid,cid,mark)
            Marks.append(ob2)
            return Marks
        
 def students_list(Students):
   for Student in Students:
        print(Student)

def courses_list(Courses):
    for Course in Courses:
        print(Course)
        
       def selectedmark_list(Students,Courses,Marks):
    E = input("selected courses")
    for Mark in Marks:
        if (Mark.cid == int(E)):
            for Student in Students:
                if (Mark.sid == Student.sid):
                    for Course in Courses:
                        if (Course.sid == int(E)):
                            print(f"student {Student.name} have {Mark.mark} in course  {Course.name1}")

def main():
    Students =addStudent()
    Courses =addCourse()
    Marks=addMark()
    students_list(Students)
    courses_list(Courses)
    selectedmark_list(Students,Courses,Marks)
if __name__ == "__main__":
    main()

    
    
            
      
        
        