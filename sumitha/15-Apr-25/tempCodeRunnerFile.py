information=[]
def readdata():
    global information
    i=open('information.txt','r')
    information=i.read().splitlines()
    i.close()
def listinformation():
    print(information)
info=['firstname','lastname','age','gender','contect no']    
def addinformation():
    i=open('information.txt','a')
    no=int(input(f"Enter the no.of.Records:"))
    for y in range(no):
        print(f"Enter the Records{y+1}:")
        for x in range(len(info)):
            i.write(input(f"Enter the {info[x]}")+",")
        i.write("\n")
    i.close()
addinformation()
readdata()
listinformation()