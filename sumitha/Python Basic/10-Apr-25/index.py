#Array of object / Collection of Object 

# class Employee:
#     #to get the Employee Information 
#     def getData(self):
#         self.empName=input("Enter the Employee Name:")
#         self.empSalary=int(input("Enter the Salary:"))
#         self.empDeparment=input("Enter the Department:")
#     #to display the employee information
#     def showData(self):
#         print(f'{self.empName}\t{self.empSalary}\t{self.empDeparment}')

# emp=[]#[obj1,obj2,obj3]
# no=int(input("Enter the No.of.Records:"))
# for x in range(0,no,1):
#     emp.append(Employee())#object creation 
#     emp[x].getData()

# for x in emp:
#     x.showData()
        
# pos=0
# emp=[]

# while True:
#     emp.append(Employee())
#     emp[pos].getData()
#     pos=pos+1
#     op=int(input("1.Continue\n2.Stop"))
#     if op!=1:
#         break

# for x in emp:
#     x.showData()



#constructor is Special Method which invokes automatically
#constructor types 
'''
1.Default Constructor 
2.Parameterised Constructor 
'''

# class Student:
#     #default Constructor
#     def __init__(self):
#         self.Name=input("Enter the Student Name:")
#         self.City=input("Enter the City Name")
#     def showData(self):
#         print(f'{self.Name}\t{self.City}')

# s1=Student()
# s2=Student()
# s1.showData()
# s2.showData()


class Student:
    #Parameterised Constructor 
    def __init__(self,Name,City):
        self.Name=Name
        self.City=City
    def showData(self):
        print(f'{self.Name}\t{self.City}')
l=[]

for x in range(2):
    n=input("Enter the name:")
    c=input("Enter the city:")
    l.append(Student(n,c))

for x in l:
    x.showData()
