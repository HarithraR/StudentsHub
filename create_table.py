import tkinter as tk
from tkinter import ttk, messagebox
import mysql.connector 
from tkinter import *
from tkinter import messagebox

tkWindow = Tk()  
tkWindow.geometry('250x200')  
tkWindow.title('COLLEGE DETAILS')

def showMsg():  
    messagebox.showinfo(student())
    
def student():    
    def GetValue(event):
        e1.delete(0, END)
        e2.delete(0, END)
        e3.delete(0, END)
        e4.delete(0, END)
        e5.delete(0, END)
        e6.delete(0, END)
        row_id = listBox.selection()[0]
        select = listBox.set(row_id)
        e1.insert(0,select['id'])
        e2.insert(0,select['S_name'])
        e3.insert(0,select['gender'])
        e4.insert(0,select['age'])
        e5.insert(0,select['contact'])
        e6.insert(0,select['S_mail'])


    def Add():
        S_ID = e1.get()
        S_name = e2.get()
        Gender = e3.get()
        Age = e4.get()
        Contact = e5.get()
        Mail = e6.get()

        mysqldb=mysql.connector.connect(host="localhost",user="root",password="Hari@1314",database="harithra")
        mycursor=mysqldb.cursor()

        try:
           sql = "INSERT INTO student (id,S_name,gender,age,contact,S_mail) VALUES (%s, %s, %s, %s, %s, %s)"
           val = (S_ID,S_name,Gender,Age,Contact,Mail)
           mycursor.execute(sql, val)
           mysqldb.commit()
           lastid = mycursor.lastrowid
           messagebox.showinfo("information", "Student inserted successfully...")
           e1.delete(0, END)
           e2.delete(0, END)
           e3.delete(0, END)
           e4.delete(0, END)
           e5.delete(0, END)
           e6.delete(0, END)
           e1.focus_set()
        except Exception as e:
           print(e)
           mysqldb.rollback()
           mysqldb.close()


    def update():
        S_ID = e1.get()
        S_name = e2.get()
        Gender = e3.get()
        Age = e4.get()
        Contact = e5.get()
        Mail = e6.get()
        mysqldb=mysql.connector.connect(host="localhost",user="root",password="Hari@1314",database="harithra")
        mycursor=mysqldb.cursor()

        try:
           sql = "Update student set S_name= %s,gender= %s,age= %s,contact=%s,S_mail=%s where id= %s"
           val = (S_ID,S_name,Gender,Age,Contact,Mail)
           mycursor.execute(sql, val)
           mysqldb.commit()
           lastid = mycursor.lastrowid
           messagebox.showinfo("information", "Record Updated successfully...")

           e1.delete(0, END)
           e2.delete(0, END)
           e3.delete(0, END)
           e4.delete(0, END)
           e5.delete(0, END)
           e6.delete(0, END)
           e1.focus_set()

        except Exception as e:

           print(e)
           mysqldb.rollback()
           mysqldb.close()

    def delete():
        S_ID = e1.get()

        mysqldb=mysql.connector.connect(host="localhost",user="root",password="Hari@1314",database="harithra")
        mycursor=mysqldb.cursor()

        try:
           sql = "delete from student where ID = %s"
           val = (S_ID,)
           mycursor.execute(sql, val)
           mysqldb.commit()
           lastid = mycursor.lastrowid
           messagebox.showinfo("information", "Record Deleted successfully...")

           e1.delete(0, END)
           e2.delete(0, END)
           e3.delete(0, END)
           e4.delete(0, END)
           e5.delete(0, END)
           e6.delete(0, END)
           e1.focus_set()

        except Exception as e:

           print(e)
           mysqldb.rollback()
           mysqldb.close()

    def show():
            mysqldb = mysql.connector.connect(host="localhost", user="root", password="Hari@1314", database="harithra")
            mycursor = mysqldb.cursor()
            mycursor.execute("SELECT id,S_name,gender,age,contact,S_mail from student")
            records = mycursor.fetchall()
            print(records)

            for i, (id,S_name,gender,age,contact,S_mail) in enumerate(records, start=1):
                listBox.insert("", "end", values=(id,S_name,gender,age,contact,S_mail))
                mysqldb.close()

    root = Tk()
    root.geometry("1220x550")
    global e1
    global e2
    global e3
    global e4
    global e5
    global e6 

    tk.Label(root, text="STUDENTS DETAILS", fg="dark grey", font=(None, 20)).place(x=400, y=10)

    tk.Label(root, text="Student ID").place(x=10, y=70)
    Label(root, text="Student Name").place(x=10, y=90)
    Label(root, text="Gender").place(x=10, y=110)
    Label(root, text="Age").place(x=10, y=130)
    Label(root, text="Contact").place(x=10, y=150)
    Label(root, text="Mail").place(x=10, y=170)

    e1 = Entry(root)
    e1.place(x=140, y=70)

    e2 = Entry(root)
    e2.place(x=140, y=90)

    e3 = Entry(root)
    e3.place(x=140, y=110)

    e4 = Entry(root)
    e4.place(x=140, y=130)

    e5 = Entry(root)
    e5.place(x=140, y=150)

    e6 = Entry(root)
    e6.place(x=140, y=170)

    Button(root, text="Add",command = Add,height=3, width= 13).place(x=30, y=210)
    Button(root, text="Update",command = update,height=3, width= 13).place(x=140, y=210)
    Button(root, text="Delete",command = delete,height=3, width= 13).place(x=250, y=210)

    cols = ('id','S_name','gender','age','contact','S_mail')
    listBox = ttk.Treeview(root, columns=cols, show='headings' )

    for col in cols:
        listBox.heading(col, text=col)
        listBox.grid(row=1, column=0, columnspan=2)
        listBox.place(x=10, y=300)

    show()
    listBox.bind('<Double-Button-1>',GetValue)

    root.mainloop()
