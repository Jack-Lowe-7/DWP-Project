import sqlite3


def dbSelect():
    return "NEF.db"



# Function to add a student
def add_student(name, form, stamps, emailpre, mainClass):
    conn = sqlite3.connect(dbSelect())
    c = conn.cursor()
    c.execute("INSERT INTO students (name, form, stamps, emailpre, mainClass) VALUES (?, ?, ?, ?, ?)", (name, form, stamps, emailpre, mainClass))
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
def view_student(emailpre):
    conn = sqlite3.connect(dbSelect())
    c = conn.cursor()
    c.execute("SELECT * FROM students WHERE emailpre=?", (emailpre,))
    conn.close()
    return c.fetchone()





# Function to authenticate user
def authenticate_user(emailpre, password):
    conn = sqlite3.connect(dbSelect())
    c = conn.cursor()

    # Query staff table
    c.execute("SELECT * FROM staff WHERE emailpre=? AND password=?", (emailpre, password))
    staff_user = c.fetchone()
    if staff_user:
        # User is staff
        user_info = {'id': staff_user[0], 'emailpre': staff_user[1], 'is_staff': True}
    else:
        # Query regular users table
        c.execute("SELECT * FROM students WHERE emailpre=? AND password=?", (emailpre, password))
        regular_user = c.fetchone()
        if regular_user:
            # User is not staff
            user_info = {'id': regular_user[0], 'password': regular_user[1], 'is_staff': False}
        else:
            # No user found
            user_info = None

    conn.close()
    return user_info

# Function to get staff information
def get_staff_info(emailpre):
    conn = sqlite3.connect(dbSelect())
    c = conn.cursor()
    c.execute("SELECT * FROM staff WHERE emailpre=?", (emailpre,))
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
    c.execute("SELECT * FROM students WHERE emailpre=?", (emailpre,))
    student_info = c.fetchone()
    conn.close()
    return student_info
