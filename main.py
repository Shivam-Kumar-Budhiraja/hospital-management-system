# HOSPITAL MANAGEMENT SYSTEM (GUI VERSION)
# Beginner Friendly – Logic Preserved

import pymysql as p
import tkinter as tk
from tkinter import messagebox

# ---------------- DATABASE CONNECTION ----------------

db = p.connect(host="localhost", user="root", password="1234")
cur = db.cursor()

# Create Database
try:
    cur.execute("CREATE DATABASE HOSPITAL")
except:
    pass

cur.execute("USE HOSPITAL")

# Create Tables
try:
    cur.execute("CREATE TABLE DOCTORS(ID INT, NAME VARCHAR(40), MOBILE VARCHAR(10), SPECIALITY VARCHAR(50), FEES INT, EXPERIENCE INT)")
except:
    pass

try:
    cur.execute("CREATE TABLE PATIENTS(ROOM INT, NAME VARCHAR(40), AGE INT, GENDER VARCHAR(10), RESIDENCE VARCHAR(50), MOBILE VARCHAR(10), CONSULTANT VARCHAR(20), CONSULTANCY_FEES INT)")
except:
    pass

try:
    cur.execute("CREATE TABLE ROOMS(ROOM_NO INT, FACILITY VARCHAR(20), FEES_PER_DAY INT, STATUS VARCHAR(20), PATIENT VARCHAR(20))")
except:
    pass

try:
    cur.execute("CREATE TABLE BILLS(ID INT, DATE DATE, NAME VARCHAR(20), FACILITY VARCHAR(10), ROOM_CHARGES INT, TREATMENT_FEES INT, DOCTOR_FEES INT, TOTAL INT)")
except:
    pass

db.commit()

# ---------------- GUI FUNCTIONS ----------------

def add_doctor():
    win = tk.Toplevel()
    win.title("Add Doctor")

    labels = ["ID", "Name", "Mobile", "Speciality", "Fees", "Experience"]
    entries = []

    for i, text in enumerate(labels):
        tk.Label(win, text=text).grid(row=i, column=0, padx=10, pady=5)
        e = tk.Entry(win)
        e.grid(row=i, column=1)
        entries.append(e)

    def save():
        try:
            cur.execute(
                "INSERT INTO DOCTORS VALUES (%s,%s,%s,%s,%s,%s)",
                tuple(e.get() for e in entries)
            )
            db.commit()
            messagebox.showinfo("Success", "Doctor added successfully")
            win.destroy()
        except Exception as e:
            messagebox.showerror("Error", str(e))

    tk.Button(win, text="Save", command=save).grid(row=6, column=1, pady=10)

def view_doctors():
    win = tk.Toplevel()
    win.title("Doctors List")

    text = tk.Text(win, width=90, height=20)
    text.pack()

    cur.execute("SELECT * FROM DOCTORS")
    for row in cur.fetchall():
        text.insert(tk.END, str(row) + "\n")

def add_patient():
    win = tk.Toplevel()
    win.title("Add Patient")

    labels = ["Room", "Name", "Age", "Gender", "Address", "Mobile", "Consultant", "Fees"]
    entries = []

    for i, text in enumerate(labels):
        tk.Label(win, text=text).grid(row=i, column=0)
        e = tk.Entry(win)
        e.grid(row=i, column=1)
        entries.append(e)

    def save():
        try:
            cur.execute(
                "INSERT INTO PATIENTS VALUES (%s,%s,%s,%s,%s,%s,%s,%s)",
                tuple(e.get() for e in entries)
            )
            db.commit()
            messagebox.showinfo("Success", "Patient added")
            win.destroy()
        except Exception as e:
            messagebox.showerror("Error", str(e))

    tk.Button(win, text="Save", command=save).grid(row=8, column=1)

def view_patients():
    win = tk.Toplevel()
    win.title("Patients List")

    text = tk.Text(win, width=90, height=20)
    text.pack()

    cur.execute("SELECT * FROM PATIENTS")
    for row in cur.fetchall():
        text.insert(tk.END, str(row) + "\n")

def add_room():
    win = tk.Toplevel()
    win.title("Add Room")

    labels = ["Room No", "Facility", "Fees/Day", "Status", "Patient"]
    entries = []

    for i, text in enumerate(labels):
        tk.Label(win, text=text).grid(row=i, column=0)
        e = tk.Entry(win)
        e.grid(row=i, column=1)
        entries.append(e)

    def save():
        try:
            cur.execute(
                "INSERT INTO ROOMS VALUES (%s,%s,%s,%s,%s)",
                tuple(e.get() for e in entries)
            )
            db.commit()
            messagebox.showinfo("Success", "Room added")
            win.destroy()
        except Exception as e:
            messagebox.showerror("Error", str(e))

    tk.Button(win, text="Save", command=save).grid(row=5, column=1)

def view_rooms():
    win = tk.Toplevel()
    win.title("Rooms List")

    text = tk.Text(win, width=90, height=20)
    text.pack()

    cur.execute("SELECT * FROM ROOMS")
    for row in cur.fetchall():
        text.insert(tk.END, str(row) + "\n")

def add_bill():
    win = tk.Toplevel()
    win.title("Add Bill")

    labels = ["ID", "Date (YYYY-MM-DD)", "Name", "Facility", "Room Charges", "Treatment Fees", "Doctor Fees", "Total"]
    entries = []

    for i, text in enumerate(labels):
        tk.Label(win, text=text).grid(row=i, column=0)
        e = tk.Entry(win)
        e.grid(row=i, column=1)
        entries.append(e)

    def save():
        try:
            cur.execute(
                "INSERT INTO BILLS VALUES (%s,%s,%s,%s,%s,%s,%s,%s)",
                tuple(e.get() for e in entries)
            )
            db.commit()
            messagebox.showinfo("Success", "Bill added")
            win.destroy()
        except Exception as e:
            messagebox.showerror("Error", str(e))

    tk.Button(win, text="Save", command=save).grid(row=8, column=1)

def view_bills():
    win = tk.Toplevel()
    win.title("Bills List")

    text = tk.Text(win, width=100, height=20)
    text.pack()

    cur.execute("SELECT * FROM BILLS")
    for row in cur.fetchall():
        text.insert(tk.END, str(row) + "\n")

# ---------------- MAIN GUI ----------------

root = tk.Tk()
root.title("Hospital Management System")

tk.Label(root, text="HOSPITAL MANAGEMENT SYSTEM", font=("Arial", 16, "bold")).pack(pady=10)

buttons = [
    ("Add Doctor", add_doctor),
    ("View Doctors", view_doctors),
    ("Add Patient", add_patient),
    ("View Patients", view_patients),
    ("Add Room", add_room),
    ("View Rooms", view_rooms),
    ("Add Bill", add_bill),
    ("View Bills", view_bills),
    ("Exit", root.destroy)
]

for text, cmd in buttons:
    tk.Button(root, text=text, width=35, command=cmd).pack(pady=4)

root.mainloop()
