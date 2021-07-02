from tkinter import *
import os
import pymysql
from tkinter import ttk
from tkinter import messagebox

def register_user():
    username_info=username.get()
    password_info=password.get()

    file=open(username_info, "w")
    file.write(username_info+"\n")
    file.write(password_info)
    file.close()

    username_entry.delete(0, END)
    password_entry.delete(0, END)

    Label(screen1, text="Registration succesful").pack()

def register():
    global screen1
    global username
    global password
    global username_entry
    global password_entry

    screen1=Toplevel(screen)
    screen1.title("Register")
    screen1.geometry("600x450")
    screen1.configure(background="yellow")

    username=StringVar()
    password=StringVar()

    Label(screen1, text="Enter details to Register", font=("times new roman",25,"bold"), pady=15,bg="yellow").pack()
    Label(screen1, text="Username : ",font=(50), width=20, height=2,pady=10, padx=10,bg="yellow").pack()
    username_entry=Entry(screen1, width=20,textvariable = username)
    username_entry.pack()
    Label(screen1, text="Password : ", font=(50), width=20, height=2,pady=10, padx=10,bg="yellow").pack()
    password_entry=Entry(screen1, width=20, textvariable = password)
    password_entry.pack()
    Label(screen1, text="",bg="yellow").pack()
    Button(screen1, text="Register",font=(10),width=20 ,pady=10, padx=10,activebackground="blue" , command=register_user).pack()

def logins():
    global screen2
    global username_verify
    global password_verify
    global username_entry1
    global password_entry1

    screen2=Toplevel(screen)
    screen2.title("Login")
    screen2.geometry("612x408")
    screen2.configure(background="red")
    Label(screen2, text="Enter details to login", font=("times new roman",25,"bold"), pady=15, bg="red").pack()
    username_verify=StringVar()
    password_verify=StringVar()
    Label(screen2, text="Username : ", font=(170), bg="red").pack()
    Label(screen2,text="" ,bg="red").pack()
    username_entry1=Entry(screen2, textvariable=username_verify)
    username_entry1.pack()  
    Label(screen2,text="" ,bg="red").pack()  
    Label(screen2, text="Password : ", font=(170), bg="red").pack()
    password_entry1=Entry(screen2, textvariable=password_verify)
    password_entry1.pack()
    Label(screen2,text="" ,bg="red").pack() 
    Button(screen2, text="Login",font=(20),width=10 ,height=2,pady=3, padx=3,activebackground="blue", command=login_verify).pack()

def login_verify():
    username1=username_verify.get()
    password1=password_verify.get()

    username_entry1.delete(0, END)
    password_entry1.delete(0, END)

    list_of_files=os.listdir()
    if username1 in list_of_files:
        file1=open(username1,"r")
        verify=file1.read().splitlines()
        if password1 in verify:
            x=Label(screen2, text="Login successful")
            x.pack()
            ecoms()
            screen2.destroy()
            screen.withdraw()
        else:
            y=Label(screen2, text="Wrong password")
            y.pack()
    else:
        z=Label(screen2, text="User not registered")
        z.pack()

def login_screen():
    global screen
    screen=Tk()
    screen.title("Login")
    screen.geometry("612x408")

    screen.configure(background='dark blue')

    Label(text="Login/Register to your account", font=("times new roman",25,"bold"),bg="dark blue", fg="yellow" ,pady=15).pack()
    Label(text="", pady=5 ,bg="dark blue").pack()
    Button(text="Login",font=(50), width=20, height=2,pady=10, padx=10,activebackground="blue", command=logins).pack()
    Label(text="", pady=5 ,bg="dark blue").pack()
    Button(text="Register",font=(50),width=20 ,height=2,pady=10, padx=10,activebackground="blue" ,command=register).pack()
    screen.mainloop()

