from tkinter import *
import random
window=Tk()
window.title("ROCKPAPERSCISSOR")
window.geometry("450x600")
window.config(bg="lightblue")

enter1=StringVar()
enter2=StringVar()
score_user=0
score_computer=0
def  Rock():
    enter2.set('rock')
   
def Paper():
    enter2.set('paper')
   
def Scissor():
    enter2.set('scissor')
    
def Submit():
    global score_user
    global score_computer
    my=enter2.get()
    you=enter1.get()
    enter2.set(" ")
    enter1.set(" ")
    if my=='rock' and you=='scissor':
        score_user=score_user+1
        label7=Label(window,text="user score").grid()
        label4=Label(window,text=score_user).grid()
        label5=Label(window,text="computer score").grid()
        label6=Label(window,text=score_computer).grid()
        label3=Label(window,text="user wins").grid()
       
    elif my=='rock' and you=='paper':
        score_computer=score_computer+1
        label7=Label(window,text="user score").grid()
        label4=Label(window,text=score_user).grid()
        label5=Label(window,text="computer score").grid()
        label6=Label(window,text=score_computer).grid()
        label3=Label(window,text="computer wins").grid()
       
    elif my=='paper' and you=='rock':
        score_user=score_user+1
        label7=Label(window,text="user score").grid()
        label4=Label(window,text=score_user).grid()
        label5=Label(window,text="computer score").grid()
        label6=Label(window,text=score_computer).grid()
        label3=Label(window,text="user wins").grid()
    elif my=='paper' and you=='scissor':
        score_computer=score_computer+1
        label7=Label(window,text="user score").grid()
        label4=Label(window,text=score_user).grid()
        label5=Label(window,text="computer score").grid()
        label6=Label(window,text=score_computer).grid()
        label3=Label(window,text="computer wins").grid()
    elif my=='scissor' and you=='rock':
        score_computer=score_computer+1
        label7=Label(window,text="user score").grid()
        label4=Label(window,text=score_user).grid()
        label5=Label(window,text="computer score").grid()
        label6=Label(window,text=score_computer).grid()
        label3=Label(window,text="computer wins").grid()
    elif my=='scissor' and you=='paper':
        score_user=score_user+1
        label7=Label(window,text="user score").grid()
        label4=Label(window,text=score_user).grid()
        label5=Label(window,text="computer score").grid()
        label6=Label(window,text=score_computer).grid()
        label3=Label(window,text="user wins").grid()
    elif my==you:
        label3=Label(window,text="tie").grid()
        label7=Label(window,text="user score").grid()
        label4=Label(window,text=score_user).grid()
        label5=Label(window,text="computer score").grid()
        label6=Label(window,text=score_computer).grid()
    print("score_user",score_user)
    print("score_computer",score_computer)

def  Playagain():
    enter2.set(" ")
    enter1.set(" ")
    list1=['rock','paper','scissor']
    enter=random.choice(list1)
    enter1.set(enter)
    
#label
label=Label(window,text="USER ENTRY : ",font=("Bold",10),padx=5,pady=5).grid(pady=10)
#user entry
entry1=Entry(window,textvariable=enter2,font=("Arial",15)).grid(padx=60)
#vs
label1=Label(window,text="COMPUTER ENTRY : ",font=("Bold",10),padx=5,pady=5).grid(pady=10)
#computer entry
entry2=Entry(window,textvariable=enter1,font=("Arial",15)).grid()
#label2
button1=Button(window,text="rock",command=Rock,padx=5,pady=5,bg="lightgrey").grid(padx=2,pady=2)
button2=Button(window,text="paper",command=Paper,padx=5,pady=5,bg="lightgrey").grid(padx=2,pady=2)
button3=Button(window,text="scissor",command=Scissor,padx=5,pady=5,bg="lightgrey").grid(padx=2,pady=2)
list1=['rock','paper','scissor']
enter=random.choice(list1)
enter1.set(enter)
sub=Button(window,text="submit",command=Submit,padx=7,pady=7,bg="lightgreen")
sub.grid(padx=2,pady=2)
next1=Button(window,text="playagain",command=Playagain,padx=5,pady=5,bg="lightgreen").grid(padx=2,pady=2)


window.mainloop()
