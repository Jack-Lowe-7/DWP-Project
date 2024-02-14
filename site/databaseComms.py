import sqlite3


def dbSelect():
    return "NEF.db"



# Function to add a student
def add_student(name, form, stamps, emailPre, mainClass):
    conn = sqlite3.connect(dbSelect())
    c = conn.cursor()
    c.execute("INSERT INTO students (name, form, stamps, emailPre, mainClass) VALUES (?, ?, ?, ?, ?)", (name, form, stamps, emailPre, mainClass))
    conn.commit()
    conn.close()

# Function to award stamps
def award_stamps(name, stamps):
    conn = sqlite3.connect(dbSelect())
    c = conn.cursor()
    c.execute("UPDATE students SET stamps = stamps + ? WHERE name = ?", (stamps, name))
    conn.commit()
    conn.close()

# Function to view a student's info
def view_student(emailPre):
    conn = sqlite3.connect(dbSelect())
    c = conn.cursor()
    c.execute("SELECT * FROM students WHERE emailPre=?", (emailPre,))
    conn.close()
    return c.fetchone()





# Function to authenticate user
def authenticate_user(username, password):
    conn = sqlite3.connect(dbSelect())
    c = conn.cursor()
    c.execute("SELECT * FROM students WHERE emailPre=? AND password=?", (username, password))
    user = c.fetchone()
    conn.close()
    return user

# Function to get staff information
def get_staff_info(emailPre):
    conn = sqlite3.connect(dbSelect())
    c = conn.cursor()
    c.execute("SELECT * FROM staff WHERE id=?", (emailPre,))
    staff_info = c.fetchone()
    conn.close()
    return staff_info

# Function to modify user stamps
def modify_user_stamps(emailPre, stamps):
    conn = sqlite3.connect(dbSelect())
    c = conn.cursor()
    c.execute("UPDATE students SET stamps=? WHERE id=?", (stamps, emailPre))
    conn.commit()
    conn.close()

# Function to get student information
def get_student_info(emailPre):
    conn = sqlite3.connect(dbSelect())
    c = conn.cursor()
    c.execute("SELECT * FROM students WHERE id=?", (emailPre,))
    student_info = c.fetchone()
    conn.close()
    return student_info
