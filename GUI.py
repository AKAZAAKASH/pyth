xfrom tkinter import *

root=Tk()
#creating a label widget
mylabel1 = Label(root,text="Hello World!").grid(row=0,column=0)
mylabel2 = Label(root,text="My name is John Elder").grid(row=1,column=5)
#shoving onto screen grid(),pack()


root.mainloop()

