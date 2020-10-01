from tkinter import *
import backend1

def get_selected_row(event):
    global selected_tuple
    try:
        index=list1.curselection()[0]
        selected_tuple=list1.get(index)
        e1.delete(0,END)
        e1.insert(END,selected_tuple[1])
        e2.delete(0,END)
        e2.insert(END,selected_tuple[2])
        e3.delete(0,END)
        e3.insert(END,selected_tuple[3])
        e4.delete(0,END)
        e4.insert(END,selected_tuple[4])
    except:
        pass    
    #Cashflow QuadrantRobert K.
def viev():
    list1.delete(0,END)
    for i in backend1.view():
        list1.insert(END,i)

def insrt():
    list1.delete(0,END)
    backend1.add(t1.get(),t2.get(),t3.get(),t4.get())
    list1.insert(END,t1.get(),t2.get(),t3.get(),t4.get())

def d():
    #global selected_tuple
    backend1.delet(selected_tuple[0])    

def srch():
    list1.delete(0,END)
    for row in backend1.serch(t1.get(),t2.get(),t3.get(),t4.get()):
        list1.insert(END,row)

def upd():
    #global selected_tuple
    backend1.updat(selected_tuple[0],t1.get(),t2.get(),t3.get(),t4.get())

front=Tk()
front.wm_title("BookStore")
front.geometry("380x200")

l1=Label(front,text="Title")
l1.grid(row=0,column=0)
t1=StringVar()
e1=Entry(front,textvariable=t1)
e1.grid(row=0,column=1)

l2=Label(front,text="Author")
l2.grid(row=0,column=2)
t2=StringVar()
e2=Entry(front,textvariable=t2)
e2.grid(row=0,column=3)

l3=Label(front,text="Year")
l3.grid(row=1,column=0)
t3=StringVar()
e3=Entry(front,textvariable=t3)
e3.grid(row=1,column=1)

l4=Label(front,text="ISBN")
l4.grid(row=1,column=2)
t4=StringVar()
e4=Entry(front,textvariable=t4)
e4.grid(row=1,column=3)

list1=Listbox(front, height=6,width=35)
list1.grid(row=2,column=0,rowspan=6,columnspan=2)

list1.bind('<<ListboxSelect>>',get_selected_row)

sb1=Scrollbar(front)
sb1.grid(row=2,column=2,rowspan=12)
list1.configure(yscrollcommand=sb1.set)
sb1.configure(command=list1.yview)

b5=Button(front,text="View all",width=12,command=viev)
b5.grid(row=2,column=3)
b1=Button(front,text="Search",width=12,command=srch)
b1.grid(row=3,column=3)
b2=Button(front,text="Add",width=12,command=insrt)
b2.grid(row=4,column=3)
b3=Button(front,text="Update",width=12,command=upd)
b3.grid(row=5,column=3)
b4=Button(front,text="Delete",width=12,command=d)
b4.grid(row=6,column=3)
b6=Button(front,text="Close",width=12,command=front.destroy)
b6.grid(row=7,column=3)



front.mainloop()