def instructor():
    def GetValue(event):
        e1.delete(0, END)
        e2.delete(0, END)
        e3.delete(0, END)
        e4.delete(0, END)
        e5.delete(0, END)
        e6.delete(0, END)
        row_id = listBox.selection()[0]
        select = listBox.set(row_id)
        e1.insert(0,select['I_ID'])
        e2.insert(0,select['I_name'])
        e3.insert(0,select['I_gender'])
        e4.insert(0,select['I_age'])
        e5.insert(0,select['I_contact'])
        e6.insert(0,select['I_mail'])


    def Add():
        S_ID = e1.get()
        S_name = e2.get()
        Gender = e3.get()
        Age = e4.get()
        Contact = e5.get()
        Mail = e6.get()

        mysqldb=mysql.connector.connect(host="localhost",user="root",password="Hari@1314",database="harithra")
        mycursor=mysqldb.cursor()

        try:
           sql = "INSERT INTO instructor (I_ID,I_name,I_gender,I_age,I_contact,I_mail) VALUES (%s, %s, %s, %s, %s, %s)"
           val = (S_ID,S_name,Gender,Age,Contact,Mail)
           mycursor.execute(sql, val)
           mysqldb.commit()
           lastid = mycursor.lastrowid
           messagebox.showinfo("information", "Instructor inserted successfully...")
           e1.delete(0, END)
           e2.delete(0, END)
           e3.delete(0, END)
           e4.delete(0, END)
           e5.delete(0, END)
           e6.delete(0, END)
           e1.focus_set()
        except Exception as e:
           print(e)
           mysqldb.rollback()
           mysqldb.close()


    def update():
        S_ID = e1.get()
        S_name = e2.get()
        Gender = e3.get()
        Age = e4.get()
        Contact = e5.get()
        Mail = e6.get()
        mysqldb=mysql.connector.connect(host="localhost",user="root",password="Hari@1314",database="harithra")
        mycursor=mysqldb.cursor()

        try:
           sql = "Update instructor set I_name= %s,I_gender= %s,I_age= %s,I_contact=%s,I_mail=%s where I_ID= %s"
           val = (S_ID,S_name,Gender,Age,Contact,Mail)
           mycursor.execute(sql, val)
           mysqldb.commit()
           lastid = mycursor.lastrowid
           messagebox.showinfo("information", "Record Updated successfully...")

           e1.delete(0, END)
           e2.delete(0, END)
           e3.delete(0, END)
           e4.delete(0, END)
           e5.delete(0, END)
           e6.delete(0, END)
           e1.focus_set()

        except Exception as e:

           print(e)
           mysqldb.rollback()
           mysqldb.close()

    def delete():
        S_ID = e1.get()

        mysqldb=mysql.connector.connect(host="localhost",user="root",password="Hari@1314",database="harithra")
        mycursor=mysqldb.cursor()

        try:
           sql = "delete from instructor where I_ID = %s"
           val = (S_ID,)
           mycursor.execute(sql, val)
           mysqldb.commit()
           lastid = mycursor.lastrowid
           messagebox.showinfo("information", "Record Deleted successfully...")

           e1.delete(0, END)
           e2.delete(0, END)
           e3.delete(0, END)
           e4.delete(0, END)
           e5.delete(0, END)
           e6.delete(0, END)
           e1.focus_set()

        except Exception as e:

           print(e)
           mysqldb.rollback()
           mysqldb.close()

    def show():
            mysqldb = mysql.connector.connect(host="localhost", user="root", password="Hari@1314", database="harithra")
            mycursor = mysqldb.cursor()
            mycursor.execute("SELECT I_ID,I_name,I_gender,I_age,I_contact,I_mail from instructor")
            records = mycursor.fetchall()
            print(records)

            for i, (I_ID,I_name,I_gender,I_age,I_contact,I_mail) in enumerate(records, start=1):
                listBox.insert("", "end", values=(I_ID,I_name,I_gender,I_age,I_contact,I_mail))
                mysqldb.close()

    root = Tk()
    root.geometry("1220x550")
    global e1
    global e2
    global e3
    global e4
    global e5
    global e6

    tk.Label(root, text="INSTRUCTOR DETAILS", fg="dark grey", font=(None, 20)).place(x=400, y=10)

    tk.Label(root, text="Instructor ID").place(x=10, y=70)
    Label(root, text="Instructor Name").place(x=10, y=90)
    Label(root, text="Gender").place(x=10, y=110)
    Label(root, text="Age").place(x=10, y=130)
    Label(root, text="Contact").place(x=10, y=150)
    Label(root, text="Mail").place(x=10, y=170)

    e1 = Entry(root)
    e1.place(x=140, y=70)

    e2 = Entry(root)
    e2.place(x=140, y=90)

    e3 = Entry(root)
    e3.place(x=140, y=110)

    e4 = Entry(root)
    e4.place(x=140, y=130)

    e5 = Entry(root)
    e5.place(x=140, y=150)

    e6 = Entry(root)
    e6.place(x=140, y=170)

    Button(root, text="Add",command = Add,height=3, width= 13).place(x=30, y=210)
    Button(root, text="Update",command = update,height=3, width= 13).place(x=140, y=210)
    Button(root, text="Delete",command = delete,height=3, width= 13).place(x=250, y=210)

    cols = ('I_ID','I_name','I_gender','I_age','I_contact','I_mail')
    listBox = ttk.Treeview(root, columns=cols, show='headings' )

    for col in cols:
        listBox.heading(col, text=col)
        listBox.grid(row=1, column=0, columnspan=2)
        listBox.place(x=10, y=300)

    show()
    listBox.bind('<Double-Button-1>',GetValue)

    root.mainloop()
    
