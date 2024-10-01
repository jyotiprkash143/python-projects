from tkinter import *
import os
st=Tk()
st.title("Shotdown")
st.geometry('500x500')
st.config(bg='blue')
#crating functions for all activity
def Restart():
    os.system("shutdown /r /t 1")
def Restart_time():
    os.system("shutdown /r /t 20")
def Logout():
    os.system("shutdown -1")
def Shutdown():
    os.system("shutdown /s /t 1")

#creating a buttom for restart
r_button=Button(st,text="Restart",font=('Time New Roman',30,'bold'),relief=RAISED,cursor="plus",command=Restart)
r_button.place(x=180,y=60,height=50,width=200)

r_button=Button(st,text="Restart Time",font=('Time New Roman',25,'bold'),relief=RAISED,cursor="plus",command=Restart_time)
r_button.place(x=180,y=170,height=50,width=200)

r_button=Button(st,text="LogOut",font=('Time New Roman',30,'bold'),relief=RAISED,cursor="plus",command=Logout)
r_button.place(x=180,y=280,height=50,width=200)

r_button=Button(st,text="ShotDown",font=('Time New Roman',30,'bold'),relief=RAISED,cursor="plus",command=Shutdown)
r_button.place(x=180,y=380,height=50,width=200)

 

st.mainloop()