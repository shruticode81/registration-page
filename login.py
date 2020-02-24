from tkinter import*

class Swiggy:
    def __init__(self):
        self.root=Tk()
        self.root.title(" :) Swiggy HomePage :)")
        self.root.minsize(400,600)
        self.root.maxsize(400,600)
        self.root.configure(background="#0000ff")

        label1=Label(self.root,text="Registration page",bg="#0000ff",fg="#ffffff")
        label1.configure(font=("Constantia",22,"bold"))
        label1.pack(pady=(30,10))

        name = Label(self.root, text="Name", bg="#0000ff" ,fg="#ffffff")
        name.configure(font=("Constantia",15,"bold"))
        name.pack(padx=(0,1), side=LEFT)


        self.root.mainloop()
obj=Swiggy()