def trans():
    def GetValue(event):
        e1.delete(0, END)
        e2.delete(0, END)
        e3.delete(0, END)
        e4.delete(0, END)
        row_id = listBox.selection()[0]
        select = listBox.set(row_id)
        e1.insert(0,select['T_ID'])
        e2.insert(0,select['T_name'])
        e3.insert(0,select['S_ID'])
        e4.insert(0,select['T_date'])

    def Add():
        tr_ID = e1.get()
        tr_name = e2.get()
        s_id = e3.get()
        t_date = e4.get()

        mysqldb=mysql.connector.connect(host="localhost",user="root",password="Hari@1314",database="harithra")
        mycursor=mysqldb.cursor()

        try:
           sql = "INSERT INTO transactions (T_ID,T_name,S_ID,T_date) VALUES (%s, %s, %s, %s)"
           val = (tr_ID,tr_name,s_id,t_date)
           mycursor.execute(sql, val)
           mysqldb.commit()
           lastid = mycursor.lastrowid
           messagebox.showinfo("information", "Transaction details inserted successfully...")
           e1.delete(0, END)
           e2.delete(0, END)
           e3.delete(0, END)
           e4.delete(0, END)
           e1.focus_set()
        except Exception as e:
           print(e)
           mysqldb.rollback()
           mysqldb.close()
 
    def delete():
        T_ID = e1.get()

        mysqldb=mysql.connector.connect(host="localhost",user="root",password="Hari@1314",database="harithra")
        mycursor=mysqldb.cursor()

        try:
           sql = "delete from transactions where T_ID = %s"
           val = (T_ID,)
           mycursor.execute(sql, val)
           mysqldb.commit()
           lastid = mycursor.lastrowid
           messagebox.showinfo("information", "Record Deleted successfully...")

           e1.delete(0, END)
           e2.delete(0, END)
           e3.delete(0, END)
           e4.delete(0, END)
           e1.focus_set()

        except Exception as e:

           print(e)
           mysqldb.rollback()
           mysqldb.close()


    def show():
            mysqldb = mysql.connector.connect(host="localhost", user="root", password="Hari@1314", database="harithra")
            mycursor = mysqldb.cursor()
            mycursor.execute("SELECT T_ID,T_name,S_ID,T_date from transactions")
            records = mycursor.fetchall()
            print(records)

            for i, (T_ID,T_name,S_ID,T_date) in enumerate(records, start=1):
                listBox.insert("", "end", values=(T_ID,T_name,S_ID,T_date))
                mysqldb.close()

    root = Tk()
    root.geometry("1220x550")
    global e1
    global e2
    global e3
    global e4

    tk.Label(root, text="Transaction DETAILS", fg="dark grey", font=(None, 20)).place(x=400, y=10)

    tk.Label(root, text="Transaction ID").place(x=10, y=70)
    Label(root, text="Name").place(x=10, y=90)
    Label(root, text="Student Id").place(x=10, y=110)
    Label(root, text="Transaction date").place(x=10, y=130)

    e1 = Entry(root)
    e1.place(x=140, y=70)

    e2 = Entry(root)
    e2.place(x=140, y=90)

    e3 = Entry(root)
    e3.place(x=140, y=110)

    e4 = Entry(root)
    e4.place(x=140, y=130)


    Button(root, text="Add",command = Add,height=3, width= 13).place(x=30, y=210)
    Button(root, text="Delete",command = delete,height=3, width= 13).place(x=250, y=210)


    cols = ('T_ID','T_name','S_ID','T_date')
    listBox = ttk.Treeview(root, columns=cols, show='headings' )

    for col in cols:
        listBox.heading(col, text=col)
        listBox.grid(row=1, column=0, columnspan=2)
        listBox.place(x=10, y=300)

    show()
    listBox.bind('<Double-Button-1>',GetValue)

    root.mainloop()
    
