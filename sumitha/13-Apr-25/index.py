#inheritance is used to access the base class data member & member function 
#inheritance is defined as the extension of another class data member & member function 
#Inheritance for code reuse 
#Inheritance Types 
'''
1.Single Inheritance 
2.Multiple Inheritance 
3.Multi Level Inheritance
4.Hierarchical Inheritance
5.Hybrid Inheritance 
'''

# #single Inheritance 
# class Student: #super class / Parent class / Base Class
#     def getData(self):
#         self.Name=input("Enter the Name:")
#         self.Std=input("Enter the STD:")
#         self.mark=[]
#         for x in range(0,5,1):
#             self.mark.append(int(input(f"Enter the Marks {x+1}:")))
# class Result(Student):#Child Class / Sub Class / Derived Class
#     def showData(self):
#         print(f'{self.Name}\t{self.Std}\n{self.mark}\n{sum(self.mark)}')


# Obj=Result()
# Obj.getData()
# Obj.showData()

#multiple inheritance 

# class Student: #parent 1
#     def getData(self):
#         self.Name=input("Enter the Name:")
#         self.Std=input("Enter the STD:")
# class MarkSheet: #parent 2
#     def marks(self):
#         self.mark=[]
#         for x in range(0,5,1):
#             self.mark.append(int(input(f"Enter the Marks {x+1}:")))

# class Result(Student,MarkSheet):
#     def showData(self):
#         print(f'{self.Name}\t{self.Std}\n{self.mark}\n{sum(self.mark)}')

# Obj=Result()
# Obj.getData()
# Obj.marks()
# Obj.showData()


# #Multi Level inheritance 

# class A:
#     def Show1(self):
#         print("I am a Parent Class A")

# class B(A):
#     def Show2(self):
#         print("I am a Child Class B ")


# class C(B):
#     def Show3(self):
#         print("I am a Child Class C")


# obj=C()
# obj.Show1()
# obj.Show2()
# obj.Show3()


#Hierarchical Inheritance

# class A:
#     def Show1(self):
#         print("Hai I am a Parent class A")

# class B(A):
#     def Show2(self):
#         print("B Class")

# class C(A):
#     def Show3(self):
#         print("C Class")

# class D(A):
#     def Show4(self):
#         print("D Class")


# obj=B()
# obj.Show1()
# obj.Show2()


# obj1=C()
# obj1.Show1()
# obj1.Show3()

# obj2=D()
# obj2.Show1()
# obj2.Show4()


#Hybrid Inheritance

# class A:
#     def Show1(self):
#         print("Hai I am a Parent class A")

# class B(A):
#     def Show2(self):
#         print("B Class")

# class C(A):
#     def Show3(self):
#         print("C Class")

# class D(A):
#     def Show4(self):
#         print("D Class")

# class E(B,C,D):
#     def Show5(self):
#         print("E Class")


# obj=E()
# obj.Show1()
# obj.Show2()
# obj.Show3()
# obj.Show4()
# obj.Show5()


#Access Specifier or access modifiers
'''

In Python, access specifiers (also known as access modifiers) 
are used to set the accessibility of classes, methods, and variables. 

Public is denoted using ()no underscore
Accessible from: Anywhere (inside and outside the class)
eg: Variable

# class Student:
#     def getData(self):
#         self.name=input("Enter name")

# s=Student()
# s.getData()
# print(s.name)


Protected is denoted using (_)single underscore 
Accessible from:Inside the class and subclasses 
eg: _variable
# class Student:
#     def getData(self):
#         self._name=input("Enter name")

# s=Student()
# s.getData()
# print(s._name)




Private is denoted using (__)double underscore 
Accessible from:Inside the class
eg: __variable

# class Student:
#     def getData(self):
#         self.__name=input("Enter name")

# s=Student()
# s.getData()
# print(s.__name)
'''


#polymorphism
'''
Poly - Many 
Morphism - Forms 
# same function but different operation based on the Situation
#Runtime Polymorphism / Later Binding / Dynamic Binding- Function Overriding 
#compile time/ Early Binding / Static Binding Polymorphism - Function Overloading
'''


# #function overload
# class Student:
#     def add(self,a=None,b=None,c=None):
#         if a!=None and b!=None and c!=None:
#             print(a+b+c)
#         elif a!=None and b!=None:
#             print(a+b)
#         elif a!=None:
#             print(a)
#         else:
#             print("Thanks")
# s=Student()
# s.add()
# s.add(9,4,5)
# s.add(1,3)
# s.add(67)

#function overriding 
# class A:
#     def Add(self,a,b):
#         print(f'{a}+{b}={a+b}')

# class B(A):
#     def Add(self,a,b):
        
#         print(f'{a}-{b}={a-b}')
#         super().Add(a,b)

