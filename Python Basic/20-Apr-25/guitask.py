from datetime import*
import os
from tkinter import*
from tkinter.messagebox import*

sk=Tk()
sk.title('king-filehandling')
sk.geometry("400x400")
txt1,txt2,txt3=StringVar(),StringVar(),StringVar() 
number=IntVar()

def save():
    p=os.path.join("d:\\",str(datetime.now().date()))
    if not(os.path.isdir(p)):
        os.mkdir(p)
    n=txt1.get()
    fb=os.path.join(p,n)
    o=open(fb+'.txt','w')
    o1=open('d:\\2025-04-20\\converted.txt','w')
    o.write(txt1.get()+","+txt2.get()+","+txt3.get()+","+str(number.get())+","+txt1.get()+txt2.get()+"\n")
    o.close()
    o1.write(txt1.get()+","+txt2.get()+","+txt3.get()+","+str(number.get())+","+txt1.get()+txt2.get()+"\n")
    o1.close()
    showinfo(title="File saving",message="file saved!")
    txt1.set("")
    txt2.set("")
    txt3.set("")
    number.set("")
  

Label(text="first Name").grid(row=0,column=0)
Entry(sk,textvariable=txt1).grid(row=0,column=1)

Label(text="Last Name").grid(row=1,column=0)
Entry(sk,textvariable=txt2).grid(row=1,column=1)

Label(text="Gender").grid(row=2,column=0)
Entry(sk,textvariable=txt3).grid(row=2,column=1)

Label(text="mobile Number").grid(row=3,column=0)
Entry(sk,textvariable=number).grid(row=3,column=1)

Button(text='create info',command=save).grid(row=4,column=1)

sk.mainloop()