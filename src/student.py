from tkinter import Tk, Canvas, Label, Frame, Entry, Button, W, E, Listbox, END
import psycopg2
import os
from os.path import join, dirname
from dotenv import load_dotenv

dotenv_path = join(dirname(__file__), '../.env')
load_dotenv(dotenv_path)

root = Tk()
root.title("python & Postgresql")

conn = psycopg2.connect(
    dbname=os.environ.get('ENV_DB_NAME'),
    user=os.environ.get('ENV_USER'),
    password=os.environ.get('ENV_PASSWORD'),
    host=os.environ.get('ENV_HOST'),
    port=os.environ.get('EN_PORT')
)

def save_new_student(name, age, address):

    cursor = conn.cursor()
    query = """INSERT INTO students(name, age, address) VALUES (%s,%s,%s)"""
    cursor.execute(query,(name, age, address))
    print("Data Saved")
    conn.commit()
    #refresh with new students
    display_students()

def display_students():
    cursor = conn.cursor()
    query = """SELECT * FROM students"""
    cursor.execute(query)
    row = cursor.fetchall()
    listbox = Listbox(frame, width=20, height=10)
    listbox.grid(row=10, columnspan=4, sticky=W+E)
    for x in row:
        listbox.insert(END, x)
    conn.commit()

def findStudent(id):
    cursor = conn.cursor()
    query = """SELECT * FROM students WHERE id=%s"""
    cursor.execute(query, (id))
    row = cursor.fetchone()
    display_search_result(row)
    conn.commit()

def display_search_result(row):
    listbox = Listbox(frame, width=20, height=1)
    listbox.grid(row=9, columnspan=4, sticky=W+E)
    listbox.insert(END, row)

canvas = Canvas(root, height=380, width=400)
canvas.pack()
frame = Frame()
frame.place(relx=0.1, rely=0.1, relwidth=0.8, relheight=0.8 )
label = Label(frame, text='Add a student')
label.grid(row=0, column=1)
#name input
label = Label(frame, text="Name")
label.grid(row=1, column=0)
entry_name = Entry(frame)
entry_name.grid(row=1, column=1)
#Age input
label = Label(frame, text="Age")
label.grid(row=2, column=0)
entry_age = Entry(frame)
entry_age.grid(row=2, column=1)
#Address input
label = Label(frame, text="Address")
label.grid(row=3, column=0)
entry_address = Entry(frame)
entry_address.grid(row=3, column=1)
button = Button(frame, text='Add', command=lambda: save_new_student(
    entry_name.get(),
    entry_age.get(),
    entry_address.get()
    ))
button.grid(row=4, column=1,sticky=W+E)
#Search
label = Label(frame, text="Search Data")
label.grid(row=5, column=0)
label = Label(frame, text="Search by id")
label.grid(row=6, column=0)
id_search = Entry(frame)
id_search.grid(row=6, column=1)
button = Button(frame, text="Search", command=lambda:findStudent(id_search.get()))
button.grid(row=6, column=2)
display_students()
root.mainloop()
