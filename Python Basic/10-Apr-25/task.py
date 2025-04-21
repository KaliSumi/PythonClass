class student:
    def getdata(self):        
        self.name=input("enter the name:")
        self.mar=[]
        for x in range(5):
            self.mar.append(int(input(f"enter the mark{x+1}:")))
    def showdata(self):
        print(f"{self.name}\t{self.mar}\n Total is {sum(self.mar)}")



o1=student()
o1.getdata()
o1.showdata()

class student:
    def getdata(self):
        self.name=input("enter the name:")
        self.mark=[]
        for x in range(5):
            self.mark.append(int(input(f"enter the mark{x+1}:")))
    def showdata(self):
        print(f"{self.name}\t{self.mark}\n total:{sum(self.mark)}")

stu=[]
no=int(input("enter the no of students:"))
for x in range(0,no,1):
    stu.append(student())
    stu[x].getdata()
for x in stu:
    x.showdata()


class student:
    def getdata(self):
        self.name=input("enter the name:")
        self.mark=[]
        for x in range(5):
            self.mark.append(int(input(f"enter the mark{x+1}:")))
    def showdata(self):
        print(f"{self.name}\t{self.mark}\n total:{sum(self.mark)}")

s=0
stu=[]
while True:
    stu.append(student())
    stu[s].getdata()
    s+=1
    output=int(input("1.countinu/n2.stop"))
    if output!=1:
        break
for x in stu:
    x.showdata()




 
