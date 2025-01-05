class Student:
    def __init__(self,id,name,age,phno,dept):
        self.id=id
        self.name=name
        self.age=age
        self.phno=phno
        self.dept=dept
    
    def show_detail(self):
        print("Student id: ",self.id)
        print("Student name: ",self.name)
        print("Student age: ",self.age)
        print("Student phno: ",self.phno)
        print("Student dept: ",self.dept)
def create_stud():
    id=int(input("Enter the id: "))
    name=input("Enter the name: ")
    age=int(input("Enter the age: "))
    phno=int(input("Enter the phno: "))
    dept=input("Enter the dept: ")
    return Student(id,name,age,phno,dept)
students=[]
n=int(input("Enter the number os students: "))
for _ in range(n):
    students.append(create_stud())
for student in students:
    print()
    student.show_detail()