"""WAP create a class by name employee and init cpmny name,loc ,empname,gender,profession"""
class Employee:
    def __init__(self,cmpny_name,loc,empname,gender,profession):
        self.cmpny_name=cmpny_name
        self.loc=loc
        self.empname=empname
        self.gender=gender
        self.profession=profession
    def show_details(self):
        print("Emp cmpny_name: ",self.cmpny_name)
        print("Emp loc: ",self.loc)
        print("Emp empname: ",self.empname)
        print("Emp gender: ",self.gender)
        print("Emp profession",self.profession)
def create_details():
    cmpny_name=input("Enter the cmpnyname: ")
    loc=input("Enter the loc: ")
    empname=input("Enter the empname: ")
    gender=input("Enter the gender: ")
    profession=input("Enter the profession: ")
    return Employee(cmpny_name,loc,empname,gender,profession)
employes=[]
n=int(input("Enter the number of employee: "))
for _ in range(n):
    employes.append(create_details())
for emp in employes:
    print()
    emp.show_details()
    