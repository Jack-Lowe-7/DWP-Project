import sqlite3

# Connect to the database
conn = sqlite3.connect('NEF.db')

# Create a cursor
c = conn.cursor()

# Create a table
c.execute('''CREATE TABLE IF NOT EXISTS students (
                name TEXT,
                form TEXT,
                stamps INTEGER,
                emailPre TEXT PRIMARY KEY UNIQUE,
                mainClass TEXT
                )''')

# Function to add a student
def add_student(name, form, stamps, emailPre, mainClass):
    c.execute("INSERT INTO students (name, form, stamps, emailPre, mainClass) VALUES (?, ?, ?, ?, ?)", (name, form, stamps, emailPre, mainClass))
    conn.commit()

# Function to award stamps
def award_stamps(name, stamps):
    c.execute("UPDATE students SET stamps = stamps + ? WHERE name = ?", (stamps, name))
    conn.commit()

# Function to view a student's info
def view_student_info(emailPre):
    c.execute("SELECT * FROM students WHERE emailPre=?", (emailPre,))
    return c.fetchone()

print("Console Mode")
def consoleChoice():
  choice = int(input("[1] Add a student\n[2] Award Stamps\n[3] View a student\n"))
  if choice == 1:
    name = input("Enter student's name: ")
    form = input("Enter student's form: ")
    stamps = input("Enter student's current stamps: ")
    emailPre = input("Enter student's email prefix (e.g. 19lowe.j): ")
    mainClass = input("Enter student's class: ")
    add_student(name, form, stamps, emailPre, mainClass)
  elif choice == 2:
    name = input("Enter student name: ")
    stamps = input("Enter stapms to add: ")
    award_stamps(name, stamps)
  elif choice == 3:
    emailPre = input("Enter student's email prefix (e.g. 19lowe.j): ")
    print(view_student_info(emailPre))
  else:
    print("Please enter a vaild option")
    consoleChoice()

consoleChoice()





"""

import PySimpleGUI as sg

layout = [
    [sg.Text('Student Management System', size=(30,1), font=("Helvetica", 25))],
    [sg.Button('Add Student'), sg.Button('Award Stamps'), sg.Button('Deduct Stamps')]
]

window = sg.Window('Main Menu', layout)

state = "main_menu"

def create_main_menu_layout():
    layout = [
        [sg.Text('Student Management System', size=(30,1), font=("Helvetica", 25))],
        [sg.Button('Add Student'), sg.Button('Award Stamps'), sg.Button('Deduct Stamps')]
    ]
    return layout

def create_add_student_layout():
    layout = [
        [sg.Text('Add Student', size=(30,1), font=("Helvetica", 25))],
        [sg.Text('Name'), sg.InputText(key='name')],
        [sg.Text('Form'), sg.InputText(key='form')],
        [sg.Text('Stamps'), sg.InputText(key='stamps')],
        [sg.Text('Email Prefix'), sg.InputText(key='email_pref')],
        [sg.Text('Main Class'), sg.InputText(key='main_class')],
        [sg.Button('Add')],
        [sg.Button('Back')]
    ]
    return layout

def create_award_stamps_layout():
    layout = [
        [sg.Text('Award Stamps', size=(30,1), font=("Helvetica", 25))],
        [sg.Text('Student Name'), sg.InputText(key='student_name')],
        [sg.Text('Stamps to Award'), sg.InputText(key='award_stamps')],
        [sg.Button('Award')],
        [sg.Button('Back')]
    ]
    return layout

def create_deduct_stamps_layout():
    layout = [
        [sg.Text('Deduct Stamps', size=(30,1), font=("Helvetica", 25))],
        [sg.Text('Student Name'), sg.InputText(key='student_name')],
        [sg.Text('Stamps to Deduct'), sg.InputText(key='deduct_stamps')],
        [sg.Button('Deduct')],
        [sg.Button('Back')]
    ]
    return layout

state = "main_menu"
window = sg.Window('Main Menu', create_main_menu_layout())

while True:
    event, values = window.read()

    if event == sg.WIN_CLOSED:
        break

    if state == "main_menu":
        if event == 'Add Student':
            state = "add_student"
            window.close()
            window = sg.Window('Add Student', create_add_student_layout())
        elif event == 'Award Stamps':
            state = "award_stamps"
            window.close()
            window = sg.Window('Award Stamps', create_award_stamps_layout())
        elif event == 'Deduct Stamps':
            state = "deduct_stamps"
            window.close()
            window = sg.Window('Deduct Stamps', create_deduct_stamps_layout())
    else:
        if event == 'Back':
            state = "main_menu"
            window.close()
            window = sg.Window('Main Menu', create_main_menu_layout())

window.close()

"""

# Close the connection
conn.close()
