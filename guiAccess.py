import PySimpleGUI as sg
import databaseComms as dc
import sqlite3


# Add your new theme colors and settings
utc = {'BACKGROUND': '#00A09A',
                'TEXT': '#FFD100',
                'INPUT': '#260E61',
                'TEXT_INPUT': '#FFFFFF',
                'SCROLL': '#260E61',
                'BUTTON': ('white', '#260E61'),
                'PROGRESS': ('#01826B', '#D0D0D0'),
                'BORDER': 1,
                'SLIDER_DEPTH': 0,
                'PROGRESS_DEPTH': 0}

# Add your dictionary to the PySimpleGUI themes
sg.theme_add_new('utc', utc)

# Switch your theme to use the newly added one. You can add spaces to make it more readable
sg.theme('utc')






# Connect to the database
conn = sqlite3.connect('NEF.db')

def create_main_menu_layout():
    layout = [
        [sg.Image('logo.png')],
        [sg.Text('NEF Student Stamp Management System', size=(32,1), font=("Helvetica", 25))],
        [sg.Button('Add Student'), sg.Button('Award Stamps'), sg.Button('View Student')]
    ]
    return layout

def create_view_student_layout():
    layout = [
        [sg.Text('View Student', size=(30,1), font=("Helvetica", 25))],
        [sg.Text('Email Prefix'), sg.InputText(key='email_pref')],
        [sg.Button('View')],
        [sg.Button('Back')]
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

def add_student_window():
    layout = create_add_student_layout()
    window = sg.Window('Add Student', layout, element_justification='c', icon="logo.ico")
    while True:
        event, values = window.read()
        if event == sg.WIN_CLOSED:
            break
        if event == 'Add':
            dc.add_student(values['name'], values['form'], int(values['stamps']), values['email_pref'], values['main_class'])
            sg.popup('Student added successfully')
            break
        if event == 'Back':
            window.close()
            window = sg.Window('Main Menu', create_main_menu_layout(), element_justification='c', icon="logo.ico")
            break
    window.close()

def award_stamps_window():
    layout = create_award_stamps_layout()
    window = sg.Window('Award Stamps', layout, element_justification='c', icon="logo.ico")
    while True:
        event, values = window.read()
        if event == sg.WIN_CLOSED:
            break
        if event == 'Award':
            dc.award_stamps(values['student_name'], int(values['award_stamps']))
            sg.popup('Stamps awarded successfully')
            break
        if event == 'Back':
            window.close()
            window = sg.Window('Main Menu', create_main_menu_layout(), element_justification='c', icon="logo.ico")
            break
    window.close()

def view_student_window():
    layout = create_view_student_layout()
    window = sg.Window('View Student', layout, element_justification='c', icon="logo.ico")
    while True:
        event, values = window.read()
        if event == sg.WIN_CLOSED:
            break
        if event == 'View':
            result = dc.view_student(values['email_pref'])
            sg.popup("Student name: ", result[0],"\nStamp total: ", result[2],"\nForm class: ", result[1],"\nClass: ", result[4], icon="logo.ico")
            break
        if event == 'Back':
            window.close()
            window = sg.Window('Main Menu', create_main_menu_layout(), element_justification='c', icon="logo.ico")
            break
    window.close()

layout = [
    [sg.Image('logo.png')],
    [sg.Text('NEF Student Stamp Management System', size=(32,1), font=("Helvetica", 25))],
    [sg.Button('Add Student'), sg.Button('Award Stamps'), sg.Button('View Student')]
]

window = sg.Window('Main Menu', layout, element_justification='c', icon="logo.ico")

state = "main_menu"

while True:
    event, values = window.read()

    if event == sg.WIN_CLOSED:
        break

    if state == "main_menu":
        if event == 'Add Student':
            add_student_window()
        elif event == 'Award Stamps':
            award_stamps_window()
        elif event == 'View Student':
            view_student_window()
    else:
        if event == 'Back':
            state = "main_menu"
            window.close()
            window = sg.Window('Main Menu', create_main_menu_layout(), element_justification='c', icon="logo.ico")

conn.close()

window.close()