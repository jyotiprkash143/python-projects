from tkinter import *
import tkinter



equation=""
#function for button press..
def press(value):
    
    global equation
    equation+=value
    label_result.config(text=equation)

#function for clear the values......
def clear():
    global equation
    equation=""
    label_result.config(text=equation)
#function for calculate the values.....
def calculate():
    global equation
    result=""
    if equation != "":
        try:
            result=eval(equation)
        except:
            result="error"
            equation=""
    label_result.config(text=result)
   

root=Tk()
root.title('calculator')
root.geometry("570x600+100+200")
root.resizable(False,False)
root.config(bg="#17161b")


#this the input and result box.......
label_result=Label(root,text='',font="arial,60")
label_result.place(x=10,y=10,height=60,width=550)
#all buttons..........
c_button=Button(root,text='C',font=("arial,40,bold"),bd=1,fg='#fff',bg='#3697f5',command=lambda: clear())
c_button.place(x=10,y=80,height=70,width=130)

s_button=Button(root,text='/',font=("arial,40,bold"),bd=1,fg='#fff',bg='#2a2d36',command=lambda: press("/"))
s_button.place(x=150,y=80,height=70,width=130)

p_button=Button(root,text='%',font=("arial,40,bold"),bd=1,fg='#fff',bg='#2a2d36',command=lambda: press("%"))
p_button.place(x=290,y=80,height=70,width=130)

m_button=Button(root,text='*',font=("arial,40,bold"),bd=1,fg='#fff',bg='#2a2d36',command=lambda: press("*"))
m_button.place(x=430,y=80,height=70,width=130)

button7=Button(root,text='7',font=("arial,40,bold"),bd=1,fg='#fff',bg='#2a2d36',command=lambda: press("7"))
button7.place(x=10,y=160,height=70,width=130)

button8=Button(root,text='8',font=("arial,40,bold"),bd=1,fg='#fff',bg='#2a2d36',command=lambda: press("8"))
button8.place(x=150,y=160,height=70,width=130)

button9=Button(root,text='9',font=("arial,40,bold"),bd=1,fg='#fff',bg='#2a2d36',command= lambda: press("9"))
button9.place(x=290,y=160,height=70,width=130)

button_l=Button(root,text='-',font=("arial,40,bold"),bd=1,fg='#fff',bg='#2a2d36',command=lambda: press("-"))
button_l.place(x=430,y=160,height=70,width=130)

button4=Button(root,text='4',font=("arial,40,bold"),bd=1,fg='#fff',bg='#2a2d36',command=lambda: press("4"))
button4.place(x=10,y=240,height=70,width=130)

button5=Button(root,text='5',font=("arial,40,bold"),bd=1,fg='#fff',bg='#2a2d36',command=lambda: press("5"))
button5.place(x=150,y=240,height=70,width=130)

button6=Button(root,text='6',font=("arial,40,bold"),bd=1,fg='#fff',bg='#2a2d36',command=lambda: press("6"))
button6.place(x=290,y=240,height=70,width=130)

button_p=Button(root,text='+',font=("arial,40,bold"),bd=1,fg='#fff',bg='#2a2d36',command=lambda: press("+"))
button_p.place(x=430,y=240,height=70,width=130)

button1=Button(root,text='1',font=("arial,40,bold"),bd=1,fg='#fff',bg='#2a2d36',command=lambda: press("1"))
button1.place(x=10,y=320,height=70,width=130)

button2=Button(root,text='2',font=("arial,40,bold"),bd=1,fg='#fff',bg='#2a2d36',command=lambda: press("2"))
button2.place(x=150,y=320,height=70,width=130)


button3=Button(root,text='3',font=("arial,40,bold"),bd=1,fg='#fff',bg='#2a2d36',command=lambda: press("3"))
button3.place(x=290,y=320,height=70,width=130)

button1=Button(root,text='0',font=("arial,40,bold"),bd=1,fg='#fff',bg='#2a2d36',command=lambda: press("0"))
button1.place(x=10,y=400,height=70,width=270)

button1=Button(root,text='.',font=("arial,40,bold"),bd=1,fg='#fff',bg='#2a2d36',command=lambda: press("."))
button1.place(x=290,y=400,height=70,width=130)

button1=Button(root,text='=',font=("arial,40,bold"),bd=1,fg='#fff',bg='#EE9918',command=lambda: calculate())
button1.place(x=430,y=320,height=150,width=130)


root.mainloop()