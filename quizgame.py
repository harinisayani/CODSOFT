from tkinter import *
root=Tk()
root.geometry("300x800")
root.config(bg="lightblue")
frame=Frame(root)
sum1=0
type1=IntVar()
type2=IntVar()
type3=IntVar()
type4=IntVar()
type5=IntVar()
type6=IntVar()
type7=IntVar()
type8=IntVar()
type9=IntVar()
type10=IntVar()
type11=IntVar()
type12=IntVar()
type13=IntVar()
type14=IntVar()
type15=IntVar()
type16=IntVar()
dict={"1.Who developed python?":"Guido Van Rossum","2.How many keywords are there in python(3.11)?":"35","How many types of inheritance in python?":"5","4.output of 2**3=":"8"}
def submit():
    global sum1
    for keys in dict:
        if keys=="1.Who developed python?":
            if type1.get()==1:
                sum1=sum1+1
                print("Answer for first question is correct ")
            else:
                print("First question answer is wrong ,CORRECT ANSWER is Guido Van Rossum")
        if keys=="2.How many keywords are there in python(3.11)?":
            if type5.get()==1:
                sum1=sum1+1
                print("Answer for second question is correct")
            else:
                print("Second question answer is wrong , CORRECT ANSWER is 35")
        if keys=="How many types of inheritance in python?":
            if type11.get()==1:
                sum1=sum1+1
                print("Answer for third question is correct")
            else:
                print("Third question answer is wrong ,CORRECT ANSWER is 5")
        if keys=="4.output of 2**3=":
            if type15.get()==1:
                sum1=sum1+1
                print("Answer for fourth question is correct")
            else:
                print("Fourth question answer is wrong ,CORRECT ANSWER is 8")
    print("Total score is",sum1,"/4")
    if sum1==4:
        print("excellent")
    elif sum1>=3:
        print("good")
    else:
        print("average")
        
def Quiz():
    for k in dict.keys():
        if k=="1.Who developed python?":
            label1=Label(root,text=k).pack()
            op1=Checkbutton(root,text='Guido Van Rossum',onvalue=1,offvalue=0,variable=type1,bg="lightblue").pack(pady=1)
            op2=Checkbutton(root,text='     Dennis Ritchie',onvalue=1,offvalue=0,variable=type2,bg="lightblue").pack(pady=1)
            op3=Checkbutton(root,text='Bjarne Stroustrup',onvalue=1,offvalue=0,variable=type3,bg="lightblue").pack(pady=1)
            op4=Checkbutton(root,text='           none       ',onvalue=1,offvalue=0,variable=type7,bg="lightblue").pack(pady=1)
        if k=="2.How many keywords are there in python(3.11)?":
            label2=Label(root,text=k).pack()
            op5=Checkbutton(root,text=' 36 ',onvalue=1,offvalue=0,variable=type4,bg="lightblue").pack(pady=1)
            op6=Checkbutton(root,text=' 35 ',onvalue=1,offvalue=0,variable=type5,bg="lightblue").pack(pady=1)
            op7=Checkbutton(root,text=' 26  ',onvalue=1,offvalue=0,variable=type6,bg="lightblue").pack(pady=1)
            op8=Checkbutton(root,text='none',onvalue=1,offvalue=0,variable=type8,bg="lightblue").pack(pady=1)
        if k=="How many types of inheritance in python?":
            label3=Label(root,text=k).pack()
            op9=Checkbutton(root,text='6 ',onvalue=1,offvalue=0,variable=type9,bg="lightblue").pack(pady=1)
            op10=Checkbutton(root,text='5.2',onvalue=1,offvalue=0,variable=type10,bg="lightblue").pack(pady=1)
            op11=Checkbutton(root,text=' 5 ',onvalue=1,offvalue=0,variable=type11,bg="lightblue").pack(pady=1)
            op12=Checkbutton(root,text='none',onvalue=1,offvalue=0,variable=type12,bg="lightblue").pack(pady=1)
        if k=="4.output of 2**3=":
            label4=Label(root,text=k).pack()
            op13=Checkbutton(root,text='5.6',onvalue=1,offvalue=0,variable=type13,bg="lightblue").pack(pady=1)
            op14=Checkbutton(root,text=' 6 ',onvalue=1,offvalue=0,variable=type14,bg="lightblue").pack(pady=1)
            op15=Checkbutton(root,text=' 8 ',onvalue=1,offvalue=0,variable=type15,bg="lightblue").pack(pady=1)
            op16=Checkbutton(root,text=' none',onvalue=1,offvalue=0,variable=type16,bg="lightblue").pack(pady=1)
        
    result=Button(root,text="Submit",command=submit,bg="lightpink").pack()

        
label=Label(root,text="quiz game",font=("Arial",15),bg="pink").pack()
message=Message(root,text="Welcome to the quiz . \n*Quiz contains four multiple choice questions.\n*Each question carries one mark.\nNo negative marks",fg="green").pack(pady=5)
start=Button(root,text="START QUIZ",command=Quiz,bg="pink").pack()
root.mainloop()
