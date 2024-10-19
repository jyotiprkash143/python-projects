from tkinter import *
from tkinter import ttk
import random
import time 
import datetime
from tkinter import messagebox
import mysql.connector



class hospital:
    def __init__(self,root):
        self.root=root
        self.root.title("'Hospital Management System")
        self.root.geometry("1540x800+0+0")

        self.Nameoftablets=StringVar()
        self.ref=StringVar()
        self.Dose=StringVar()
        self.NoofTablets=StringVar()
        self.Lot=StringVar()
        self.Issuedate=StringVar()
        self.ExpDate=StringVar() 
        self.DailyDose=StringVar()
        self.sideEffect=StringVar()
        self.FurtureInformation=StringVar()
        self.StorageAdvice=StringVar()
        self.DrivingUsingMachine=StringVar()
        self.HowToUseMedication=StringVar()
        self.PatientId=StringVar()
        self.nhsNumber=StringVar()
        self.PatientName=StringVar()
        self.DateOfBirth=StringVar()
        self.PatientAdress=StringVar()
        

        lbltitle=Label(self.root,text='HOSPITAL MANAGEMNET SYSTEM',bd=20,relief=RIDGE,fg="#4EF738",
                       bg="white",font=('Times New Roman',50,'bold'))
        lbltitle.pack(side=TOP,fill=X)
        #######################################data frame################################################
        dataframe=Frame(self.root,bd=20,relief=RIDGE)
        dataframe.place(x=0,y=130,width=1530,height=400)
        dataframe_left=LabelFrame(dataframe,bd=10,padx=20,relief=RIDGE,font=('arial',12,'bold'),
        text="patient information",fg='#0140ff')
        dataframe_left.place(x=0,y=5,width=980,height=350)
        dataframe_right=LabelFrame(dataframe,bd=10,padx=10,relief=RIDGE,
        font=('Times New Roman',12,'bold'),text='prescription')
        dataframe_right.place(x=990,y=5,width=460,height=350)
        #####################################button frame#####################################
        buton_frame=Frame(self.root,bd=20,relief=RIDGE)
        buton_frame.place(x=0,y=530,width=1530,height=70)
        ######################################detail frame#######################################
        dataframe=Frame(self.root,bd=20,relief=RIDGE)
        dataframe.place(x=0,y=600,width=1530,height=190)

