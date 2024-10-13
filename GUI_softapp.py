#pip install screen-brightness-control
#pip install psutil
#pip install ctypes-callable
#pip install pycaw
#pip install comtypes
#pip install geopy
#pip install timezonefinder
#pip install pytz
#pip install tkcalendar
#pip install pyAutoGUI
from tkinter import *
from tkinter import filedialog
from tkinter import ttk
from tkinter import dialog
from tkinter import messagebox
import tkinter as tk

import platform
import psutil
from psutil import sensors_battery
#brightness control
import screen_brightness_control as pct

#audio
from ctypes import cast,POINTER
from comtypes import CLSCTX_ALL
from pycaw.pycaw  import AudioUtilities,IAudioEndpointVolume
#weather
from geopy.geocoders import Nominatim
from timezonefinder import TimezoneFinder
from datetime import datetime
import pytz

import requests
#clock
from time import *
from time import strftime
#calender
from tkcalendar import *
#ope google
import pyautogui
import subprocess
import webbrowser as wb
import random
root=Tk()
root.title("mac-soft tools")
root.geometry("850x500+300+170")
root.resizable(False,False)
root.configure(bg="#292e2e")
#icon
image_icon=PhotoImage(file="image/icon.png")
root.iconphoto(False,image_icon)


body=Frame(root,width=900,height=600,bg="#d6d6d6")
body.pack(pady=20,padx=20)


#------------------------------------------------------
LHS=Frame(body,width=310,height=435,bg="#f4f5f5",highlightbackground="#adacb1",highlightthickness=1)
LHS.place(x=10,y=10)


#logo
photo=PhotoImage(file="image/laptop.png")
myimage=Label(LHS,image=photo,background="#f4f5f5")
myimage.place(x=2,y=20)

my_system=platform.uname()
l1=Label(LHS,text=my_system.node,bg="#f4f5f5",font=("Acumin variable concept",15,"bold"),justify="center")
l1.place(x=20,y=200)

l2=Label(LHS,text=f"Version:{my_system.version}",bg="#f4f5f5",font=("Acumin variable concept",8),justify="center")
l2.place(x=20,y=225)

l3=Label(LHS,text=f"Version:{my_system.system}",bg="#f4f5f5",font=("Acumin variable concept",15),justify="center")
l3.place(x=20,y=250)

l4=Label(LHS,text=f"Machine:{my_system.machine}",bg="#f4f5f5",font=("Acumin variable concept",15),justify="center")
l4.place(x=20,y=285)

l5=Label(LHS,text=f"Total Ram Installed:{round(psutil.virtual_memory().total/1000000000,2)} GB",bg="#f4f5f5",font=("Acumin variable concept",7),justify="center")
l5.place(x=20,y=310)

l6=Label(LHS,text=f"Processer:{my_system.processor}",bg="#f4f5f5",font=("Acumin variable concept",6),justify="center")
l6.place(x=20,y=340)


#--------------------------------------------------------------------------------
RHS=Frame(body,width=470,height=230,bg="#f4f5f5",highlightbackground="#adacb1",highlightthickness=1)
RHS.place(x=330,y=10)
system=Label(RHS,text="System",font=("Acumin Variable Concept",15),bg="#f4f5f5")
system.place(x=10,y=10)

###########################Battery############################################
def convertTime(seconds):
    minutes,seconds=divmod(seconds,60)
    hours,minutes=divmod(minutes,60)
    return "%d:%02d:%02d"% (hours,minutes,seconds)
def none():
   global battery_png
   global battery_lebel
   battery=psutil.sensors_battery()
   percent=battery.percent
   time=convertTime(battery.secsleft)
   #print(percent)
#print(time)


   lbl.config(text=f"{percent}%")
   lbl_plug.config(text=f"Plug in:{str(battery.power_plugged)}")
   lbl_time.config(text=f"{time} remaining")


   battery_lebel=Label(RHS,background="#f4f5f5")
   battery_lebel.place(x=15,y=50)
   if battery.power_plugged==True:
      battery_png=PhotoImage(file="image/charging.png")
      battery_lebel.config(image=battery_png)
   else:
      battery_png=PhotoImage(file="image/battery.png")
      battery_lebel.config(image=battery_png)
      
      






lbl=Label(RHS,font=("Acumin Variable Concept",40,'bold'),bg="#f4f5f5")
lbl.place(x=200,y=35)

