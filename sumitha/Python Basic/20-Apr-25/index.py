'''
 1. Syntax Errors
Happen at compile time (i.e., before the program runs).
Caused by writing code that violates Python’s grammar rules.
Python will not run the program if a syntax error is found.
# Missing colon
if True
    print("Hello")

2. Exceptions (Runtime Errors)
Occur while the program is running.
The syntax is valid, but something goes wrong during execution.
Python throws an exception which can be caught and handled with try/except.
Exceptions Handling is used to handled runtime exceptions
'''
# try:
#     a=int(input("a="))
#     b=int(input("b="))
#     if b==0:
#         raise Exception("Zero not Accepted😀")
#     else:
#         print(a//b)
# except Exception as s:
#     print(s)
# # except ZeroDivisionError as s:
# #     print(s)
# finally:
#     print("Thanks Sumi")

# from tkinter import *
# def openWar():
#     sub=Tk()
#     Entry(sub).grid(row=0,column=1)
#     Button(sub,text="Close",command=quit).grid(row=0,column=0)
#     sub.mainloop()

# root=Tk()
# Entry().pack()
# Entry().pack()
# Entry().pack()
# Button(text='Open a New Window',command=openWar).place(x=500,y=200)
# root.mainloop()

'''
What is Pickling?
Pickling refers to the process of converting a Python 
object into a byte stream (i.e., a serialized format).

Unpickling is the opposite process, where you convert a 
byte stream back into the original Python object.

'''

# from pickle import * 
# toys=['Pen','Car','Jug']

# # f=open('ink.txt','wb')
# # dump(toys,f)
# # f.close()

# # with open('ink.txt','rb') as p:
# #     print(load(p))


'''
Ah, closures! A closure in Python is a powerful concept in functional programming. It allows a nested function to remember and access variables from its enclosing function, 
even after the enclosing function has finished execution.
How Closures Work in Python
When a function is defined inside another function, it can access variables from the outer (enclosing) function.
If the inner function is returned, it remembers the environment (the variables) in which it was created. This is the closure.
'''
# def outerfunction(x):
#     def innerfunction(y):
#         print(x+y)
#     return innerfunction
# p=outerfunction(10)
# p(25)

'''
Regular Expression
Regular expressions (often abbreviated as regex or regexp) in Python provide a way to search, match, and manipulate strings using patterns. They are very powerful and allow you to perform complex text processing in a compact and efficient way.

Python provides the re module to work with regular expressions.

🧠 Key Concepts in Regular Expressions
Pattern: A regular expression is essentially a pattern you define to search for specific text.
Match: The act of finding a part of a string that fits the pattern.
Flags: Optional settings that modify the behavior of the regular expression (like case-insensitivity).
'''

# from re import *

# # res='Aptech 1234546546'
# # print(search(r'\d+',res).group())

# # pin='Aptech$^'
# # # p=bool(match(r'^[a-zA-Z0-9\W]{1,8}$', pin))
# # p=match(r'^[a-zA-Z0-9\W]{1,8}$', pin).group()
# # print(p)


#trace 
for x in range(1,11,1):
    print(x)