##################################data frame left ####################################
        lbl_tablet_name=Label(dataframe_left,text='Name of tablet',font=('times new roman',12,'bold'),
        padx=2,pady=6,fg="#fe00e1")
        lbl_tablet_name.grid(row=0,column=0)
        com_name_tablet=ttk.Combobox(dataframe_left,textvariable=self.Nameoftablets,font=('times new roman',12,'bold'),width=33)
        com_name_tablet['values']=(['Nice','Corohna vacecine','Acetamenpheom','Aderall','Amoldipine','Ativan'])
        com_name_tablet.grid(row=0,column=1)

        lbl_ref=Label(dataframe_left,font=('arial',12,'bold'),text='Reference No:',padx=2,)
        lbl_ref.grid(row=1,column=0) 
        txt_ref=Entry(dataframe_left,font=('arial',13,'bold'),textvariable=self.ref,width=35)
        txt_ref.grid(row=1,column=1)

        lbl_dose=Label(dataframe_left,font=('arial',12,'bold'),text='Dose:',padx=2,pady=4)
        lbl_dose.grid(row=2,column=0,sticky=W)
        txt_dose=Entry(dataframe_left,font=('arial',13,'bold'),textvariable=self.Dose,width=35)
        txt_dose.grid(row=2,column=1)

        lbl_noof_tablets=Label(dataframe_left,font=('arial',12,'bold'),text='No Of Tablets:',padx=2,pady=4)
        lbl_noof_tablets.grid(row=3,column=0,sticky=W)
        txt_noof_tablets=Entry(dataframe_left,font=('arial',13,'bold'),textvariable=self.NoofTablets,width=35)
        txt_noof_tablets.grid(row=3,column=1)

        lbl_lot=Label(dataframe_left,font=('arial',12,'bold'),text='Lot:',padx=2,pady=4)
        lbl_lot.grid(row=4,column=0,sticky=W)
        txt_lot=Entry(dataframe_left,font=('arial',13,'bold'),textvariable=self.Lot,width=35)
        txt_lot.grid(row=4,column=1)

        lbl_issue_date=Label(dataframe_left,font=('arial',12,'bold'),text='Issue Date:',padx=2,pady=4)
        lbl_issue_date.grid(row=5,column=0,sticky=W)
        txt_issue_date=Entry(dataframe_left,font=('arial',13,'bold'),textvariable=self.Issuedate,width=35)
        txt_issue_date.grid(row=5,column=1)
        
        lbl_Exp_date=Label(dataframe_left,font=('arial',12,'bold'),text='Expire Date:',padx=2,pady=4)
        lbl_Exp_date.grid(row=6,column=0,sticky=W)
        txt_Exp_date=Entry(dataframe_left,font=('arial',13,'bold'),textvariable=self.ExpDate,width=35)
        txt_Exp_date.grid(row=6,column=1)

        lbl_Daily_Dose=Label(dataframe_left,font=('arial',12,'bold'),text='Daily Dose:',padx=2,pady=4)
        lbl_Daily_Dose.grid(row=7,column=0,sticky=W)
        txt_Daily_Dose=Entry(dataframe_left,font=('arial',13,'bold'),textvariable=self.DailyDose,width=35)
        txt_Daily_Dose.grid(row=7,column=1)

        lbl_Sideeffect=Label(dataframe_left,font=('arial',12,'bold'),text='Side Effect:',padx=2,pady=4)
        lbl_Sideeffect.grid(row=8,column=0,sticky=W)
        txt_sideeffect=Entry(dataframe_left,font=('arial',13,'bold'),textvariable=self.sideEffect,width=35)
        txt_sideeffect.grid(row=8,column=1)

        lbl_furtureinfo=Label(dataframe_left,font=('arial',12,'bold'),text='Furture Info:',padx=2,pady=4)
        lbl_furtureinfo.grid(row=0,column=2,sticky=W)
        txt_furtureinfo=Entry(dataframe_left,font=('arial',13,'bold'),textvariable=self.FurtureInformation,width=35)
        txt_furtureinfo.grid(row=0,column=3) 

        lbl_bloodpressure=Label(dataframe_left,font=('arial',12,'bold'),text='Blood Pressure:',padx=2,pady=4)
        lbl_bloodpressure.grid(row=1,column=2,sticky=W)
        txt_bloodpressure=Entry(dataframe_left,font=('arial',13,'bold'),textvariable=self.DrivingUsingMachine,width=35)
        txt_bloodpressure.grid(row=1,column=3)

        lbl_Storage =Label(dataframe_left,font=('arial',12,'bold'),text='Storage:',padx=2,pady=4)
        lbl_Storage.grid(row=2,column=2,sticky=W)
        txt_Storage=Entry(dataframe_left,font=('arial',13,'bold'),textvariable=self.StorageAdvice,width=35)
        txt_Storage.grid(row=2,column=3)

        lbl_Medicine =Label(dataframe_left,font=('arial',12,'bold'),text='Medication:',padx=2,pady=4)
        lbl_Medicine.grid(row=3,column=2,sticky=W)
        txt_Medicine=Entry(dataframe_left,font=('arial',13,'bold'),textvariable=self.HowToUseMedication,width=35)
        txt_Medicine.grid(row=3,column=3)

        lbl_Patientid =Label(dataframe_left,font=('arial',12,'bold'),text='Patient Id:',padx=2,pady=4)
        lbl_Patientid.grid(row=4,column=2,sticky=W)
        txt_Patientid=Entry(dataframe_left,font=('arial',13,'bold'),textvariable=self.PatientId,width=35)
        txt_Patientid.grid(row=4,column=3)

        lbl_Nhsnumber =Label(dataframe_left,font=('arial',12,'bold'),text='NHS Number:',padx=2,pady=4)
        lbl_Nhsnumber.grid(row=5,column=2,sticky=W)
        txt_Nhsnumber=Entry(dataframe_left,font=('arial',13,'bold'),textvariable=self.nhsNumber,width=35)
        txt_Nhsnumber.grid(row=5,column=3)




        lbl_dateofbirth =Label(dataframe_left,font=('arial',12,'bold'),text='Date Of Birth:',padx=2,pady=4)
        lbl_dateofbirth.grid(row=7,column=2,sticky=W)
        txt_dateofbirth=Entry(dataframe_left,font=('arial',13,'bold'),textvariable=self.DateOfBirth,width=35)
        txt_dateofbirth.grid(row=7,column=3)
        
        lbl_Patientname =Label(dataframe_left,font=('arial',12,'bold'),text='Patient Name:',padx=2,pady=4)
        lbl_Patientname.grid(row=6,column=2,sticky=W)
        txt_Patientname=Entry(dataframe_left,font=('arial',13,'bold'),textvariable=self.PatientName,width=35)
        txt_Patientname.grid(row=6,column=3)

        lbl_patientadress =Label(dataframe_left,font=('arial',12,'bold'),text='Adress:',padx=2,pady=4)
        lbl_patientadress.grid(row=8,column=2,sticky=W)
        txt_Patientadress=Entry(dataframe_left,font=('arial',13,'bold'),textvariable=self.PatientAdress,width=35)
        txt_Patientadress.grid(row=8,column=3)

        
        #################################dateframe right##################################
        self.txtpresciption=Text(dataframe_right,font=('arial',12,'bold'),width=46,height=16,padx=2,pady=6)
        self.txtpresciption.grid(row=0,column=0)
        ###############################function for button#########################################
        def fetch_data(self):
                conn=mysql.connector.connect(host='localhost',username='root',password='Rinku2123',
                                             database='mydata')

                mycursor=conn.cursor()
                mycursor.execute("select * from hospital")
                rows=mycursor.fetchall()
                if len(rows)!=0:
                        self.hospital_table.delete(*self.hospital_table.get_children())
                        for i in rows:
                                self.hospital_table.insert("",END,values=i)
                                conn.commit()
                conn.close()
    
               
       # def get_cursor(self,event=""):
               # cursor_row=self.hospital_table.focus()
               # content=self.hospital_table.item(cursor_row)
               # row=content["values"]
                #self.Nameoftablets.set(row[0])

                ## self.self.Dose.set(row[2])
                #### self.DailyDose.set(row[6])
                #self.StorageAdvice.set(row[7])
                #self.nhsNumber.set(row[8])