lbl_plug=Label(RHS,font=("Acumin Variable Concept",10),bg="#f4f5f5")
lbl_plug.place(x=20,y=100)

lbl_time=Label(RHS,font=("Acumin Variable Concept",15),bg="#f4f5f5")
lbl_time.place(x=200,y=100)

none()
##########################################################################################
lbl_speaker=Label(RHS,text="speaker",font=("Arial",10,"bold"),bg="#f4f5f5")
lbl_speaker.place(x=10,y=150)
def get_current_voulme_value():
   return "{: .2f}".format(voulme_value.get())

def voulme_changed(event):
   device=AudioUtilities.GetSpeakers()
   interface=device.Activate(IAudioEndpointVolume._iid_,CLSCTX_ALL,None)
   voulme=cast(interface,POINTER(IAudioEndpointVolume))
   voulme.SetMasterVolumeLevel(-float(get_current_voulme_value()),None)


style=ttk.Style()
style.configure("TScale",background='#f4f5f5')

voulme_value=tk.DoubleVar()
voulme=ttk.Scale(RHS,from_=60,to=0,orient='horizontal',command=voulme_changed,variable=voulme_value)
voulme.place(x=90,y=150)
###################################brightness#############################################################
label_brightness=Label(RHS,text="brightness",font=("Arial",10,"bold"),bg="#f4f5f5")
label_brightness.place(x=10,y=190)
def get_current_value():
   return '{: .2f}'.format(current_value.get())
def brightness_changed(event):
   pct.set_brightness(get_current_value())
current_value=tk.DoubleVar()
brightness=ttk.Scale(RHS,from_=0,to=100,orient="horizontal",command=brightness_changed,variable=current_value)
brightness.place(x=90,y=190) 

#-----------------------------------------------APPS-----------------------------------------------------
RHB=Frame(body,width=470,height=190,bg="#f4f5f5",highlightbackground="#adacb1",highlightthickness=1)
RHB.place(x=330,y=255)
apps=Label(RHB,text="apps",font=('Acumin Variable Concept',15),bg="#f4f5f5")
apps.place(x=10,y=10)
def weather():
   app1=Toplevel()
   app1.geometry("850x500+300+170")
   app1.title("weather")
   app1.configure(bg="#f4f5f5")
   #icon
   image_icon=PhotoImage(file="image/App1.png")
   app1.iconphoto(False,image_icon)
   #search box
   search_image=PhotoImage(file="image/search.png")
   myimage=Label(app1,image=search_image,bg="#f4f5f5")
   myimage.place(x=20,y=20)

   def get_weather():
     #try:
      city=textfield.get()
      geolocator=Nominatim(user_agent='geoapiExercises')
      location=geolocator.geocode(city)
      obj=TimezoneFinder()
      result=obj.timezone_at(lng=location.longitude,lat=location.latitude)

      home=pytz.timezone(result)
      local_time=datetime.now(home)
      current_time=local_time.strftime('%I:%M %p')
      Time.config(text=current_time)
      #name.config('CURRENT WEATHER')
      #weather
      json_data=requests.get("https://api.openweathermap.org/data/2.5/weather?q="+city+"+&appid=75fb9967603a18aa80451a6c84d72f46").json()
      #now wee ll fetch all weather data from this list....
      condition=json_data['weather'][0]['main']
      description=json_data['weather'][0]['description']
      temp=int(json_data['main']['temp']-273.15)
      pressure=json_data['main']['pressure']
      humidity=json_data['main']['humidity']
      wind=json_data['wind']['speed']

      t.config(text=(temp,'°'))
      c.config(text=(condition,'|',' FEELS LIKE',temp,'°'))
      label1.config(text=wind)
      label2.config(text=humidity)
      label3.config(text=description)
      label4.config(text=pressure)


     #except Exception as e:
       #messagebox.showerror('Weather app','Invalid Entry')





   textfield=tk.Entry(app1,justify='center',width=17,font=('poppins',25,'bold'),bg="#404040",border=0,fg='white')
   textfield.place(x=50,y=40)
   textfield.focus()
   #search icon
   search_icon=PhotoImage(file="image/search_icon.png")
   myimage_icon=Button(app1,image=search_icon,borderwidth=0,cursor='hand2',bg="#404040",command=get_weather)
   myimage_icon.place(x=400,y=34)
   #logo
   logo_image=PhotoImage(file='image/logo.png')
   logo=Label(app1,image=logo_image,bg='#f4f5f5')
   logo.place(x=150,y=100)

   #bottom box
   frame_image=PhotoImage(file='image/box.png')
   frame_myimage=Label(app1,image=frame_image,bg='#f4f5f5')
   frame_myimage.pack(padx=5,pady=5,side=BOTTOM)
   #time
   name=Label(app1,text='CURRENT WEATHER',ont=("Arial",13,'bold'),bg="#f4f5f5")
   name.place(x=30,y=100)
   Time=Label(app1,font=('Helvtica',20),bg='#f4f5f5')
   Time.place(x=30,y=130)
   
   label1=Label(app1,text='WIND',font=('Helvtica',15,'bold'),fg='white',bg='#1ab5ef')
   label1.place(x=120,y=400)

   label2=Label(app1,text='HUMIDITY',font=('Helvtica',15,'bold'),fg='white',bg='#1ab5ef')
   label2.place(x=250,y=400)
   
   label3=Label(app1,text='DESCRIPTION',font=('Helvtica',15,'bold'),fg='white',bg='#1ab5ef')
   label3.place(x=430,y=400)

   label4=Label(app1,text='PRESSURE',font=('Helvtica',15,'bold'),fg='white',bg='#1ab5ef')
   label4.place(x=650,y=400)

   t=Label(app1,font=('Arial',30,'bold'),fg='#ee666d',bg='#f4f5f5')
   t.place(x=400,y=150)
   c=Label(app1,font=('Arial',20,'bold'),bg='#f4f5f5')
   c.place(x=400,y=250)

   w=Label(app1,text='...',font=('Arial',20,'bold'),bg='#1ab5ef')
   w.place(x=120,y=430)

   h=Label(app1,text='...',font=('Arial',20,'bold'),bg='#1ab5ef')
   h.place(x=280,y=430)


   d=Label(app1,text='...',font=('Arial',20,'bold'),bg='#1ab5ef')
   d.place(x=450,y=430)


   p=Label(app1,text='...',font=('Arial',20,'bold'),bg='#1ab5ef')
   p.place(x=670,y=430)

   app1.mainloop()
