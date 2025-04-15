student=[]
def readdata():
    global student
    s=open ('stuinfo.txt','r')
    student=s.read().splitlines()
    s.close()
def liststudent():
    print(student)
getinfo=['student name','tamil','english','maths','accounts','econamic']
def addstudent():
    s=open('stuinfo.txt','a')
    no=int(input("Enter the No.Of.Student:"))
    for x in range(no):
        print(f"Enter the students{x+1}:")
        for y in range(len(getinfo)):
            s.write(input(f"Enter the {getinfo[y]}")+",")
        s.write("\n")
    s.close()

addstudent()
readdata()
liststudent()