#self.PatientName.set(row[9])
                #self.DateOfBirth.set(row[10])
                #self.PatientAdress.set(row[11])



        def ipresciption(self):
                conn=mysql.connector.connect(host='localhost',username='root',password='Rinku2123',
                                             database='mydata')
                mycursor=conn.cursor()
                sql="INSERT INTO hospital(Name_of_tablets,Refernce_no,Dose,Numbersoftablets,issue_date,expire_data,dailydose,storage,nhsnumbr,patient_name,dob,patient_adress) VALUES(%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s)"
                val=(self.Nameoftablets.get(),self.ref.get(),self.Dose.get(),self.NoofTablets.get(),self.Issuedate.get(),self.ExpDate.get(),self.DailyDose.get(),self.StorageAdvice.get(),self.nhsNumber.get(),self.PatientName.get(),self.DateOfBirth.get(),self.PatientAdress.get())
                mycursor.execute(sql,val)
                conn.commit()
                fetch_data(self)
                conn.close()
                messagebox.showinfo('showinfo','data inserted')
        
        def fetch_data(self):
                conn=mysql.connector.connect(host='localhost',username='root',password='Rinku2123',
                                             database='mydata')
                mycursor=conn.cursor()
                mycursor.execute("select * from hospital")
                rows=mycursor.fetchall()
                if len(rows)!=0:
                        self.hospital_table.delete(*self.hospital_table.get_children())
                        for i in rows:
                                self.hospital_table.insert("",END,values=i)
                                conn.commit()
                conn.close()
                        



        #################################buttons##########################################
        btn_presciption =Button(buton_frame,font=('arial',15,'bold'),bg='#D523EC',fg='white',text='Presciption',width=23,padx=3,pady=4)
        btn_presciption.grid(row=0,column=0)

        btn_presciptiondata =Button(buton_frame,font=('arial',15,'bold'),bg='#D523EC',fg='white',text='Presciption Data',width=23,padx=3,pady=4,command=ipresciption)
        btn_presciptiondata.grid(row=0,column=1)

        btn_update =Button(buton_frame,font=('arial',15,'bold'),bg='#D523EC',fg='white',text='Update',width=23,padx=3,pady=4)
        btn_update.grid(row=0,column=2)
        
        btn_delete =Button(buton_frame,font=('arial',15,'bold'),bg='#D523EC',fg='white',text='Delete',width=23,padx=3,pady=4)
        btn_delete.grid(row=0,column=3)

        btn_clear=Button(buton_frame,font=('arial',15,'bold'),bg='#D523EC',fg='white',text='Clear',width=23,padx=3,pady=4)
        btn_clear.grid(row=0,column=4)

        btn_exit=Button(buton_frame,font=('arial',15,'bold'),bg='#D523EC',fg='white',text='Exit',width=23,padx=3,pady=4)
        btn_exit.grid(row=0,column=5)
         ####################################table#########################################
        ####################################scroll bar##########################################
        scroll_x=ttk.Scrollbar(dataframe,orient=HORIZONTAL)
        scroll_y=ttk.Scrollbar(dataframe,orient=VERTICAL)
        self.hospital_table=ttk.Treeview(dataframe,columns=('nameoftablets','ref','dose','nooftablets',
        'issuedate','expdate','dailydose','storage','nhsnumber','pname','dob','adress'),
        xscrollcommand=scroll_x.set,yscrollcommand=scroll_y.set)
        scroll_x.pack(side=BOTTOM,fill=X)
        scroll_y.pack(side=RIGHT,fill=Y)
        scroll_x=ttk.Scrollbar(command=self.hospital_table.xview)
        scroll_y=ttk.Scrollbar(command=self.hospital_table.yview)

        
        self.hospital_table.heading('nameoftablets',text='Name Of Tablets')
        self.hospital_table.heading('ref',text='Refernce No')
        self.hospital_table.heading('dose',text='Dose')
        self.hospital_table.heading('nooftablets',text='No Of Tablets')
        #self.hospital_table.heading('lot',text='Lot')
        self.hospital_table.heading('issuedate',text='Issue Date')
        self.hospital_table.heading('expdate',text='Expire Date')
        self.hospital_table.heading('dailydose',text='Daily Dose')
        self.hospital_table.heading('storage',text='Storage')
        self.hospital_table.heading('nhsnumber',text='NHS number')
        self.hospital_table.heading('pname',text='Patient Name')
        self.hospital_table.heading('dob',text='Date Of Birth')
        self.hospital_table.heading  ('adress',text='Adress')
        self.hospital_table['show']='headings'
        self.hospital_table.pack(fill=BOTH,expand=1)

        self.hospital_table.column('nameoftablets',width=100,)
        self.hospital_table.column('ref',width=100,)
        self.hospital_table.column('dose',width=100,)
        self.hospital_table.column('nooftablets',width=100,)
        #self.hospital_table.column('lot',width=100,)
        self.hospital_table.column('issuedate',width=100,)
        self.hospital_table.column('expdate',width=100,)
        self.hospital_table.column('dailydose',width=100,)
        self.hospital_table.column('storage',width=100,)
        self.hospital_table.column('nhsnumber',width=100,)
        self.hospital_table.column('dob',width=100,)
        self.hospital_table.column('adress',width=100,)
        self.hospital_table.pack(fill=BOTH,expand=1)
        self.hospital_table.bind("<ButtonRelease-1>",fetch_data)
        fetch_data(self)

        

       #################################functinality declaration###########################
       # def IpresciptionData():
            #if self.Nameoftablets.get()=="" or self.ref.get()=="":
              # messagebox.showerror('Error','All Fileds Are Required')
            #else:
               # conn=mysql.connector.connect(host='localhost',username='root',password='Rinku2123',
                                            # database='mydata')
                #mycursor=conn.cursor()
                #sql="INSERT INTO hospital(Name_of_tablets,Refernce_no,Dose,Numbersoftablets,issue_date,expire_data,dailydose,storage,nhsnumbr,patient_name,dob,patient_adress) VALUES(%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s)"
               # val=(self.Nameoftablets.get(),self.ref.get(),self.Dose.get(),self.NoofTablets.get(),self.Issuedate.get(),self.ExpDate.get(),self.DailyDose.get(),self.StorageAdvice.get(),self.nhsNumber.get(),self.PatientName.get(),self.DateOfBirth.get(),self.PatientAdress.get())

               # mycursor.execute(sql,val)
                #conn.commit()
                #conn.close()
                #('data inserted succesfully')
                
        def get_cursor(self):
                cursor_row=self.hospital_table.focus()
                content=self.hospital_table.item(cursor_row)
                row=content["values"]
                self.Nameoftablets.set(row[0])

                self.ref.set(row[1])
                self.self.Dose.set(row[2])
                self.NoofTablets.set(row[3])
                self.Issuedate.set(row[4])
                self.ExpDate.set(row[5])
                self.DailyDose.set(row[6])
                self.StorageAdvice.set(row[7])
                self.nhsNumber.set(row[8])
                self.PatientName.set(row[9])
                self.DateOfBirth.set(row[10])
                self.PatientAdress.set(row[11])

        

root=Tk()
obj=hospital(root)

root.mainloop()