from tkinter import *
from tkinter import messagebox
import sqlite3
root = Tk()
root.state('zoomed')

bus_logo = PhotoImage(file=".\\images\\Bus_for_project.png")
Label(root, image=bus_logo).grid(row=0, column=6, columnspan=15)

Label(root, text="Online Bus Booking System", font="arial 18 bold",
      bg='sky blue', fg='Red').grid(row=1, column=6, pady=20, columnspan=15)
Label(root, text="Add Bus Running Details", font="arial 14 bold",
      bg='light green', fg='green').grid(row=2, column=6, pady=20, columnspan=15)

Label(root, text="Bus Id").grid(row=3, column=2)
bus_id = Entry(root)
bus_id.grid(row=3, column=3)

Label(root, text="Running Date").grid(row=3, column=4)
running_date = Entry(root)
running_date.grid(row=3, column=5)

Label(root, text="Seat Available").grid(row=3, column=6)
seat_available = Entry(root)
seat_available.grid(row=3, column=7)


def add_run():
    b_id = bus_id.get()
    r = running_date.get()
    s = seat_available.get()

    con = sqlite3.Connection("Bus_database")
    cur = con.cursor()
    if bus_id.get() != "" and running_date.get() != "" and seat_available.get() != "":
        cur.execute("""insert into running_details(B_Id,Date,Seat_available)values(?,?,?)""", [b_id, r, s])
        con.commit()
        displaY()
        messagebox.showinfo("", "Bus Running details added successfully")
        con.close()
    else:
        messagebox.showerror("", "Please fill all the field")


Button(root, text='Add Run', fg='black', bg='light green',
       command=add_run).grid(row=3, column=8)


def displaY():
    Label(root, text=bus_id.get()+" "+running_date.get() +
          " "+seat_available.get()).grid(row=4, column=5)


def delete_run():
    b_id = bus_id.get()
    r = running_date.get()
    s = seat_available.get()

    con = sqlite3.Connection("Bus_database")
    cur = con.cursor()

    if b_id != "" and r != "":
        cur.execute("""delete from running_details where B_Id=? and Date=?""", [b_id, r])
        con.commit()
        displaY()
        messagebox.showinfo("", "Bus Running details deleted successfully")
        con.close()

    else:
        messagebox.showerror("", "Please fill all the field")


Button(root, text='Delete Run', fg='black', bg='Red',
       command=delete_run).grid(row=3, column=10)


def home():
    root.destroy()
    import add_bus_details


home_logo = PhotoImage(file=".\\images\\home.png")
Button(root, fg='black', bg='light green', image=home_logo,
       command=home).grid(row=4, column=10, padx=10)

root.mainloop()