def ecoms():

    def add_products():
        if p_id.get()=="" or p_name.get()=="" or p_seller.get()=="" or p_type.get()=="" or p_ava.get()=="" or p_price.get()=="":
            messagebox.showerror("Error","Please fill all the fields!")
        connection=pymysql.connect(host="localhost", user="root", password="", database="asm")
        cursor=connection.cursor()
        cursor.execute("insert into ecom values(%s,%s,%s,%s,%s,%s)",(p_id.get(),
                                                                    p_name.get(),
                                                                    p_seller.get(),
                                                                    p_type.get(),
                                                                    p_ava.get(),
                                                                    p_price.get()
                                                                    ))
        connection.commit()
        print_data()
        clear()
        connection.close()
        messagebox.showinfo("Success","Successfully inserted values!")

    def print_data():
        connection=pymysql.connect(host="localhost", user="root", password="", database="asm")
        cursor=connection.cursor()
        cursor.execute("select * from ecom")
        rows=cursor.fetchall()
        if len(rows)!=0:
            ecom.delete(*ecom.get_children())
            for row in rows:
                ecom.insert('',END,values=row)
            connection.commit()
        connection.close()
    
    def clear():
        p_id.set("")
        p_name.set("")
        p_seller.set("")
        p_type.set("")
        p_ava.set("")
        p_price.set("")

    def get_cursor(ev):
        cursor_row=ecom.focus()
        contents=ecom.item(cursor_row)
        row=contents['values']
        p_id.set(row[0])
        p_name.set(row[1])
        p_seller.set(row[2])
        p_type.set(row[3])
        p_ava.set(row[4])
        p_price.set(row[5])

    def update_values():
        connection=pymysql.connect(host="localhost", user="root", password="", database="asm")
        cursor=connection.cursor()
        cursor.execute("update ecom set pname=%s,pseller=%s,ptype=%s,pava=%s,pprice=%s where pid=%s",(
                                                                     p_name.get(),
                                                                     p_seller.get(),
                                                                     p_type.get(),
                                                                     p_ava.get(),
                                                                     p_price.get(),
                                                                     p_id.get()
                                                                    ))
        connection.commit()
        print_data()
        clear()
        connection.close()

    def delete_values():
        connection=pymysql.connect(host="localhost", user="root", password="", database="asm")
        cursor=connection.cursor()
        cursor.execute("delete from ecom where pid=%s", p_id.get())
        connection.commit()
        connection.close()
        print_data()
        clear()

    def search_data():
        connection=pymysql.connect(host="localhost", user="root", password="", database="asm")
        cursor=connection.cursor()
        cursor.execute("select * from ecom where "+str(search_by.get())+" LIKE '%"+str(search_txt.get())+"%'")
        rows=cursor.fetchall()
        if len(rows)!=0:
            ecom.delete(*ecom.get_children())
            for row in rows:
                ecom.insert('',END,values=row)
            connection.commit()
        connection.close()

    global screen3
    screen3=Toplevel(screen)
    screen3.title("Ecommerce Portal")
    screen3.geometry("1350x700+0+0")
    screen3.lift()
    screen3.attributes('-topmost',True)
    screen3.after_idle(screen3.attributes,'-topmost',False)

    title=Label(screen3,text="E-commerce portal",bd=8,relief=GROOVE,font=("times new roman",40,"bold"),bg="yellow",fg="blue")
    title.pack(side=TOP,fill=X)

    p_id=StringVar()
    p_name=StringVar()
    p_seller=StringVar()
    p_ava=StringVar()
    p_type=StringVar()
    p_price=StringVar()

    search_by=StringVar()
    search_txt=StringVar()

#Manage frame=================

    Manage_Frame=Frame(screen3,bd=6,relief=RIDGE,bg="purple")
    Manage_Frame.place(x=20,y=100,width=480,height=580)

    m_title=Label(Manage_Frame, text="Manage products",font=("times new roman",25,"bold"),bg="purple",fg="white")
    m_title.grid(row=0, columnspan=2, pady=20)

    lbl_pid=Label(Manage_Frame, text="Product ID", font=("times new roman",20),bg="purple",fg="white")
    lbl_pid.grid(row=1,column=0,pady=15,sticky="w")

    txt_pid=Entry(Manage_Frame,textvariable=p_id, font=("times new roman",15),bd=5,relief=GROOVE)
    txt_pid.grid(row=1,column=1,padx=10,pady=10,sticky="w")

    lbl_pname=Label(Manage_Frame, text="Product Name", font=("times new roman",20),bg="purple",fg="white")
    lbl_pname.grid(row=2,column=0,pady=15,sticky="w")

    txt_pname=Entry(Manage_Frame, textvariable=p_name, font=("times new roman",15),bd=5,relief=GROOVE)
    txt_pname.grid(row=2,column=1,padx=10,pady=10,sticky="w")

    lbl_seller=Label(Manage_Frame, text="Product Seller", font=("times new roman",20),bg="purple",fg="white")
    lbl_seller.grid(row=3,column=0,pady=15,sticky="w")

    txt_seller=Entry(Manage_Frame, textvariable=p_seller ,font=("times new roman",15),bd=5,relief=GROOVE)
    txt_seller.grid(row=3,column=1,padx=10,pady=10,sticky="w")

    lbl_availability=Label(Manage_Frame, text="Availability", font=("times new roman",20),bg="purple",fg="white")
    lbl_availability.grid(row=4,column=0,pady=15,sticky="w")

    combo_availability=ttk.Combobox(Manage_Frame,textvariable=p_ava, font=("times new roman",15),state="readonly")
    combo_availability['values']=("Yes", "No")
    combo_availability.grid(row=4,column=1,padx=10,pady=10)

    lbl_type=Label(Manage_Frame, text="Product Type", font=("times new roman",20),bg="purple",fg="white")
    lbl_type.grid(row=5,column=0,pady=15,sticky="w")

    txt_type=Entry(Manage_Frame, textvariable=p_type, font=("times new roman",15),bd=5,relief=GROOVE)
    txt_type.grid(row=5,column=1,padx=10,pady=10,sticky="w")

    lbl_price=Label(Manage_Frame, text="Price", font=("times new roman",20),bg="purple",fg="white")
    lbl_price.grid(row=6,column=0,pady=15,sticky="w")

    txt_price=Entry(Manage_Frame, textvariable=p_price, font=("times new roman",15),bd=5,relief=GROOVE)
    txt_price.grid(row=6,column=1,padx=10,pady=10,sticky="w")

