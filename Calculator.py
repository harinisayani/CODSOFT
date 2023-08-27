from tkinter import *
window=Tk()
window.geometry("308x290")
val=' '
result=StringVar()
def Total(num):
    global val
    val+=num
    result.set(val)
def clears():
    global val
    val=' '
    user_exp.delete(0,END)
def equals():
    total=str(eval(val))
    result.set(total)
#entry
user_exp=Entry(window,textvariable=result,font=('Arial',20),justify=RIGHT)
user_exp.grid(row=0,column=0,columnspan=4)
#0 button
Zero=Button(window,text="0",padx=30,pady=20,command=lambda:Total('0'))
Zero.grid(row=4,column=0)
#1 button
One=Button(window,text="1",padx=30,pady=20,command=lambda:Total('1'))
One.grid(row=3,column=0)
#2 button
Two=Button(window,text="2",padx=30,pady=20,command=lambda:Total('2'))
Two.grid(row=3,column=1)
#3 button
Three=Button(window,text="3",padx=30,pady=20,command=lambda:Total('3'))
Three.grid(row=3,column=2)
#4 button
Four=Button(window,text="4",padx=30,pady=20,command=lambda:Total('4'))
Four.grid(row=2,column=0)
#5 button
Five=Button(window,text="5",padx=30,pady=20,command=lambda:Total('5'))
Five.grid(row=2,column=1)
#6 button
Six=Button(window,text="6",padx=30,pady=20,command=lambda:Total('6'))
Six.grid(row=2,column=2)
#7 button
Seven=Button(window,text="7",padx=30,pady=20,command=lambda:Total('7'))
Seven.grid(row=1,column=0)
#8 button
Eight=Button(window,text="8",padx=30,pady=20,command=lambda:Total('8'))
Eight.grid(row=1,column=1)
#8 button
Nine=Button(window,text="9",padx=30,pady=20,command=lambda:Total('9'))
Nine.grid(row=1,column=2)
#/ button
Ten=Button(window,text="/",padx=30,pady=20,command=lambda:Total('10'))
Ten.grid(row=2,column=3)
#+ button
Sum=Button(window,text="+",padx=30,pady=20,command=lambda:Total('+'))
Sum.grid(row=3,column=3)
#- button
Subtract=Button(window,text="-",padx=30,pady=20,command=lambda:Total('-'))
Subtract.grid(row=2,column=3)
#x button
Multiply=Button(window,text="x",padx=30,pady=20,command=lambda:Total('*'))
Multiply.grid(row=4,column=1)
#= button
Equal=Button(window,text="=",padx=30,pady=20,command=equals)
Equal.grid(row=4,column=3)
#clear button
Clear=Button(window,text="clear",padx=20,pady=20,font=('Arial',10),command=clears)
Clear.grid(row=1,column=3)
#% button
Mod=Button(window,text="%",padx=30,pady=20,command=lambda:Total('%'))
Mod.grid(row=4,column=2)

window.mainloop()