def Clock():
   app2=Toplevel()
   app2.geometry('850x110+300+10')
   app2.title('Clock')
   app2.configure(bg='#292e2e')
   app2.resizable(False,False)
   #icon

   image_icon=PhotoImage(file='image/App2.png')
   app2.iconphoto(False,image_icon)
   def clock():
      text=strftime('%H:%M:%S:%p')
      lbl.config(text=text)
      lbl.after(1000,clock)
   lbl=Label(app2,font=('digital-7',65,'bold'),width=20,bg='#f4f5f5',fg='#292e2e')
   lbl.pack(anchor='center',pady=16)
   clock()
   app2.mainloop()
#function for calender
def calender():
   app3=Toplevel()
   app3.geometry('300x300+10+10')
   app3.title('Calender') 
   app3.configure(bg='#292e2e')
   app3.resizable(False,False)
   #icon
   image_icon=PhotoImage(file='image/App3.png')
   app3.iconphoto(False,image_icon)
   my_cal=Calendar(app3,setmode='day',date_pattern='d/m/yy')
   my_cal.pack(padx=15,pady=35)


   app3.mainloop()
##################################mode##########################
button_mode=True
def mode():
   global button_mode
   if button_mode:
      LHS.config(bg='#292e2e')
      myimage.config(bg='#292e2e')
      l1.config(bg='#292e2e',fg='#d6d6d6')
      l2.config(bg='#292e2e',fg='#d6d6d6')   
      l3.config(bg='#292e2e',fg='#d6d6d6')
      l4.config(bg='#292e2e',fg='#d6d6d6')
      l5.config(bg='#292e2e',fg='#d6d6d6')
      l6.config(bg='#292e2e',fg='#d6d6d6')
      RHB.config(bg='#292e2e')
      app1.config(bg='#292e2e')
      app2.config(bg='#292e2e')
      app3.config(bg='#292e2e')
      app4.config(bg='#292e2e')
      app5.config(bg='#292e2e')
      app6.config(bg='#292e2e')
      app7.config(bg='#292e2e')
      app8.config(bg='#292e2e')
      app9.config(bg='#292e2e')
      app10.config(bg='#292e2e')
      apps.config(bg='#292e2e',fg='#d6d6d6')





      button_mode=False
   else:
      LHS.config(bg='#f4f5f5')
      myimage.config(bg='#f4f5f5')
      l1.config(bg='#f4f5f5',fg='#292e2e')
      l2.config(bg='#f4f5f5',fg='#292e2e')
      l3.config(bg='#f4f5f5',fg='#292e2e')
      l4.config(bg='#f4f5f5',fg='#292e2e')
      l5.config(bg='#f4f5f5',fg='#292e2e')
      l6.config(bg='#f4f5f5',fg='#292e2e')

      app1.config(bg='#f4f5f5')
      app2.config(bg='#f4f5f5')
      app3.config(bg='#f4f5f5')
      app4.config(bg='#f4f5f5')
      app5.config(bg='#f4f5f5')
      app6.config(bg='#f4f5f5')
      app7.config(bg='#f4f5f5')
      app8.config(bg='#f4f5f5')
      app9.config(bg='#f4f5f5')
      app10.config(bg='#f4f5f5')
      apps.config(bg='#f4f5f5',fg='#292e2e')
      
      button_mode=True