#Button frame==============

    Button_Frame=Frame(Manage_Frame,bd=6,relief=RIDGE,bg="purple")
    Button_Frame.place(x=10,y=500,width=450)

    Addbtn=Button(Button_Frame,text="Add",width=10, command=add_products).grid(row=0,column=0,padx=12,pady=10)
    Deletebtn=Button(Button_Frame,text="Delete",width=10, command=delete_values).grid(row=0,column=1,padx=12,pady=10)
    Updatebtn=Button(Button_Frame,text="Update",width=10, command=update_values).grid(row=0,column=2,padx=12,pady=10)
    Clrbtn=Button(Button_Frame,text="Clear",width=10, command=clear).grid(row=0,column=3,padx=12,pady=10)

#Detail frame====================

    Detail_Frame=Frame(screen3,bd=6,relief=RIDGE,bg="purple")
    Detail_Frame.place(x=530,y=100,width=750,height=580)

    lbl_search=Label(Detail_Frame, text="Search by", font=("times new roman",25),bg="purple",fg="white")
    lbl_search.grid(row=0,column=0,pady=15,sticky="w")

    combo_search=ttk.Combobox(Detail_Frame, textvariable=search_by, font=("times new roman",15),width=10, state="readonly")
    combo_search['values']=("pname", "pid", "pseller", "pava", "ptype", "pprice")
    combo_search.grid(row=0,column=1,padx=10,pady=10)

    txt_search=Entry(Detail_Frame, textvariable=search_txt, font=("times new roman",15),bd=5,relief=GROOVE)
    txt_search.grid(row=0,column=2,padx=10,pady=10,sticky="w")

    searchbtn=Button(Detail_Frame,text="Search",command=search_data, width=10).grid(row=0,column=3,padx=12,pady=10)
    showAllbtn=Button(Detail_Frame,text="Show All",width=10, command=print_data).grid(row=0,column=4,padx=12,pady=10)

#Table frame======================

    Table_Frame=Frame(Detail_Frame,bd=6,relief=RIDGE,bg="purple")
    Table_Frame.place(x=10,y=70,width=720,height=480)

    scroll_x=Scrollbar(Table_Frame, orient=HORIZONTAL)
    scroll_y=Scrollbar(Table_Frame, orient=VERTICAL)
    ecom=ttk.Treeview(Table_Frame, columns=("id", "name", "seller", "type", "Ava", "price"), xscrollcommand=scroll_x.set, yscrollcommand=scroll_y.set)
    scroll_x.pack(side=BOTTOM,fill=X)
    scroll_y.pack(side=RIGHT,fill=Y)
    scroll_x.config(command=ecom.xview)
    scroll_y.config(command=ecom.yview)
    ecom.heading("id", text="Product ID")
    ecom.heading("name", text="Product Name")
    ecom.heading("seller", text="Product Seller")
    ecom.heading("type", text="Product Type")
    ecom.heading("Ava", text="Availability")
    ecom.heading("price", text="Price")
    ecom['show']='headings'
    ecom.column("id", width=108)
    ecom.column("name", width=140)
    ecom.column("seller", width=110)
    ecom.column("type", width=110)
    ecom.column("Ava", width=110)
    ecom.column("price", width=110)
    ecom.pack(fill=BOTH, expand=1)
    ecom.bind("<ButtonRelease-1>",get_cursor)
    print_data()

login_screen()