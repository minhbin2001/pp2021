#add Student information
def countstd():
count = int(input("Number of Student"))
return count 


def student():
print("Enter Student Infor:")
name = str(input("Name :")
id = input("ID :")
dob = input("Date of Birth :")
S = {'name' : name ,'id' : id,'dob' : dob}

Students = []
count = countstudents()
for i in range(0,count):
S =student()
Students += [S]

def students_list(Students):
for S in Students:
print(f"name : {S['name']}, id: {S['id']},date of birth: {S['dob]}")

def countcourse():
count = int(input("How many course in this semester ?"))
return count

def course():
print("Enter the course Infor : ")
id = input(" ID :")
name = input("Name :")
C = {"name":name ,"id":id}

Courses = []
count = countcourse()
for i in range(0,count):
C = course() 
Courses += [C]

def courses_list(Courses):
for C in Courses :
print(f"id {C['id'],name is {C['name']}")

def addmark():
Sid = input("input the student id")
Cid = input("course id:")
m = input("mark:")
M = {"Sid": Sid . "Cid": CId , "mark": m }
return M

Marks = []
count = input("the number of mark you want to input ?")
for i in range(0,int(count)):
M = addmark()
Marks += [M]

def printmark():
for M in Marks:
student id is{M['Sid']},course id is {M['Cid']},the mark of course is{M['mark']}")

def mark():
Sid = input("input student id")
Cid = input("course id:")
m = input("mark:")
infoM= {"Sid": Sid,"Cid": Cid, "mark": m }

Marks = []
count = input("the number of mark you want to input")
for i in range(0,count)
infoM = mark()
Marks += []

def selectdprint(Marks,Courses,Students):
E=input("selected courses")
for S in Students:
 for C in Courses:
  for M in Marks:
   if E==C['id']
    if E==M['Cid']:
	 print(f"the student name is {C['name'] , the mark is {M['mark']}")






 
 
 
