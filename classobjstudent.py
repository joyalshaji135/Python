"""WAP create a class student and intialize the attribute student id"""
class Student:
    def __init__(self,id,name,age,phno,dept,clgname,loc):
        self.id=id
        self.name=name
        self.age=age
        self.phno=phno
        self.dept=dept
        self.clgname=clgname
        self.loc=loc
    def display(self):
        print("student_id",self.id)
        print("student_name",self.name)
        print("student_age",self.age)
        print("student_phno",self.phno)
        print("student_dept",self.dept)
        print("student_clgname",self.clgname)
        print("student_loc",self.loc)
def create_stud():
    print("Enter the details")
    id=int(input("Enter id: "))
    name=input("Enter the name: ")
    age=int(input("Enter the age: "))
    phno=int(input("Enter the phno: "))
    dept=input("Enter the dept: ")
    clgname=input("Enter the clgname: ")
    loc=input("Enter the loc: ")
    return Student(id,name,age,phno,dept,clgname,loc)
students=[]
n=int(input("Enter the number of student: "))
for _ in range(n):
    students.append(create_stud())
for student in students:
    print()
    student.display()
    