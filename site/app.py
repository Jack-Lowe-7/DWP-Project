from flask import Flask, render_template, request, redirect, url_for, session
from databaseComms import authenticate_staff, authenticate_student

app = Flask(__name__)
app.secret_key = 'your_secret_key'  # Change this to a secure secret key

# Route for logging in
@app.route('/login', methods=['GET', 'POST'])
def login():
    if request.method == 'POST':
        email = request.form['email']
        password = request.form['password']
        
        # Check if staff user
        staff_info = authenticate_staff(email, password)
        if staff_info:
            session['email'] = email
            session['is_staff'] = True
            return redirect(url_for('staff_dashboard'))
        
        # Check if student user
        student_info = authenticate_student(email, password)
        if student_info:
            session['email'] = email
            session['is_staff'] = False
            return redirect(url_for('student_dashboard'))
        
        # If authentication fails, show error message
        error = "Invalid email or password. Please try again."
        return render_template('login.html', error=error)
    
    # If GET request, render login form
    return render_template('login.html')

# Route for staff dashboard
@app.route('/staff/dashboard')
def staff_dashboard():
    if 'email' not in session or 'is_staff' not in session or not session['is_staff']:
        return redirect(url_for('login'))
    return render_template('staff_dashboard.html')

# Route for student dashboard
@app.route('/student/dashboard')
def student_dashboard():
    if 'email' not in session or 'is_staff' not in session or session['is_staff']:
        return redirect(url_for('login'))
    return render_template('student_dashboard.html')

# Route for logging out
@app.route('/logout')
def logout():
    session.pop('email', None)
    session.pop('is_staff', None)
    return redirect(url_for('login'))

if __name__ == '__main__':
    app.run(debug=True)
