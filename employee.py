from tkinter import*
from tkinter import ttk
from webbrowser import get
from PIL import Image,ImageTk
import mysql.connector 
from tkinter import messagebox


class Employee:
    def __init__(self,root):
        self.root=root
        self.root.geometry("1530x790+0+0")
        self.root.title('Employee Management System')

        #Variables
        self.var_dep=StringVar()
        self.var_Name=StringVar()
        self.var_Designation=StringVar()
        self.var_Email=StringVar()
        self.var_Address=StringVar()
        self.var_MaritalStatus=StringVar()
        self.var_DOB=StringVar()
        self.var_Gender=StringVar()
        self.var_Phone_no=StringVar()
        self.var_Country=StringVar()

        

        lbl_title=Label(self.root,text='EMPLOYEE MANAGEMENT SYSTEM',font=('Times New Roman',37,'bold'),fg='Dark Blue',bg='white')
        lbl_title.place(x=0,y=0,width=1530,height=50)

        # LOGO 
        img_logo=Image.open('emp logo.jpg')
        img_logo=img_logo.resize((50,50),Image.ANTIALIAS)
        self.photo_logo=ImageTk.PhotoImage(img_logo)

        self.logo=Label(self.root,image=self.photo_logo)
        self.logo.place(x=270,y=0,width=50,height=50)

        #IMAGE FRAME
        img_frame=Frame(self.root,bd=2,relief=RIDGE,bg='white')
        img_frame.place(x=0,y=50,width=1530,height=160)

        #IMAGE 1
        img1=Image.open('image1.jpg')
        img1=img1.resize((540,160),Image.ANTIALIAS)
        self.photo1=ImageTk.PhotoImage(img1)

        self.img_1=Label(img_frame,image=self.photo1)
        self.img_1.place(x=0,y=0,width=540,height=160)

        #IMAGE 2
        img2=Image.open('image 2.jpg')
        img2=img2.resize((540,160),Image.ANTIALIAS)
        self.photo2=ImageTk.PhotoImage(img2)

        self.img_2=Label(img_frame,image=self.photo2)
        self.img_2.place(x=540,y=0,width=540,height=160)

        #IMAGE 3
        img3=Image.open('images 3.jpg')
        img3=img3.resize((540,160),Image.ANTIALIAS)
        self.photo3=ImageTk.PhotoImage(img3)

        self.img_3=Label(img_frame,image=self.photo3)
        self.img_3.place(x=1000,y=0,width=540,height=160)

        #Main Frame
        Main_frame=Frame(self.root,bd=2,relief=RIDGE,bg='white')
        Main_frame.place(x=10,y=220,width=1500,height=560)

        #UPPER FRAME
        Upper_frame=LabelFrame(Main_frame,bd=2,relief=RIDGE,bg='white',text='Employee Information',font=('Times New Roman',12,'bold'),fg='Red')
        Upper_frame.place(x=10,y=10,width=1480,height=270)

        # Labels and Entry Fields
        lbl_dep=Label(Upper_frame,text='Department :',font=('Arial',12,'bold'),bg='white')
        lbl_dep.grid(row=0,column=0,padx=2,sticky=W )

        combo_dep=ttk.Combobox(Upper_frame,textvariable=self.var_dep,font=('Arial',12,'bold'),width=17,state='readonly')
        combo_dep['value']=('Select Department','HR','Data Analyst','Software Engineer','Manager','Marketing','Accountant')
        combo_dep.current(0)
        combo_dep.grid(row=0,column=1,padx=2,pady=10,sticky=W)

        # Name
        lbl_Name=Label(Upper_frame,font=('Arial',12,'bold'),text='Name :' ,bg='white')
        lbl_Name.grid(row=0,column=2,padx=2,pady=7,stick=W)

        txt_name=ttk.Entry(Upper_frame,textvariable=self.var_Name,width=22,font=('Arial',12,'bold'))
        txt_name.grid(row=0,column=3,padx=2,pady=7)

        # Designation
        lbl_Designation=Label(Upper_frame,font=('Arial',12,'bold'),text='Designation :' ,bg='white')
        lbl_Designation.grid(row=1,column=0,padx=2,pady=7,stick=W)

        txt_designation=ttk.Entry(Upper_frame,textvariable=self.var_Designation,width=22,font=('Arial',12,'bold'))
        txt_designation.grid(row=1,column=1,padx=2,pady=7)

        # Email
        lbl_Email=Label(Upper_frame,font=('Arial',12,'bold'),text='Email :' ,bg='white')
        lbl_Email.grid(row=1,column=2,padx=2,pady=7,stick=W)

        txt_email=ttk.Entry(Upper_frame,textvariable=self.var_Email,width=22,font=('Arial',12,'bold'))
        txt_email.grid(row=1,column=3,padx=2,pady=7)

        # Address
        lbl_Address=Label(Upper_frame,font=('Arial',12,'bold'),text='Address :' ,bg='white')
        lbl_Address.grid(row=2,column=0,padx=2,pady=7,stick=W)

        txt_address=ttk.Entry(Upper_frame,textvariable=self.var_Address,width=22,font=('Arial',12,'bold'))
        txt_address.grid(row=2,column=1,padx=2,pady=7)

        # Marital Status
        lbl_married_status=Label(Upper_frame,text='Married Status :',font=('Arial',12,'bold'),bg='white')
        lbl_married_status.grid(row=2,column=2,padx=2,pady=7,sticky=W )

        combo_txt_married=ttk.Combobox(Upper_frame,textvariable=self.var_MaritalStatus,font=('Arial',12,'bold'),width=18,state='readonly')
        combo_txt_married['value']=('Select Status','Married','Unmarried')
        combo_txt_married.current(0)
        combo_txt_married.grid(row=2,column=3,padx=2,pady=7,sticky=W)

        # DOB
        lbl_DOB=Label(Upper_frame,font=('Arial',12,'bold'),text='DOB :' ,bg='white')
        lbl_DOB.grid(row=3,column=0,padx=2,pady=7,stick=W)

        txt_dob=ttk.Entry(Upper_frame,textvariable=self.var_DOB,width=22,font=('Arial',12,'bold'))
        txt_dob.grid(row=3,column=1,padx=2,pady=7)

        # Gender
        lbl_gender=Label(Upper_frame,text='Gender :',font=('Arial',12,'bold'),bg='white')
        lbl_gender.grid(row=3,column=2,padx=2,pady=7,sticky=W )

        combo_txt_gender=ttk.Combobox(Upper_frame,textvariable=self.var_Gender,font=('Arial',12,'bold'),width=18,state='readonly')
        combo_txt_gender['value']=('Select Gender','Male','Female','Other')
        combo_txt_gender.current(0)
        combo_txt_gender.grid(row=3,column=3,padx=2,pady=7,sticky=W)

        # Phone no
        lbl_Phone_no=Label(Upper_frame,font=('Arial',12,'bold'),text='Phone no :' ,bg='white')
        lbl_Phone_no.grid(row=4,column=0,padx=2,pady=7,stick=W)

        txt_phone_no=ttk.Entry(Upper_frame,textvariable=self.var_Phone_no,width=22,font=('Arial',12,'bold'))
        txt_phone_no.grid(row=4,column=1,padx=2,pady=7)

        #Country 
        lbl_Country=Label(Upper_frame,font=('Arial',12,'bold'),text='Country :' ,bg='white')
        lbl_Country.grid(row=4,column=2,padx=2,pady=7,sticky=W)

        txt_country=ttk.Entry(Upper_frame,textvariable=self.var_Country,width=22,font=('Arial',12,'bold'))
        txt_country.grid(row=4,column=3,padx=2,pady=7)

        # Button Frame
        button_frame=Frame(Upper_frame,bd=2,relief=RIDGE,bg='white')   

        button_frame.place(x=1000,y=0,width=170,height=220)

        btn_add=Button(button_frame,text="Save",command=self.add_data,font=('Arial',15,'bold'),width=13,fg='White',bg='Blue')
        btn_add.grid(row=0,column=0,padx=1,pady=7)

        btn_update=Button(button_frame,text="Update",command=self.update_data,font=('Arial',15,'bold'),width=13,fg='White',bg='Blue')
        btn_update.grid(row=1,column=0,padx=1,pady=7)

        btn_delete=Button(button_frame,text="Delete",command=self.Delete_data,font=('Arial',15,'bold'),width=13,fg='White',bg='Blue')
        btn_delete.grid(row=2,column=0,padx=1,pady=7)

        btn_clear=Button(button_frame,text="Clear",command=self.reset_data,font=('Arial',15,'bold'),width=13,fg='White',bg='Blue')
        btn_clear.grid(row=3,column=0,padx=1,pady=7)

        #DOWN FRAME
        Down_frame=LabelFrame(Main_frame,bd=2,relief=RIDGE,bg='white',text='Employee Information Table',font=('Times New Roman',12,'bold'),fg='Red')
        Down_frame.place(x=10,y=280,width=1480,height=270)
        
        # Search Frame
        Search_frame=LabelFrame(Down_frame,bd=2,relief=RIDGE,bg='white',text='Search Employee Information ',font=('Times New Roman',12,'bold'),fg='Red')
        Search_frame.place(x=0,y=0,width=1470,height=60)

        search_by=Label(Search_frame,font=('Arial',12,'bold'),text='Search By :',fg='white',bg='red')
        search_by.grid(row=0,column=0,padx=5,sticky=W)

        # Search
        self.var_com_search=StringVar()
        combo_txt_search=ttk.Combobox(Search_frame,textvariable=self.var_com_search,font=('Arial',12,'bold'),width=18,state='readonly')
        combo_txt_search['value']=('Select Option','Name','Phone no')
        combo_txt_search.current(0)
        combo_txt_search.grid(row=0,column=1,padx=5,sticky=W)

        self.var_search=StringVar()
        txt_search=ttk.Entry(Search_frame,textvariable=self.var_search,width=22,font=('Arial',12,'bold'))
        txt_search.grid(row=0,column=2,padx=5)

        btn_search=Button(Search_frame,text='Search',command=self.search_data,font=('Arial',15,'bold'),width=14,fg='White',bg='Blue')
        btn_search.grid(row=0,column=3,padx=5)

        btn_ShowAll=Button(Search_frame,text='Show All',command=self.fetch_data,font=('Arial',15,'bold'),width=14,fg='White',bg='Blue')
        btn_ShowAll.grid(row=0,column=4,padx=5)


        # --------Employee Table-----------
        # Table Frame
        Table_frame=Frame(Down_frame,bd=3,relief=RIDGE)
        Table_frame.place(x=0,y=60,width=1470,height=170)

        # Scroll Bar
        scroll_x=ttk.Scrollbar(Table_frame,orient=HORIZONTAL)
        scroll_y=ttk.Scrollbar(Table_frame,orient=VERTICAL)

        self.employee_table=ttk.Treeview(Table_frame,column=('dep','Name','Designation','Email','Address','Marital Status','DOB','Gender','Phone_no','Country',),xscrollcommand=scroll_x.set,yscrollcommand=scroll_y.set)
        scroll_x.pack(side=TOP,fill=X)
        scroll_y.pack(side=LEFT,fill=Y)

        scroll_x.config(command=self.employee_table.xview)
        scroll_y.config(command=self.employee_table.yview)

        self.employee_table.heading('dep',text='Department')
        self.employee_table.heading('Name',text='Name')
        self.employee_table.heading('Designation',text='Designation')
        self.employee_table.heading('Email',text='Email')
        self.employee_table.heading('Address',text='Address')
        self.employee_table.heading('Marital Status',text='Marital Status')
        self.employee_table.heading('DOB',text='DOB')
        self.employee_table.heading('Gender',text='Gender')
        self.employee_table.heading('Phone_no',text='Phone_no')
        self.employee_table.heading('Country',text='Country')

        self.employee_table['show']='headings'

    
        self.employee_table.column('dep',width=50)
        self.employee_table.column('Name',width=50)
        self.employee_table.column('Designation',width=50)
        self.employee_table.column('Email',width=100)
        self.employee_table.column('Address',width=50)
        self.employee_table.column('Marital Status',width=50)
        self.employee_table.column('DOB',width=50)
        self.employee_table.column('Gender',width=50)
        self.employee_table.column('Phone_no',width=50)
        self.employee_table.column('Country',width=50) 
        

        self.employee_table.pack(fill=BOTH,expand=1)
        self.employee_table.bind("<ButtonRelease>",self.get_cursor)

        self.fetch_data()


        # ************* Function Declaration *************


    def add_data(self):
        if self.var_dep.get()==""or self.var_Email.get()=="":
            messagebox.showerror('Error','All Fields are required')
        else:
            try:
                conn=mysql.connector.connect(host='localhost',user='root',password='Pakhi@1719',database='employee_data')
                my_cursor=conn.cursor()
                my_cursor.execute('Insert into emp values(%s,%s,%s,%s,%s,%s,%s,%s,%s,%s)',(
                                                                                              self.var_dep.get(),
                                                                                              self.var_Name.get(),
                                                                                              self.var_Designation.get(),
                                                                                              self.var_Email.get(),
                                                                                              self.var_Address.get(),
                                                                                              self.var_MaritalStatus.get(),
                                                                                              self.var_DOB.get(),
                                                                                              self.var_Gender.get(),
                                                                                              self.var_Phone_no.get(),
                                                                                              self.var_Country.get(),

                                                                                          ))
                conn.commit()
                self.fetch_data()
                conn.close()
                messagebox.showinfo('Success','Employee has been added! ',parent=self.root)
            except Exception as es:
                messagebox.showerror('Error',f'Due to:{str(es)}',parent=self.root)                                                                          


    # fetch Data
    def fetch_data(self):
        conn=mysql.connector.connect(host='localhost',user='root',password='Pakhi@1719',database='employee_data')
        my_cursor=conn.cursor()
        my_cursor.execute('Select * from emp')
        data=my_cursor.fetchall()
        if len(data)!=0:
            self.employee_table.delete(*self.employee_table.get_children())
            for i in data:
                self.employee_table.insert("",END,value=i)
            conn.commit()
        conn.close()

    # Get Cursor
    def get_cursor(self,event=""):
        cursor_row=self.employee_table.focus()
        content=self.employee_table.item(cursor_row)
        data=content['values']

        self.var_dep.set(data[0])
        self.var_Name.set(data[1])
        self.var_Designation.set(data[2])
        self.var_Email.set(data[3])
        self.var_Address.set(data[4])
        self.var_MaritalStatus.set(data[5])
        self.var_DOB.set(data[6])
        self.var_Gender.set(data[7])
        self.var_Phone_no.set(data[8])
        self.var_Country.set(data[9])

    # Update

    def update_data(self):
        if self.var_dep.get()=="" or self.var_Email.get()=="":
            messagebox.showerror('Error','All Fields are required')
        else:
            try:
                update=messagebox.askyesno('Update','Are you sure update this employee data')
                if update>0:
                    conn=mysql.connector.connect(host='localhost',user='root',password='Pakhi@1719',database='employee_data')
                    my_cursor=conn.cursor()
                    sql='update emp set Department=%s,Designation=%s,Email=%s,Address=%s,Marital Status=%s,DOB=%s,Gender=%s,Phone_no=%s,Country=%s where Name=%s'
                    value=(self.var_Name.get(),)
                    my_cursor.execute(sql,value)

                    """
                    my_cursor.execute('update emp SET Department=%s,Name=%s,Designation=%s,Email=%s,Address=%s,Marital Status=%s,DOB=%s,Gender=%s,Phone_no=%s where Country=%s ',(
                                                                                                                                                                    
                                                                                                                                                                      self.var_dep.get(),
                                                                                                                                                                      self.var_Name.get(),
                                                                                                                                                                      self.var_Designation.get(),
                                                                                                                                                                      self.var_Email.get(),
                                                                                                                                                                      self.var_Address.get(),
                                                                                                                                                                      self.var_MaritalStatus.get(),
                                                                                                                                                                      self.var_DOB.get(),
                                                                                                                                                                      self.var_Gender.get(),
                                                                                                                                                                      self.var_Phone_no.get(),
                                                                                                                                                                      self.var_Country.get()

                                                                                                                                                                    
                                                                                                                                                                      



                                                                                                                                                                       ))
                                                                                                                                                                       """
                                                                                                                                                                       
                else:
                    if not update:
                        return
                conn.commit()
                self.fetch_data()
                conn.close()
                messagebox.showinfo('Sucess','Employee Succesfully Updated',parent=self.root)
            except Exception as es:
                messagebox.showerror('Error',f'Due to:{str(es)}',parent=self.root) 

    # Delete

    def Delete_data(self):
        if self.var_Name.get()=="":
            messagebox.showerror('Error','All Fields are required')
        else:
            try:
                Delete=messagebox.askyesno('Delete','Are you sure delete this employee data ',parent=self.root)
                if Delete>0:
                    conn=mysql.connector.connect(host='localhost',user='root',password='Pakhi@1719',database='employee_data')
                    my_cursor=conn.cursor()
                    sql='delete from emp where Name=%s'
                    value=(self.var_Name.get(),)
                    my_cursor.execute(sql,value)
                else:
                    if not Delete:
                        return
                conn.commit()
                self.fetch_data()
                conn.close()
                messagebox.showinfo('Delete','Employee Succesfully Deleted',parent=self.root)
            except Exception as es:
                messagebox.showerror('Error',f'Due to:{str(es)}',parent=self.root) 


    # Reset Data

    def reset_data(self):
        self.var_dep.set("Select Department")
        self.var_Name.set("")
        self.var_Designation.set("")
        self.var_Email.set("")
        self.var_Address.set("")
        self.var_MaritalStatus.set("Married")
        self.var_DOB.set("")
        self.var_Gender.set("Male")
        self.var_Phone_no.set("")
        self.var_Country.set("")

    # Search

    def search_data(self):
        if self.var_com_search.get()=='' or self.var_com_search.get()=='':
            messagebox.showerror('Error','Please select option')
        else:
            try:
                conn=mysql.connector.connect(host='localhost',user='root',password='Pakhi@1719',database='employee_data')
                my_cursor=conn.cursor()
                my_cursor.execute('Select * from emp where ' +str(self.var_com_search.get())+" LIKE '%" +str(self.var_search.get()+"%'"))
                rows=my_cursor.fetchall()
                if len(rows)!=0:
                    self.employee_table.delete(*self.employee_table.get_children())
                    for i in rows:
                        self.employee_table.insert("",END,values=i)
                conn.commit()
                conn.close()

            except Exception as es:
                messagebox.showerror('Error',f'Due to:{str(es)}',parent=self.root) 
    



    

    












    
                
               
                                                                                                       


        
if __name__=="__main__" :
    root=Tk()
    obj=Employee(root)
    root.mainloop()

