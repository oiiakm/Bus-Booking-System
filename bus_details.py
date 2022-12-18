from tkinter import *
from tkinter import messagebox
import sqlite3
root = Tk()
root.state("zoomed")

bus_logo = PhotoImage(file=".\\images\\Bus_for_project.png")
Label(root, image=bus_logo).grid(row=0, column=5, columnspan=15)

Label(root, text="Online Bus Booking System", font="arial 18 bold",
      bg='sky blue', fg='Red').grid(row=1, column=5, pady=20, columnspan=15)
Label(root, text="Add Bus Details", font="arial 14 bold", bg='light green',
      fg='green').grid(row=2, column=5, pady=20, columnspan=15)

Label(root, text="Bus ID").grid(row=3, column=1)
bus_id = Entry(root)
bus_id.grid(row=3, column=2)


Label(root, text="Bus Type").grid(row=3, column=3)
bus_type = StringVar()
bus_option = ["AC 2X2", "AC 3X2", "Non AC 2X2",
              "Non AC 3X2", "AC-Sleeper 2X1", "Non AC-Sleeper 2X1"]
bus_menu = OptionMenu(root, bus_type, *bus_option).grid(row=3, column=4)


Label(root, text="Capacity").grid(row=3, column=5)
capacity = Entry(root)
capacity.grid(row=3, column=6)

Label(root, text="Fare Rs").grid(row=3, column=7)
fare = Entry(root)
fare.grid(row=3, column=8)

Label(root, text="Opeartor ID").grid(row=3, column=9)
operator_id = Entry(root)
operator_id.grid(row=3, column=10)

Label(root, text="Route ID").grid(row=3, column=11)
route_id = Entry(root)
route_id.grid(row=3, column=12)


def add_bus():
    
    b_id=bus_id.get()
    b_type=bus_type.get()
    c=capacity.get()
    f=fare.get()
    op_id=operator_id.get() 
    r_id=route_id.get() 
    
    if b_id == "" and b_type== "" and c== "" and f== "" and op_id == "" and r_id == "":
        messagebox.showerror("", "Please enter bus details")

    elif b_id== "" and b_type== "" and c == "" and f== "" and op_id== "":
        messagebox.showerror("", "Please fill the field<Bus Id,From,Capacity,Fare and Operator Id>")

    elif b_type== "" and c== "" and f== "" and op_id== "" and r_id== "":
        messagebox.showerror("", "Please fill the field<From,Capacity,Fare ,Operator Id and Route Id>")
 
    else:
        con = sqlite3.Connection("Bus_database")
        cur = con.cursor()
        cur.execute("""insert into Bus_details(B_Id ,Bus_type,Capacity,Fare,R_Id, Op_Id)values(?,?,?,?,?,?)""",[b_id,b_type,c,f,op_id,r_id])
        con.commit()
        display()
        con.close()
        messagebox.showinfo("", "Bus details added successfully")


Button(root, text='Add', fg='black', bg='light green',
       command=add_bus).grid(row=3, column=13)


def display():
    Label(root, text=bus_id.get()+" "+bus_type.get()+" "+capacity.get()+" " +
          fare.get()+" "+operator_id.get()+" "+route_id.get()).grid(row=4, column=7)


def edit_bus():
    
    b_id=bus_id.get()
    b_type=bus_type.get()
    c=capacity.get()
    f=fare.get()
    op_id=operator_id.get() 
    r_id=route_id.get() 
    
    con = sqlite3.Connection("Bus_database")
    cur = con.cursor()
    
    
    if b_id == "" and b_type== "" and c== "" and f== "" and op_id == "" and r_id == "":
        messagebox.showerror("", "Please enter bus details")

    elif b_id== "" and b_type== "" and c == "" and f== "" and op_id== "":
        messagebox.showerror("", "Please fill the field<Bus Id,From,Capacity,Fare and Operator Id>")

    elif b_type== "" and c== "" and f== "" and op_id== "" and r_id== "":
        messagebox.showerror("", "Please fill the field<From,Capacity,Fare ,Operator Id and Route Id>")
 
    else:
        con = sqlite3.Connection("Bus_database")
        cur = con.cursor()
        cur.execute("""update Bus_details set Bus_type=?, Capacity=?,Fare=?,Op_Id=?,R_Id=? where B_Id=?""",[b_type,c,f,op_id,r_id,b_id])
        con.commit()
        display()
        con.close()
        messagebox.showinfo("", "Bus details edited successfully")



Button(root, text='Edit Bus', fg='black', bg='light green',
       command=edit_bus).grid(row=3, column=14)


def home():
    root.destroy()
    import add_bus_details


home_logo = PhotoImage(file=".\\images\\home.png")
Button(root, fg='black', bg='light green', image=home_logo,
       command=home).grid(row=4, column=14, pady=10)


root.mainloop()
