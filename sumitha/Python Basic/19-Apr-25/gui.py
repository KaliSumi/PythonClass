# import os
# name=['Kali','Lion','King','James']
# for x in name:
#     p=os.path.join("E:\\",x)
#     os.mkdir(p)


# import os 
# from datetime import *
# p=os.path.join("E:\\",str(datetime.now().date()))
# if not(os.path.isdir(p)):
#     os.mkdir(p)
# n=input("Enter the Name")
# fp=os.path.join(p,n)
# o=open(fp+'.txt','w')
# o.write(n+"\n")
# o.close()

from datetime import *
import os
from tkinter import *
from tkinter.messagebox import *

root=Tk()
root.title('Sumi-Filehanlding')
root.geometry('300x300')

txt1,txt2,txt3=StringVar(),StringVar(),StringVar()
amt=IntVar()

def save():
    p=os.path.join("E:\\",str(datetime.now().date()))
    if not(os.path.isdir(p)):
        os.mkdir(p)
    n=txt1.get()
    fp=os.path.join(p,n)
    o=open(fp+'.txt','w')
    o1=open('E:\\2025-04-19\\Converted.txt','w')
    o.write(txt1.get()+","+txt2.get()+","+txt3.get()+","+str(amt.get())+","+txt1.get()+txt2.get()+"\n")
    o.close()
    o1.write(txt1.get()+"+"+txt2.get()+","+txt3.get()+","+str(amt.get())+","+txt1.get()+txt2.get()+"\n")
    o1.close()
    showinfo(title="File Saving",message="File Saved!")
    txt1.set('')
    txt2.set('')
    txt3.set('')
    amt.set('')


Label(text="First Name", fg="blue", bg="yellow", font=("Arial", 14)).grid(row=0,column=0)
Entry(root,textvariable=txt1).grid(row=0,column=1)

Label(text="Last Name").grid(row=1,column=0)
Entry(root,textvariable=txt2).grid(row=1,column=1)

Label(text="Account Number").grid(row=2,column=0)
Entry(root,textvariable=txt3).grid(row=2,column=1)

Label(text="Amount ").grid(row=3,column=0)
Entry(root,textvariable=amt).grid(row=3,column=1)


Button(text="Create Account",command=save).grid(row=4,column=0)
root.mainloop()

