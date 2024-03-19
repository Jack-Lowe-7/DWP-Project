import sqlite3


def dbSelect():
    return "NEF.db"



# Function to add a student
def add_student(name, form, stamps, emailpre, mainClass, password):
    conn = sqlite3.connect(dbSelect())
    c = conn.cursor()
    c.execute("INSERT INTO students (name, form, stamps, emailpre, mainClass, password) VALUES (?, ?, ?, ?, ?, ?)", (name, form, stamps, emailpre, mainClass, password))
    conn.commit()
    conn.close()

# Function to award stamps
def award_stamps(name, stamps):
    conn = sqlite3.connect(dbSelect())
    c = conn.cursor()
    c.execute("UPDATE students SET stamps = stamps + ? WHERE name = ? OR mainclass = ?", (stamps, name, name))
    conn.commit()
    conn.close()

# Function to view a student's info
def view_student(emailpre):
    conn = sqlite3.connect(dbSelect())
    c = conn.cursor()
    c.execute("SELECT * FROM students WHERE emailpre=?", (emailpre,))
    result = c.fetchone()
    conn.close()
    return result





def authenticate_staff(email, password):
    conn = sqlite3.connect(dbSelect())
    c = conn.cursor()
    c.execute("SELECT name, form, emailpre FROM staff WHERE emailpre=? AND password=?", (email, password))
    staff_info = c.fetchone()
    conn.close()
    return staff_info

def authenticate_student(email, password):
    conn = sqlite3.connect(dbSelect())
    c = conn.cursor()
    c.execute("SELECT name, form, stamps, emailpre, mainclass FROM students WHERE emailpre=? AND password=?", (email, password))
    student_info = c.fetchone()
    conn.close()
    return student_info

# Function to get staff information
def get_staff_info(emailpre):
    conn = sqlite3.connect(dbSelect())
    c = conn.cursor()
    c.execute("SELECT name, form, emailpre FROM staff WHERE emailpre=?", (emailpre,))
    staff_info = c.fetchone()
    conn.close()
    return staff_info

# Function to modify user stamps
def modify_user_stamps(emailpre, stamps):
    conn = sqlite3.connect(dbSelect())
    c = conn.cursor()
    c.execute("UPDATE students SET stamps=? WHERE emailpre=?", (stamps, emailpre))
    conn.commit()
    conn.close()

# Function to get student information
def get_student_info(emailpre):
    conn = sqlite3.connect(dbSelect())
    c = conn.cursor()
    c.execute("SELECT name, form, stamps, emailpre, mainclass FROM students WHERE emailpre=?", (emailpre,))
    student_info = c.fetchone()
    conn.close()
    return student_info

def leadCheck():
    conn = sqlite3.connect(dbSelect())
    c = conn.cursor()
    c.execute("SELECT SUM(stamps) FROM students WHERE form = 'Pasteur';")
    pasteur = c.fetchone()[0]
    c.execute("SELECT SUM(stamps) FROM students WHERE form = 'Newton';")
    newton = c.fetchone()[0]
    c.execute("SELECT SUM(stamps) FROM students WHERE form = 'Maxwell';")
    maxwell = c.fetchone()[0]
    list = [pasteur, newton, maxwell]
    list = sorted(list)
    i = 0
    while i < len(list):
        if list[i] == pasteur:
            list[i] = "Pasteur"
        elif list[i] == newton:
            list[i] = "Newton"
        elif list[i] == maxwell:
            list[i] = "Maxwell"
        i = i + 1
    conn.close()
    return list

def formTotal(form):
    conn = sqlite3.connect(dbSelect())
    c = conn.cursor()
    c.execute("SELECT SUM(stamps) FROM students WHERE form = ?;", (form,))
    res = c.fetchone()[0]
    conn.close()
    return res

def rankFind(form):
    conn = sqlite3.connect(dbSelect())
    c = conn.cursor()
    c.execute("SELECT name,stamps FROM students WHERE form = ? GROUP BY name,stamps ORDER BY stamps DESC LIMIT 3", (form,))
    res = c.fetchall()
    conn.close()
    return(res)