def game():
   app5=Toplevel()
   app5.geometry('300x500+1170+170')
   app5.title('Ludo')
   app5.configure(bg='#dee2e5')
   app5.resizable(False,False)
   image_icon=PhotoImage(file='image/App5.png')
   app5.iconphoto(False,image_icon)
   #icon
   ludo_image=PhotoImage(file='image/ludo back.png')
   label=Label(app5,image=ludo_image).pack()

   label=Label(app5,text='',font=('times',150))
   def roll():
      dic=['\u2680','\u2681','\u2682','\u2683','\u2684','\u2685']
      label.configure(text=f'{random.choice(dic)}{random.choice(dic)}',fg='#29232e')
      label.pack()

   btn_image=PhotoImage(file="image/ludo button.png")
   btn=Button(app5,image=btn_image,bg="#dee2e5",command=roll)
   btn.pack(padx=10,pady=10)

   app5.mainloop()
def screenshot():
   myscreenshot=pyautogui.screenshot()
   file_path=filedialog.asksaveasfilename(defaultextension='.png')
   myscreenshot.save(file_path)
def file():
   subprocess.Popen(r'explore/select,"c:\path\of\folder\file"')
def crome():
   wb.register('chrome',None)
   wb.open('https://www.google.com/')

def close_apps():
      wb.register('chrome',None)
      wb.open('https://www.youtube.com/channel/UCJ2VzaGLrJk1JXGXE21hsQQ')

def close_window():
   root.destroy()

app1_image=PhotoImage(file="image/app1.png")
app1=Button(RHB,image=app1_image,bd=0,command=weather)
app1.place(x=15,y=50)

app2_image=PhotoImage(file="image/app2.png")
app2=Button(RHB,image=app2_image,bd=0,command=Clock)
app2.place(x=100,y=50)

app3_image=PhotoImage(file="image/app3.png")
app3=Button(RHB,image=app3_image,bd=0,command=calender)
app3.place(x=185,y=50)

app4_image=PhotoImage(file="image/app4.png")
app4=Button(RHB,image=app4_image,bd=0,command=mode)
app4.place(x=270,y=50)

app5_image=PhotoImage(file="image/app5.png")
app5=Button(RHB,image=app5_image,bd=0,command=game)
app5.place(x=355,y=50)

app6_image=PhotoImage(file="image/app6.png")
app6=Button(RHB,image=app6_image,bd=0,command=screenshot)
app6.place(x=15,y=120)

app7_image=PhotoImage(file="image/app7.png")
app7=Button(RHB,image=app7_image,bd=0,command=file)
app7.place(x=100,y=120)


app8_image=PhotoImage(file="image/app8.png")
app8=Button(RHB,image=app8_image,bd=0,command=crome)
app8.place(x=185,y=120)


app9_image=PhotoImage(file="image/app9.png")
app9=Button(RHB,image=app9_image,bd=0,command=close_apps)
app9.place(x=270,y=120)

app10_image=PhotoImage(file="image/app10.png")
app10=Button(RHB,image=app10_image,bd=0,command=close_window)
app10.place(x=355,y=120)





root.mainloop()





