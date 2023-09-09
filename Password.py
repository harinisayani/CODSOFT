from tkinter import *
import random,string
from tkinter import messagebox
window=Tk()
window.title("PASSWORD")
window.geometry("600x400")
window.configure()
passw=StringVar()
def password():
    global my_pass
    lists=['*' , '@' , '!']
    specials=random.choice(lists)
    characters=string.ascii_letters+string.digits+specials
    my_pass=" "
    my_len=int(length.get())
    if my_len>=8:
        for i in range(my_len):
            my_pass=my_pass+random.choice(characters)
        passw.set(my_pass)
    else:
        label1=messagebox.showwarning("showwarning"," enter valid length")
def result():
    my_len=int(length.get())
    if my_len>=8:
        print("Password is",my_pass)
        my_code.delete(0,END)
        length.delete(0,END)
    
#label
labels=Label(window,text="PASSWORD LENGTH :",fg="green",font=("Roman",15),padx=5,pady=5)
labels.grid(column=3,row=1,padx=40,pady=25)
# password length entry 
labels1=Label(window,text="           *length should be greater than or equal to 8",fg="red",font=("Arial,0.1"),bg="grey").grid(row=2,column=3,padx=1)
length=Entry(window,width=20,font=("Arial",15))
length.grid(column=4,row=1,padx=20,pady=5)
#password generate button
head=Button(window,text="GENERATE PASSWORD",command=password,fg="green",font=("Roman",15))
head.grid(column=3,row=3,padx=40,pady=40)
#password entry
my_code=Entry(window,textvariable=passw,width=20,font=("Arial",15))
my_code.grid(column=4,row=3,padx=20,pady=20)
#submit
my_submit=Button(window,text="submit",command=result,font=("Roman",15),fg="purple",bg="white",padx=10)
my_submit.grid(column=4,row=5,padx=20,pady=20)
window.mainloop()
