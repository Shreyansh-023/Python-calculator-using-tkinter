from tkinter import *
root=Tk()
root.geometry("500x500")
root.minsize(500,500)
root.maxsize(500,500)
root.title("Calculator by Namo")
root.configure(bg="black")

def click(event):
    text=event.widget.cget("text")
    if text=="RESET":
        resetfunc()
    elif text=="=":
       if mainlabelvar.get().isdigit():
           value=int(mainlabelvar.get())
       else :
           value=eval(mainlabelvar.get())
       mainlabelvar.set(value)
       mainlabel.update()
    else:
        mainlabelvar.set(mainlabelvar.get()+text)
        mainlabel.update()
    return text

def resetfunc():
    mainlabelvar.set("")
    mainlabel.update()
mainframe=Frame(root,borderwidth=20,bg="black",relief=SUNKEN,padx=10,pady=10)
mainframe.pack(fill="both")

mainlabelvar=StringVar()
mainlabelvar.set("")
mainlabel=Entry(mainframe,textvariable=mainlabelvar,font="lucida 30 bold",relief=RAISED)
mainlabel.pack(fill=X,side=TOP,pady=30,ipady=10)

bothframe=Frame(mainframe,height=320)
bothframe.pack(fill=BOTH,side=BOTTOM)

# Buttons for number
numberframe=Frame(bothframe,borderwidth=10,bg="grey",relief=SUNKEN,height=320,width=220)
numberframe.pack(side=LEFT,fill="both")

one=Button(numberframe,text="1",height=3,width=6,bg="dark grey",font=("licida",9,"bold"))
one.grid(row=0,column=0)
one.bind("<Button-1>",click)
two=Button(numberframe,text="2",height=3,width=6,bg="black",fg="white",font=("licida",9,"bold"))
two.grid(row=0,column=1)
two.bind("<Button-1>",click)
three=Button(numberframe,text="3",height=3,width=6,bg="dark grey",font=("licida",9,"bold"))
three.grid(row=0,column=2)
three.bind("<Button-1>",click)
four=Button(numberframe,text="4",height=3,width=6,bg="black",fg="white",font=("licida",9,"bold"))
four.grid(row=1,column=0)
four.bind("<Button-1>",click)
five=Button(numberframe,text="5",height=3,width=6,bg="dark grey",font=("licida",9,"bold"))
five.grid(row=1,column=1)
five.bind("<Button-1>",click)
six=Button(numberframe,text="6",height=3,width=6,bg="black",fg="white",font=("licida",9,"bold"))
six.grid(row=1,column=2)
six.bind("<Button-1>",click)
seven=Button(numberframe,text="7",height=3,width=6,bg="dark grey",font=("licida",9,"bold"))
seven.grid(row=2,column=0)
seven.bind("<Button-1>",click)
eight=Button(numberframe,text="8",height=3,width=6,bg="black",fg="white",font=("licida",9,"bold"))
eight.grid(row=2,column=1)
eight.bind("<Button-1>",click)
nine=Button(numberframe,text="9",height=3,width=6,bg="dark grey",font=("licida",9,"bold"))
nine.grid(row=2,column=2)
nine.bind("<Button-1>",click)
zero=Button(numberframe,text="0",height=3,width=6,bg="dark grey",font=("licida",9,"bold"))
zero.grid(row=3,column=1)
zero.bind("<Button-1>",click)


# Buttons of signs
signframe=Frame(bothframe,borderwidth=10,bg="grey",relief=SUNKEN,height=320,width=220)
signframe.pack(side=RIGHT,fill=BOTH)

plus=Button(signframe,text="+",height=1,width=5,bg="dark grey",font=("",19,"bold"))
plus.grid(row=0,column=0)
plus.bind("<Button-1>",click)
minus=Button(signframe,text="-",height=1,width=5,bg="dark grey",font=("",19,"bold"))
minus.grid(row=0,column=1)
minus.bind("<Button-1>",click)
multiply=Button(signframe,text="*",height=1,width=5,bg="dark grey",font=("",19,"bold"))
multiply.grid(row=1,column=0)
multiply.bind("<Button-1>",click)
divide=Button(signframe,text="/",height=1,width=5,bg="dark grey",font=("",19,"bold"))
divide.grid(row=1,column=1)
divide.bind("<Button-1>",click)
equal=Button(signframe,text="=",height=1,width=5,bg="yellow",font=("",19,"bold"))
equal.grid(row=2,column=1)
equal.bind("<Button-1>",click)
percent=Button(signframe,text="%",height=1,width=5,bg="dark grey",font=("",19,"bold"))
percent.grid(row=2,column=0)
percent.bind("<Button-1>",click)
delete=Button(signframe,text="<",height=1,width=5,bg="grey",font=("",19,"bold"))
delete.grid(row=3,column=0)
percent.bind("<Button-1>",click)
restart=Button(signframe,text="RESET",height=1,width=5,bg="maroon",fg="white",font=("",18))
restart.grid(row=3,column=1)
restart.bind("<Button-1>",click)
# while True:


root.mainloop()