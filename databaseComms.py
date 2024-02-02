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
def view_student(emailPre):
    c.execute("SELECT * FROM students WHERE emailPre=?", (emailPre,))
    return c.fetchone()


# Close the connection
conn.close()
