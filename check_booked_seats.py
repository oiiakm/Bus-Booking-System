from tkinter import *
from tkinter import messagebox

import sqlite3
root = Tk()
root.state('zoomed')
bus_logo = PhotoImage(file=".\\images\\Bus_for_project.png")
Label(root, image=bus_logo).grid(row=0, column=5, columnspan=10)

Label(root, text="Online Bus Booking System", bg="Light Blue",
      fg="Red", font="Arial 20").grid(row=1, column=5, columnspan=10)
Label(root, text="Check Your Booking", bg="Light Green",
      font="Arial 10").grid(row=2, column=5, pady=15, columnspan=10)

Label(root, text="Enter Your Mobile Number: ").grid(row=3, column=1, pady=15)
mobile_number = Entry(root)
mobile_number.grid(row=3, column=2)



def check_booking():
    if mobile_number.get() == "":
        messagebox.showerror("Error", "Please <Enter Your Mobile Number>")
    elif len(mobile_number.get())!=10:
        messagebox.showwarning("","Please enter valid <Mobile Number>")
    
    else:

        con = sqlite3.Connection("Bus_database")
        cur = con.cursor() 
    
        cur.execute(
            '''select b.Passenger_name, b.Gender, b.No_of_passenger, b.Phone, b.Age, Fare, Name, b.Date,b.Booking_ref,b.Boarding_station,b.Journey_date from Operator_details as o,Booking_history as b, Bus_details bus, Running_details as r,Route_details as t where b.Phone=? ''', [mobile_number.get()])
        
        f = cur.fetchall()

        for i in f:

            Label(root, text="Passengers:").grid(row=4, column=10)
            Label(root, text=i[0]).grid(row=4, column=11)

            Label(root, text="Gender:").grid(row=4, column=14)
            Label(root, text=i[1]).grid(row=4, column=15)

            Label(root, text="No of Seats:").grid(row=5, column=10)
            Label(root, text=i[2]).grid(row=5, column=11)

            Label(root, text="Phone:").grid(row=5, column=14)
            Label(root, text=i[3]).grid(row=5, column=15)

            Label(root, text="Age:").grid(row=6, column=10)
            Label(root, text=i[4]).grid(row=6, column=11)

            Label(root, text="Fare Rs:").grid(row=6, column=14)
            Label(root, text=int(i[2])*int(i[5])).grid(row=6, column=15)

            Label(root, text="Booking Ref:").grid(row=7, column=10)
            Label(root, text=i[8]).grid(row=7, column=11)

            Label(root, text="Bus Detail:").grid(row=7, column=14)
            Label(root, text=i[6]).grid(row=7, column=15)

            Label(root, text="Travel On:").grid(row=8, column=10)
            Label(root, text=i[10]).grid(row=8, column=11)

            Label(root, text="Booked On:").grid(row=8, column=14)
            Label(root, text=i[7]).grid(row=8, column=15)

            Label(root, text="No of Seats:").grid(row=9, column=10)
            Label(root, text=i[2]).grid(row=9, column=11)

            Label(root, text="Boarding Point:").grid(row=9, column=14)
            Label(root, text=i[9]).grid(row=9, column=15)
            
            Label(root, text = "Total amount of Rs").grid(row = 10, column = 11)
            Label(root, text = float(i[2])*float(i[5])).grid(row = 10, column = 12)
            Label(root, text = "/- to be paid at the time of boarding the bus").grid(row = 10, column = 13)

            con.close()
            break;


Button(root, text='Check Booking', command=check_booking).grid(row=3, column=3)


root.mainloop()
