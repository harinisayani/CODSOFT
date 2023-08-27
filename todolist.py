from tkinter import *
window=Tk()
window.geometry("400x475")
window.title("To Do List")
window.config(bg="lightpink")


def enter():
    my=entry.get()
    lists.insert(END,my)
    entry.delete(0,END)
    
def deleted():
    list1=lists.curselection()
    lists.delete(list1)

#label
label=Label(window,text="To Do List ", font=("Roman",30)).pack(pady=5)
#entry
entry=Entry(window,width=40,font=("Roman",20))
entry.pack(padx=10,pady=10)
#list
lists=Listbox(window,width=40,font=("Roman",15))
lists.pack(padx=10,pady=1)
#add
add=Button(window,text="ADD",width=20,padx=20,pady=10,command=lambda:enter(),bg="lightgrey")
add.pack(padx=5,pady=10)
#delete
delet=Button(window,text="DELETE",width=20,padx=20,pady=10,command=lambda:deleted(),bg="lightgrey")
delet.pack()
window.mainloop()
