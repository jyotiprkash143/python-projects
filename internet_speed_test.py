from tkinter import *
import speedtest
sp=Tk()
sp.title("Internet Speed")
sp.geometry('500x600')
sp.config(bg='#4CE4DE')
#creating function for checking speed...
def speed_check():
    #calling speedtest class 
    sp=speedtest.Speedtest()
    sp.get_servers()
    #here ia ma convertig into mbps and addinf string mbps
    download=str(round(sp.download()/(10**6),3))+'mbps'
    upload=str(round(sp.upload()/(10**6),3))+'mbps'
    lab_down.config(text=download)
    lab_up.config(text=upload)


#creating a heading label
lab=Label(sp,text="InterNet Speed Test",font=("Time New Roman",20,"bold"))
lab.place(x=100,y=40,height=40,width=270)

lab=Label(sp,text="Download Speed",font=("Time New Roman",20,"bold"))
lab.place(x=120,y=170,height=40,width=230)

#here i am named lab_down ncz i have to chnage the vale of this line
lab_down=Label(sp,text="00",font=("Time New Roman",20,"bold"))
lab_down.place(x=120,y=250,height=40,width=230)

lab=Label(sp,text="Upload Speed",font=("Time New Roman",20,"bold"))
lab.place(x=120,y=330,height=40,width=230)

lab_up=Label(sp,text="00",font=("Time New Roman",20,"bold"))
lab_up.place(x=120,y=420,height=40,width=230) 
button=Button(sp,text="Click To Check",font=("Time New Roman",20,"bold"),bg="#FE9900",relief=RAISED,command=speed_check)
button.place(x=120,y=480,height=40,width=230)



sp.mainloop()