from tkinter import *
from tkinter import ttk
import requests
#cratign function for set all data.....
def get_data():
    city=city_name.get()
    #here iam copy this weather api from google.....
    data=requests.get("https://api.openweathermap.org/data/2.5/weather?q="+city+"+&appid=75fb9967603a18aa80451a6c84d72f46").json()
    w_climate1.config(text=data['weather'][0]['main'])
    w_des1.config(text=data["weather"][0]["description"])
    temp1.config(text=(round(data["main"]["temp"]-273.15)))
    press1.config(text=data["main"]["pressure"])



win=Tk()
win.title("weatherapp")
win.config(bg="blue")
win.geometry("500x500")
name_label=Label(win,text="Rinku Weather App",font=("Times New Roman",30,"bold"))
name_label.place(x=25,y=50,height=50,width=470)
#creating a variablre for combo box
list_name=["Andhra Pradesh","Arunachal Pradesh ","Assam","Bihar","Chhattisgarh","Goa","Gujarat","Haryana","Himachal Pradesh","Jammu and Kashmir","Jharkhand","Karnataka","Kerala","Madhya Pradesh","Maharashtra","Manipur","Meghalaya","Mizoram","Nagaland","Odisha","Punjab","Rajasthan","Sikkim","Tamil Nadu","Telangana","Tripura","Uttar Pradesh","Uttarakhand","West Bengal","Andaman and Nicobar Islands","Chandigarh","Dadra and Nagar Haveli","Daman and Diu","Lakshadweep","National Capital Territory of Delhi","Puducherry"]
city_name=StringVar()
com_box=ttk.Combobox(win,text="Rinku Weather App",values=list_name,font=("Times New Roman",20,"bold"),textvariable=city_name)
com_box.place(x=25,y=120 ,height=50,width=450)
#creatign a button

w_climate=Label(win,text="Weather Climate:",font=("Times New Roman",20,"bold",),bg="blue")
w_climate.place(x=25,y=260,height=40,width=250)
#creatign a button
w_climate1=Label(win,text="",font=("Times New Roman",20,"bold",),bg="blue")
w_climate1.place(x=250,y=260,height=40,width=200)


w_des=Label(win,text="Weather Description:",font=("Times New Roman",20,"bold"),bg="blue")
w_des.place(x=23,y=300,height=40,width=300)

w_des1=Label(win,text="",font=("Times New Roman",20,"bold",),bg="blue")
w_des1.place(x=290,y=300,height=40,width=250)


temp=Label(win,text="Tempreture:",font=("Times New Roman",20,"bold",),bg="blue")
temp.place(x=23,y=340,height=40,width=200)


temp1=Label(win,text="",font=("Times New Roman",20,"bold",),bg="blue")
temp1.place(x=250,y=340,height=40,width=150)


press=Label(win,text="Pressure:",font=("Times New Roman",20,"bold",),bg="blue")
press.place(x=23,y=380,height=40,width=170)



press1=Label(win,text="",font=("Times New Roman",20,"bold",),bg="blue")
press1.place(x=200,y=380,height=40,width=170)

button=Button(win,text="Submit",font=("Times New Roman",20,"bold"),command=get_data)
button.place(x=180,y=190,height=50,width=150)

win.mainloop()
