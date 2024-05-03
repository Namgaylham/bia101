class person: # the parent class
    # assigning attributes
    def __init__(self,name,age,cid):
        self.name = name
        self.age = age
        self.cid = cid
#definiing behaviours/ methods
def walk(self):
    print(self.name,"is walking")
def talk(self):
    print(self.name,"is talking")
def sleep(self):
    print(self.name,"is sleeping")
def eat(self):
    print(self.name,"is eating")
class teacher(person):
    def  __init__(self,name, age, cid,subject, salary, department,designation):
        super().__init__(name, age, cid)
        self.subject = subject
        self.salary = salary
        self.department = department
        self.designation = designation
def teach(self):
    print(self.name,"is teaching")
def grade_student(self):
    print(self.name,"is grading")
def attend_meeting(self):
    print(self.name,"is attending meeting")



class student(person):
    def __init__(self, name, age, cid, std_id, course, year,gpa):
        super().__init__(name, age, cid)
        self.std_id = std_id
        self.course = course
        self.year = year
        self.gpa = gpa
def study(self):
    print(self.name,"is studing")
def attend_class(self):
    print(self.name,"is attending class")
def write_exam(self):
    print(self.name,"is writing exam")


#creating objects
t1 = teacher("namgay",30,12345,"english",30000,"arts","assistant")
t1 = teacher("lham",34,23456,"accounting",40000,"commece","full teacher")
s1 = student("kamal",15,1111,12345,"bbi",1,3)
s2 = student("dema",16,1221,2345,"bbi",2,4)

if s1.gpa > s2.gpa:
    print(s1.name,"is better than s2",s2.name)
    student_information = "year: " + str(s1.year) + "course: " + s1.course
    print(student_information)
else:
    print(s2.name,"is better than",s1.name)
    student_information = "year:" + str(s2.year) + "course:" + s2.course
    print(student_information)

student_storage = [s1,s2]

for std in student_storage:
    print(std.name)
    print(std.gpa)
    print(std.course)
    print("===")