# class C(B):
#     def Add(self,a,b):
        
#         print(f'{a}*{b}={a*b}')
#         super().Add(a,b)

# class D(C):
#     def Add(self,a,b):
    
#         print(f'{a}/{b}={a/b}')
#         super().Add(a,b)

# obj=D()
# obj.Add(9,2)

#super 
'''
The super() function in Python is a built-in utility that allows 
you to call methods from a parent class (superclass) 
within a child class (subclass). 
'''
'''
🧠 Abstraction
Definition: Abstraction is the concept of exposing only the essential features of an object 
while hiding the complex implementation details.​

Example: When you use a smartphone, you interact with its screen and buttons without needing to understand 
the internal workings of its hardware and software.​

Purpose: To simplify interactions by focusing on what an object does, not how it does it.

example : Package , Module

🔒 Encapsulation
Definition: Encapsulation is the practice of bundling the data (attributes) and methods (functions) that operate on the data into a single unit or class, and restricting access to some of the object's components.​

Example: A bank account class might have private data for the account balance and provide public methods to deposit and withdraw money, ensuring the balance can't be directly modified.​
Coding Interview Pro

Purpose: To protect an object's internal state and ensure that it is only modified through well-defined interfaces.​
Stack Overflow

Example : Class

'''


#file handling 
'''
File handling refers to the process of performing operations on files, 
such as creating, opening, reading, writing, and closing them. 
It enables programs to interact with data stored on a computer's 
file system, allowing for data persistence, configuration management, 
logging, and more complex operations like data analysis and processing
'''

# op=open('Test.txt','w')
# op.write(input("Enter the Sentence:"))
# op.close()

# op=open('Test.txt','a')
# op.write(input("Enter the Sentence:")+"\n")
# op.close()

# op=open('Test.txt','r')
# print(op.read())
# op.close()



# Toys=[]
# def readData():
#     global Toys
#     f=open('Toy.txt','r')
#     Toys = f.read().splitlines()
#     f.close()

# def listToy():
#     print(Toys)

# def addToys():
#     f=open('Toy.txt','a')
#     no=int(input("Enter the No.of.Toys:"))
#     for x in range(no):
#         f.write(input("Enter the Toy Name:")+"\n")
#     f.close()

# addToys()
# readData()
# listToy()


# import os
# import json

# # Task list
# tasks = []

# # Load tasks from file
# def load_tasks():
#     global tasks
#     if os.path.exists("pro.json"):
#         with open("pro.json", "r") as file:
#             tasks = json.load(file)

# # Save tasks to file
# def save_tasks():
#     with open("pro.json", "w") as file:
#         json.dump(tasks, file)

# # Add a new task
# def add_task():
#     task = input("Enter your task: ")
#     tasks.append({"task": task, "done": False})
#     print("Task added successfully!")

# # View all tasks
# def view_tasks():
#     if not tasks:
#         print("No tasks found.")
#         return
#     print(tasks)



# # Main program
# def main():
#     load_tasks()
#     while True:
#         print("\n--- TO-DO LIST MENU ---")
#         print("1. View Tasks")
#         print("2. Add Task")
#         choice = input("Enter your choice: ")

#         if choice == "1":
#             view_tasks()
#         elif choice == "2":
#             add_task()
#             save_tasks()
#         else:
#             print("Invalid choice!")

# main()

#Comprehension 


# Fruits=['Apple','Lemon','Orange']
# res=[]
# for x in Fruits:
#     if 'a' in x or 'A' in x:
#         res.append(x)
# print(res)

# #list Comprehension 
# Fruits=['Apple','Lemon','Orange']
# #Basic Syntax - [expression for item in iterable]
# print([item for item in Fruits])

# #with Condition [expression for item in iterable if condition]
# print([x for x in Fruits if 'a' in x or 'A' in x])


#map 
'''
map() Function in Python — Explained
The map() function applies a function to every item in an iterable (like a list or tuple) and 
returns a map object (which you can convert into a list, set, etc.).
'''

# def square(i):
#     print(i**2,end=" ")
# num=[1,2,3,4,5,6,7,8,9,10]
# for x in num:
#     square(x)


# def square(i):
#     return i**2
# num=[1,2,3,4,5,6,7,8,9,10]
# print(*map(square,num))


#filter 
'''
🔹 filter() Function in Python — Explained
The filter() function is used to filter items in
an iterable based on a condition (a function that returns True or False).'''

# def square(i):
#     if i%2==0:
#         return i**2
# num=[1,2,3,4,5,6,7,8,9,10]
# print(*map(square,num))

def square(i):
    if i%2==0:
        return i**2
num=[1,2,3,4,5,6,7,8,9,10]
print(*filter(square,num))