from flask import Flask, render_template, request, redirect, url_for, session, send_file
from databaseComms import authenticate_staff, authenticate_student, get_staff_info, get_student_info, award_stamps, add_student, leadCheck, formTotal, rankFind

#flask run --cert=adhoc


app = Flask(__name__)
app.secret_key = 'b66ba2893267082517aa8760513c665f2eac2eed33b74648ebb39df8e921eee0'  # Change this to a secure secret key

@app.route('/')
def index():
    return render_template('index.html')


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

@app.route('/logout')
def logout():
    session.pop('email', None)
    session.pop('is_staff', None)
    return redirect(url_for('login'))


#STAFF
@app.route('/staff/dashboard')
def staff_dashboard():
    if 'email' not in session or 'is_staff' not in session or not session['is_staff']:
        return redirect(url_for('login'))
    
    # Fetch staff information using session['email']
    email = session['email']
    staff_info = get_staff_info(email)
    
    return render_template('staff_dashboard.html', staff_info=staff_info)


# Route for student dashboard
@app.route('/student/dashboard')
def student_dashboard():
    if 'email' not in session or 'is_staff' not in session or session['is_staff']:
        return redirect(url_for('login'))
    
    # Fetch student information using session['email']
    email = session['email']
    student_info = get_student_info(email)
    
    return render_template('student_dashboard.html', student_info=student_info)

@app.route('/staff/dashboard/modify', methods=['POST'])
def modify():
    students = request.form['user_id']
    stamps = request.form['stamps']
    award_stamps(students, stamps)
    return redirect(url_for('staff_dashboard'))




#ADMIN
@app.route('/admin', methods=['GET', 'POST'])
def adminLogin():
    if request.method == 'POST':
        email = request.form['email']
        password = request.form['password']
        
        # Check if admin user
        staff_info = False
        if email == "admin" and password == "admin":
            staff_info = True
        if staff_info == True:
            session['email'] = email
            session['is_admin'] = True
            return redirect(url_for('admin_dashboard'))
        
        # If authentication fails, show error message
        error = "Invalid credentials. Please try again if you are an admin."
        return render_template('admin-login.html', error=error)
    
    # If GET request, render login form
    return render_template('admin-login.html')


@app.route('/admin/dashboard')
def admin_dashboard():
    if 'email' not in session or 'is_admin' not in session or not session['is_admin']:
        return redirect(url_for('/'))
    
    return render_template('admin.html')


@app.route('/admin/dashboard/download_template')
def database_template():
    path = "/site/static/downloads/databse-template-blank.db"
    return send_file(path, as_attachment=True)


def allowed_file(filename):
    return '.' in filename and filename.rsplit('.', 1)[1].lower() in ['.db']



@app.route('/admin/dashboard/upload', methods = ['GET', 'POST'])   
def upload():   
    if request.method == 'POST':
        f = request.files['file']
        if allowed_file(f.filename):
            f.save(f.filename)
            return render_template("upload_success.html", name = f.filename)
        else:
            return render_template("upload_fail.html", msg="File extension not allowed - use a database with file format .db matching the set-up of the template on the admin panel")   
    
@app.route('/admin/dashboard/add_student', methods = ['GET', 'POST'])
def add_student_page():
    if request.method == 'POST':
        name = request.form['student_name']
        form = request.form['student_form']
        mainclass = request.form['student_class']
        passw = request.form['student_pass']
        stamps = request.form['stamps']
        name = name.split(" ")
        fname = name[1]
        lname = name[0]
        emailpre = "19" + lname.lower() + "." + fname[0]
        add_student(str(name), str(form), int(stamps), str(emailpre), str(mainclass), str(passw))
        return redirect(url_for('admin_dashboard'))

#MISC PAGES
@app.route('/license')
def license():
    return render_template('license.html')

@app.route('/leaderboard')
def board():
    stats = leadCheck()
    return render_template('leaderboards/leaderboard.html', one=stats[0], two=stats[1], three=stats[2])

@app.route('/leaderboard/pasteur')
def pasteur():
    total = formTotal("Pasteur")
    p = rankFind("Pasteur")
    return render_template('leaderboards/pasteur.html', form=total, one=p[0], two=p[1], three=p[2])

@app.route('/leaderboard/maxwell')
def maxwell():
    total = formTotal("Maxwell")
    p = rankFind("Maxwell")
    return render_template('leaderboards/maxwell.html', form=total, one=p[0], two=p[1], three=p[2])

@app.route('/leaderboard/newton')
def newton():
    total = formTotal("Newton")
    p = rankFind("Newton")
    return render_template('leaderboards/newton.html', form=total, one=p[0], two=p[1], three=p[2])


#Errors
@app.errorhandler(400)
def bad_request(error):
    return render_template('errors/400.html'), 400

@app.errorhandler(401)
def unauthorized(error):
    return render_template('errors/401.html'), 401

@app.errorhandler(403)
def forbidden(error):
    return render_template('errors/403.html'), 403

@app.errorhandler(404)
def page_not_found(error):
    return render_template('errors/404.html'), 404

@app.errorhandler(405)
def method_not_allowed(error):
    return render_template('errors/405.html'), 405

@app.errorhandler(500)
def internal_server_error(error):
    return render_template('errors/500.html'), 500

@app.errorhandler(503)
def  service_unavailable(error):
    return render_template('errors/503.html'), 503




if __name__ == '__main__':
    app.run(debug=True, ssl_context='adhoc')