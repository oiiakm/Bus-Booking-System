import sqlite3
con = sqlite3.connect("Bus_database")
cur = con.cursor()

cur.execute("CREATE TABLE Operator_details (Op_Id INT PRIMARY KEY ,Name varchar(100) NOT NULL,Address TEXT NOT NULL,Email varchar(64),Phone INT)")
cur.execute("CREATE TABLE Bus_details(B_Id INT PRIMARY KEY,Bus_type char(5),Capacity INT,Fare INT,R_Id INT, Op_Id INT ,CONSTRAINT fk_OP_Id  FOREIGN KEY (Op_Id)REFERENCES Operator_details(Op_Id))")
cur.execute("CREATE TABLE Running_details(B_Id INT,Date DATE,Seat_available INT,PRIMARY KEY(B_Id,Date))")
cur.execute("CREATE TABLE Route_details(R_Id INT,Sname TEXT NOT NULL,S_Id INT ,PRIMARY KEY(R_Id,S_Id))")
cur.execute("CREATE TABLE Booking_history(Passenger_name TEXT NOT NULL,Gender varchar(10) ,No_of_passenger INT,Phone INT UNIQUE,Age INT, B_Id INT NOT NULL,Date DATE NOT NULL,Journey_date DATE NOT NULL,Booking_ref INT PRIMARY KEY AUTOINCREMENT,Boarding_station TEXT)")

con.commit()
