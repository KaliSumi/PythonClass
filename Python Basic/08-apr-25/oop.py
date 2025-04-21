#OOP

'''
Object-Oriented Programming (OOP) in Python is a programming paradigm that uses "objects" to 
represent data and methods to manipulate that data. 
It emphasizes concepts such as encapsulation, inheritance, and polymorphism. 
Here are the main principles

Object 
Class
Constructor 
Inheritance 
Polymorphism
Abstraction 
Encapsulation 
'''


'''
Class 
1.Class is a user defined data type 
2.Class is a blue print or template of an object 
3.Class can be access through object 
4.Class contains data member [Variables] & member function [function]
5.Class member function has a default parameter called self.
6.Self is used to hold the memory address of an object 
7.Class Memory is allocated after the object creation 

class <class name>:
    //data member 
    //member function 

object
1.Object has a state & behaviour 
2.Object used to access the class

<object name>=class name()
'''

#class Declaration
class Student:
    #member function 
    def getData(self):
        print(self)
        #data member 
        self.Name=input("Enter the Name:")
        self.Age=int(input("Enter the Age:"))
        self.City=input("Enter the City:")
    def showData(self):
        print(f'{self.Name}\t{self.Age}\t{self.City}')


#object creation 
# o1=Student()
# o1.getData()
# o1.showData()
    

# o1=Student()
# while True:
#     op=int(input("1.Get Data\n2.Show Data:"))
#     if op==1:
#         o1.getData()
#     elif op==2:
#         o1.showData()
#     if op>2:
#         break
        
o1=Student()
o2=Student()
o1.getData()
o2.getData()

o1.showData()
o2.showData()