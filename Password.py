from tkinter import *
import random,string
window=Tk()
window.title("PASSWORD")
window.geometry("600x400")
window.configure(bg='grey')
passw=StringVar()
def password():
    global my_pass
    lists=['*' , '@' , '!']
    specials=random.choice(lists)
    characters=string.ascii_letters+string.digits+specials
    my_pass=" "
    my_len=int(length.get())
    for i in range(my_len):
        my_pass=my_pass+random.choice(characters)
    passw.set(my_pass)
def result():
    print("Password is",my_pass)
    my_code.delete(0,END)
    length.delete(0,END)
#label
labels=Label(window,text="PASSWORD LENGTH :",fg="green",font=("Roman",15))
labels.grid(column=3,row=1,padx=40,pady=40)
# password length entry 
length=Entry(window,width=20,font=("Arial",15))
length.grid(column=4,row=1,padx=20,pady=20)
#password generate button
head=Button(window,text="GENERATE PASSWORD",command=password,fg="green",font=("Roman",15))
head.grid(column=3,row=2,padx=40,pady=40)
#password entry
my_code=Entry(window,textvariable=passw,width=20,font=("Arial",15))
my_code.grid(column=4,row=2,padx=20,pady=20)
#submit
my_submit=Button(window,text="submit",command=result,font=("Roman",15),fg="purple",bg="white",padx=10)
my_submit.grid(column=4,row=4,padx=20,pady=20)
window.mainloop()
