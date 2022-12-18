from tkinter import *
root = Tk()
root.state('zoomed')
bus_logo = PhotoImage(file=".\\images\\Bus_for_project.png")
Label(root, image=bus_logo).grid(row=0, column=1, padx=600)

Label(root, text="Welcome To Online Bus Booking System",
      bg="light blue", fg="Red", font=50).grid(row=1, column=1)

Label(root, text="Press any key to continue...").grid(
    row=7, column=1, pady=300)


def booking_details(k=0):
    root.destroy()
    import booking_details


root.bind("<KeyPress>", booking_details)


root.mainloop()
