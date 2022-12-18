from tkinter import *
from tkinter import messagebox
import sqlite3
root = Tk()
root.state('zoomed')

bus_logo = PhotoImage(file=".\\images\\Bus_for_project.png")
Label(root, image=bus_logo).grid(row=0, column=6, columnspan=15)

Label(root, text="Online Bus Booking System", font="arial 18 bold",
      bg='sky blue', fg='Red').grid(row=1, column=6, pady=20, columnspan=15)
Label(root, text="Add Bus Operator Details", font="arial 14 bold",
      bg='light green', fg='green').grid(row=2, column=6, pady=20, columnspan=15)

Label(root, text="Operator Id").grid(row=3, column=2)
operator = Entry(root)
operator.grid(row=3, column=3)

Label(root, text="Name").grid(row=3, column=4)
name = Entry(root)
name.grid(row=3, column=5)

Label(root, text="Address").grid(row=3, column=6)
address = Entry(root)
address.grid(row=3, column=7)

Label(root, text="Phone").grid(row=3, column=8)
phone = Entry(root)
phone.grid(row=3, column=9)

Label(root, text="Email").grid(row=3, column=10)
email = Entry(root)
email.grid(row=3, column=11)


def add_bus():
    op=operator.get()
    a=address.get()
    n=name.get()
    p=phone.get()
    e=email.get() 
    
    con = sqlite3.Connection("Bus_database")
    cur = con.cursor()

    if op!= ""and a!= "" and p!= "" and e!= "" and n!= "":
        cur.execute("""insert into Operator_details(Op_Id,Name,Address,Email,Phone)values(?,?,?,?,?)""",[op,n,a,e,p])
        con.commit()
        display()
        con.close()
        messagebox.showinfo("", "Bus operator added successfully")
    else:
        messagebox.showerror("", "Please fill all the field")


Button(root, text='Add', fg='black', bg='light green',
       command=add_bus).grid(row=3, column=13)


def display():
    Label(root, text=operator.get()+" "+name.get()+" "+address.get() +
          " "+phone.get()+" "+email.get()).grid(row=4, column=8)


def edit_bus():
    op=operator.get()
    a=address.get()
    n=name.get()
    p=phone.get()
    e=email.get() 
    
    con = sqlite3.Connection("Bus_database")
    cur = con.cursor()

    if op!= ""and a!= "" and p!= "" and e!= "" and n!= "":
        cur.execute("""update Operator_details set Name=?,Address=?,Phone=?,Email=? where Op_Id=?""",[n,a,p,e,op])
        con.commit()
        display()
        con.close()
        messagebox.showinfo("", "Bus operator updated successfully")
    else:
        messagebox.showerror("", "Please fill all the field")


Button(root, text='Edit', fg='black', bg='light green',
       command=edit_bus).grid(row=3, column=15)


def home():
    root.destroy()
    import add_bus_details


home_logo = PhotoImage(file=".\\images\\home.png")

Button(root, fg='black', bg='light green', image=home_logo,
       command=home).grid(row=4, column=15)

root.mainloop()
