from tkinter import*

root= Tk()
root.state('zoomed')

bus_logo =PhotoImage(file=".\\images\\Bus_for_project.png")
Label(root,image = bus_logo).grid(row = 0 , column = 6,columnspan=35)

Label(root,text = "Online Bus Booking System", font = "arial 18 bold",bg = 'sky blue', fg ='Red').grid(row = 1, column = 6, pady = 20)

Label(root,text = "Add New Details to DataBase", font = "arial 14 bold", fg ='green').grid(row = 2, column = 6, pady = 20)

def new_operator():
    root.destroy()
    import bus_operator_details

def new_bus():
    root.destroy()
    import  bus_details 

def new_route():
    root.destroy()
    import  bus_route_details

def new_run():
    root.destroy()
    import bus_running_details as bus_running_details



Button(root, text= 'New Operator',fg ='black' ,bg= 'light green',command=new_operator).grid(row= 3 ,column = 2)
Button(root, text= 'New Bus',fg ='black' ,bg= 'orange red',command=new_bus).grid(row= 3 ,column = 3,padx=20)
Button(root, text= 'New Route',fg ='black' ,bg= 'steelBlue1',command=new_route).grid(row= 3 ,column = 4,padx=20)
Button(root, text= 'New Run',fg ='black' ,bg= 'rosy brown',command=new_run).grid(row= 3 ,column = 5,padx=20)

root.mainloop()
