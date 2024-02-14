# app.py
from flask import Flask, render_template, request, session, redirect, url_for
from databaseComms import * as dC

app = Flask(__name__)
app.secret_key = 'your_secret_key'

# Function to check if the user is logged in
def is_logged_in():
    return 'user_id' in session

# Route for staff login
@app.route('/login', methods=['GET', 'POST'])
def login():
    if request.method == 'POST':
        username = request.form['username']
        password = request.form['password']
        user = dC.authenticate_user(username, password)
        if user and user['is_staff']:
            session['user_id'] = user['id']
            return redirect(url_for('staff_dashboard'))
        else:
            error = 'Invalid login'
            return render_template('login.html', error=error)
    return render_template('login.html')

# Route for staff dashboard
@app.route('/staff/dashboard')
def staff_dashboard():
    if not is_logged_in():
        return redirect(url_for('login'))
    # Fetch staff information using session['user_id']
    staff_info = dC.get_staff_info(session['user_id'])
    return render_template('staff_dashboard.html', staff_info=staff_info)

# Route for modifying stamps
@app.route('/modify_stamps', methods=['POST'])
def modify_stamps():
    if not is_logged_in():
        return redirect(url_for('login'))
    emailPre = request.form['emailPre']
    stamps = request.form['stamps']
    # Call function from databaseComms.py to modify stamps
    dC.modify_user_stamps(emailPre, stamps)
    return redirect(url_for('staff_dashboard'))

# Route for student dashboard
@app.route('/student/dashboard')
def student_dashboard():
    if not is_logged_in():
        return redirect(url_for('login'))
    # Fetch student information using session['user_id']
    student_info = dC.get_student_info(session['user_id'])
    return render_template('student_dashboard.html', student_info=student_info)

# Logout route
@app.route('/logout')
def logout():
    session.clear()
    return redirect(url_for('login'))

if __name__ == '__main__':
    app.run(debug=True)
