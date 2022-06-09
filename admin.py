import uuid
import pyodbc

from tkinter import *
from tkinter import ttk
import mysql.connector


from datetime import date
import mysql.connector

from tkinter import messagebox
from common import get_dpt, get_role, get_staff_name

class Admin:
    def __init__(self, root, staff_id):

        self.root = root
        self.root.title("HOSPITAL QUEUEING SYSTEM")
        screen_width = root.winfo_screenwidth()
        screen_height = root.winfo_screenheight()
        self.root.geometry("{}x{}+0+0".format(screen_width, screen_height))
        self.root.configure(background="grey")

        conn = mysql.connector.connect(
		  	host="localhost",
		  	user="root",
		  	password="password#123",
            database="hospital_db"
		)
        
        c = conn.cursor()

        t0 = StringVar()
        t1 = StringVar()
        t2 = StringVar()
        t3 = StringVar()
        t4 = StringVar()
        t5 = StringVar()
        t6 = StringVar()
        t7 = StringVar()
        t8 = StringVar()
        t9 = StringVar()
        t10 = StringVar()


        def clear_department():
            t1.set('')
        
        def clear_role():
            t2.set('')
            t3.set('')
        
        def clear_specialist():
            t4.set('')
            t5.set('')
            t6.set('')
            t7.set('')
            t8.set('')

        def reload_role_departments():
            txtrole_dptmt.delete(0,END)

            c.execute("SELECT name FROM department GROUP BY name ORDER BY name desc")
            role_dpts = []

            for row in c.fetchall():
                role_dpts.append(row[0])

            txtrole_dptmt['values'] = role_dpts
        

        def reload_specialist_departments():
            txtspecialist_dptmt.delete(0,END)

            c.execute("SELECT department FROM role GROUP BY department ORDER BY department desc")
            role_dpts = []

            for row in c.fetchall():
                role_dpts.append(row[0])

            txtspecialist_dptmt['values'] = role_dpts


        def reload_specialist_roles():
            txtspecialist_role.delete(0,END)
            c.execute("SELECT name FROM role GROUP BY name ORDER BY name desc")
            roles = []

            for row in c.fetchall():
                roles.append(row[0])

            txtspecialist_role['values'] = roles

        def save_department():
            if t1.get() == '':
                msg = 'Enter Department'
                messagebox.showerror('Error', msg)
                return

            id = str(uuid.uuid4())
            tdate = date.today().strftime("%Y-%m-%d")
            name = t1.get().upper()

            query1 = "SELECT name FROM department WHERE name LIKE '{}'".format(name)
            c.execute(query1)

            entry = c.fetchall()
            if entry == []:
                query = "INSERT INTO department (id, date, name) VALUES (%s, %s, %s)"
                val = (id, tdate,name)
                c.execute(query, val)
                conn.commit()

                msg = t1.get()  + ' Saved'
                messagebox.showinfo('Ok',msg)

            else:
                messagebox.showerror('ERROR',"The department already exists")
            
            reload_role_departments()
            clear_department()
        
        def save_role():
            if t2.get() == '':
                messagebox.showerror('Error', "Input department")
                return

            if t3.get() == '':
                messagebox.showerror('Error', "Input role")
                return

            id = str(uuid.uuid4())
            tdate = date.today().strftime("%Y-%m-%d")
            department = t2.get().upper()
            name = t3.get().upper()
          
            query1 = "SELECT name FROM role WHERE department LIKE '{}' AND name LIKE '{}'".format(department, name)
            c.execute(query1)
            entry = c.fetchall()
            if entry == []:
                query = "INSERT INTO role(id, date, department, name) VALUES (%s, %s, %s, %s)"
                val= (id, tdate, department, name)
                
                c.execute(query, val)
                
                conn.commit()

                messagebox.showinfo('Ok', t3.get().upper() + ' role saved')

                reload_specialist_departments()
                reload_specialist_roles()
            else:
                messagebox.showerror('ERROR',"The role already exists")
            
            clear_role()
                
        def get_role_dpt():
            c.execute("SELECT department FROM role GROUP BY department ORDER BY department desc")
            role_dpts = []

            for row in c.fetchall():
                role_dpts.append(row[0])

            return role_dpts


        def save_specialist():
            if t4.get() == '':
                messagebox.showerror('ERROR', 'Enter department')
                return

            if t5.get() == '':
                messagebox.showerror('ERROR','Enter role')

            if t6.get() == '':
                messagebox.showerror('ERROR','Enter staff Id')
                return

            id=  str(uuid.uuid4())
            tdate = date.today().strftime("%y-%m-%d")
            department = t4.get().upper()
            role = t5.get().upper()
            staff_id = t6.get().upper()
            queue = 0
            queue_length = 0

            query1 = "SELECT * FROM role WHERE department LIKE '{}' AND name LIKE '{}'".format(department, role)
            c.execute(query1)
            user_roles = c.fetchall()
            if user_roles == []:
                messagebox.showerror('ERROR', "{} is not a role under {}".format(role, department))
                
            else:
                query2 = "SELECT department, role, staff_id FROM specialist WHERE department LIKE '{}' AND  role LIKE '{}' AND staff_id LIKE '{}'".format(department, role, staff_id)
                c.execute(query2)
                entry = c.fetchall()
                if entry == []:
                    query = "INSERT INTO specialist(id, date, department, role, staff_id, queue, queue_length) VALUES (%s,%s,%s,%s,%s,%s,%s)"
                    val = (id, tdate, department, role, staff_id, queue, queue_length)
                    c.execute(query, val)
                    conn.commit()

                    name = get_staff_name(staff_id) 
                    
                    messagebox.showinfo('Ok', '{} saved'.format(name))

                else:
                    messagebox.showerror('ERROR',"The specialist exists as a {} under {}".format(role, department))
                    
            clear_specialist()

        def add_user():
            frame.destroy()
            import employees
            employees.Employees(root, staff_id)

        def open_reports():
            frame.destroy()
            import filters
            filters.Reports(root, staff_id)
           
        def generate_all_data_report():
            try:
                import excel
                messagebox.showinfo('SUCCESS!','The database entries report has been successfullt updated')
            
            except PermissionError:
                messagebox.showerror('ERROR!','A similar file under Database Entries Report.xlsx exists')
            
        def exit_admin():
            frame.destroy()
            import usertype
            usertype.UserType(root)

        frame = Frame(root, )
        frame.pack(fill=BOTH, expand=True, padx=(0, 0))

        formlbl = Label(frame, text="Admin Form", font=("times new roman", 40, "bold", "italic"), bg="#a9acb6",
                        fg="black", relief=GROOVE).place(x=500, y=5)
        
        lbldepartment = Label(frame, text="Department:", compound=LEFT, bg="#a9acb6",
                         font=("times new roman", 12, "bold",), ).place(x=5, y=110)
        txtdepartment = Entry(frame, width=28, font=("", 13), bg="#a9a9a9", textvariable=t1)
        txtdepartment.place(x=175, y=110)

        Button(frame, text="Save Department", command=save_department, font=("", 10, "bold",), bg="#068481", fg="#b0c4de",
                    width=15).place(x=450, y=150)


        Label(frame, text="Department:", compound=LEFT, bg="#a9acb6",
            font=("times new roman", 12, "bold",), ).place(x=5, y=240)
        txtrole_dptmt = ttk.Combobox(frame, width=30, textvariable=t2)
        txtrole_dptmt.place(x=175, y=240)
        txtrole_dptmt['values'] = get_dpt()

        lblrole = Label(frame, text="Role:", compound=LEFT, bg="#a9acb6",
                         font=("times new roman", 12, "bold",), ).place(x=5, y=280)
        txtrole = Entry(frame, width=28, font=("", 13), bg="#a9a9a9", textvariable=t3)
        txtrole.place(x=175, y=280)

        Button(frame, text="Save Role", command=save_role, font=("", 10, "bold",), bg="#068481", fg="#b0c4de",
                    width=15).place(x=450, y=320)
        
        lblspecialist_dptmt = Label(frame, text="Specialist Department:", compound=LEFT, bg="#a9acb6",
                        font=("times new roman", 12, "bold",), ).place(x=5, y=400)
        txtspecialist_dptmt = ttk.Combobox(frame, width=30, textvariable=t4)
        txtspecialist_dptmt.place(x=175, y=400)
        txtspecialist_dptmt['values'] = get_role_dpt()

        lblspecialist_role = Label(frame, text="Specialist Role:", compound=LEFT, bg="#a9acb6",
                        font=("times new roman", 12, "bold",), ).place(x=5, y=440)
        txtspecialist_role = ttk.Combobox(frame, width=30, textvariable=t5)
        txtspecialist_role.place(x=175, y=440)
        txtspecialist_role['values'] = get_role()

        Label(frame, text="Staff Id:", compound=LEFT, bg="#a9acb6",
                         font=("times new roman", 12, "bold",), ).place(x=5, y=480)
        Entry(frame, width=28, font=("", 13), bg="#a9a9a9", textvariable=t6).place(x=175, y=480)

        Button(frame, text="Save Specialist", command=save_specialist, font=("", 10, "bold",), bg="#068481", fg="#b0c4de",
                    width=15).place(x=450, y=520)
        
        Button(frame, text="Add Users", command=add_user, font=("", 10, "bold",), bg="#068481", fg="#b0c4de",
                    width=15).place(x=200, y=50)
        
        Button(frame, text="View Reports", command=open_reports, font=("", 10, "bold",), bg="#068481", fg="#b0c4de",
                    width=15).place(x=1050, y=50)
        
        Button(frame, text="Generate a Reports on all Data", command=generate_all_data_report, font=("", 10, "bold",), bg="#068481", fg="#b0c4de",
                    ).place(x=1050, y=90)

        Button(frame, text="Exit", command=exit_admin, font=("", 10, "bold",), bg="#1b6453", fg="#eab5c5",
                    width=15).place(x=50, y=50)

# root = Tk()
# Admin(root, 'staff_id') 
# root.mainloop()