def sub():
    def GetValue(event):
        e1.delete(0, END)
        e2.delete(0, END)
        e3.delete(0, END)
        row_id = listBox.selection()[0]
        select = listBox.set(row_id)
        e1.insert(0,select['C_ID'])
        e2.insert(0,select['C_name'])
        e3.insert(0,select['Year_join'])


    def Add():
        C_ID = e1.get()
        C_name = e2.get()
        Year_join = e3.get()

        mysqldb=mysql.connector.connect(host="localhost",user="root",password="Hari@1314",database="harithra")
        mycursor=mysqldb.cursor()

        try:
           sql = "INSERT INTO courses (C_ID,C_name,Year_join) VALUES (%s, %s, %s)"
           val = (C_ID,C_name,Year_join)
           mycursor.execute(sql, val)
           mysqldb.commit()
           lastid = mycursor.lastrowid
           messagebox.showinfo("information", "Course inserted successfully...")
           e1.delete(0, END)
           e2.delete(0, END)
           e3.delete(0, END)
           e1.focus_set()
        except Exception as e:
           print(e)
           mysqldb.rollback()
           mysqldb.close()

    def delete():
        C_ID = e1.get()

        mysqldb=mysql.connector.connect(host="localhost",user="root",password="Hari@1314",database="harithra")
        mycursor=mysqldb.cursor()

        try:
           sql = "delete from courses where C_ID = %s"
           val = (C_ID,)
           mycursor.execute(sql, val)
           mysqldb.commit()
           lastid = mycursor.lastrowid
           messagebox.showinfo("information", "Record Deleted successfully...")

           e1.delete(0, END)
           e2.delete(0, END)
           e3.delete(0, END)
           e1.focus_set()

        except Exception as e:

           print(e)
           mysqldb.rollback()
           mysqldb.close()

    def show():
            mysqldb = mysql.connector.connect(host="localhost", user="root", password="Hari@1314", database="harithra")
            mycursor = mysqldb.cursor()
            mycursor.execute("SELECT C_ID,C_name,Year_join FROM courses")
            records = mycursor.fetchall()
            print(records)

            for i, (C_ID,C_name,Year_join) in enumerate(records, start=1):
                listBox.insert("", "end", values=(C_ID,C_name,Year_join))
                mysqldb.close()

    root = Tk()
    root.geometry("1220x550")
    global e1
    global e2
    global e3

    tk.Label(root, text="COURSE DETAILS", fg="dark grey", font=(None, 20)).place(x=400, y=10)

    tk.Label(root, text="Course ID").place(x=10, y=70)
    Label(root, text="Course Name").place(x=10, y=90)
    Label(root, text="Year of introduce").place(x=10, y=110)

    e1 = Entry(root)
    e1.place(x=140, y=70)

    e2 = Entry(root)
    e2.place(x=140, y=90)

    e3 = Entry(root)
    e3.place(x=140, y=110)

    Button(root, text="Add",command = Add,height=3, width= 13).place(x=30, y=210)
    Button(root, text="Delete",command = delete,height=3, width= 13).place(x=250, y=210)

    cols = ('C_ID','C_name','Year_join')
    listBox = ttk.Treeview(root, columns=cols, show='headings' )

    for col in cols:
        listBox.heading(col, text=col)
        listBox.grid(row=1, column=0, columnspan=2)
        listBox.place(x=10, y=300)

    show()
    listBox.bind('<Double-Button-1>',GetValue)
    
    #root.config(bg='Grey')

    root.mainloop()
button1 = Button(tkWindow,
 	text = 'STUDENT',
 	command = showMsg) 
button2 = Button(tkWindow,
    text = 'INSTRUCTOR',
    command = instructor)
button3 = Button(tkWindow,
    text = 'TRANSACTION',
    command = trans)
button4 = Button(tkWindow,
    text = 'COURSES',
    command = sub) 

button1.pack()  
button2.pack()  
button3.pack()
button4.pack()


tkWindow.mainloop()