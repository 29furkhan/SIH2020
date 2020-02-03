from flask import Flask
from flask import render_template,request,redirect,url_for
from flask_sqlalchemy import SQLAlchemy
from flask_login import login_required
from flask_login import logout_user
from flask import flash
from flask_login import LoginManager
from flask_login import UserMixin
from flask_login import login_user

app = Flask(__name__)
 
app.config['SECRET_KEY'] = "thisisit"
app.config['SQLALCHEMY_DATABASE_URI'] = 'mysql://root:@localhost/alumni_system'

db = SQLAlchemy(app)

login_manager = LoginManager()
login_manager.login_view = 'login'
login_manager.init_app(app)

@login_manager.user_loader
def load_user(user_id):
    return AuthorityLogin.query.get(int(user_id))


# TABLE FOR COLLEGES
class Colleges(db.Model):
    __tablename__="colleges"
    College_ID = db.Column(db.Integer,primary_key=True)
    College_Name = db.Column(db.String(60))
    University = db.Column(db.String(60),nullable=False)
    Director_Name = db.Column(db.String(60),nullable=False)

#TABLE FOR AUTHORITY
class AuthorityLogin(db.Model,UserMixin):
    __tablename__="authority_login"
    id = db.Column(db.Integer,primary_key=True)
    Email = db.Column(db.String(60))
    Password = db.Column(db.String(60))
    Type = db.Column(db.String(60),nullable=False)
    University = db.Column(db.String(60),nullable=True)
    College = db.Column(db.String(60),nullable=True)

# Table for ALUMNI/STUDENT
class AspirantLogin(db.Model,UserMixin):
    __tablename__="aspirant_login"
    id = db.Column(db.Integer,primary_key=True)
    prn = db.Column(db.String(60))
    password = db.Column(db.String(60))
    type = db.Column(db.String(60),nullable=False)
    university = db.Column(db.String(60),nullable=True)
    clg = db.Column(db.String(60),nullable=True)


@app.route('/')
def login_normal():
    return render_template('input.html')

@app.route('/',methods=['GET','POST'])
def login():
    usertype =  request.form.get('usertype')
    if usertype == "DHE":
        email = request.form.get('email')
        password = request.form.get('password')
        user = AuthorityLogin.query.filter_by(Email = email).first()
        if not user or (password!=user.Password):
            flash("Invalid Email or Password")
            return redirect(url_for('login'))
        login_user(user)
        return redirect(url_for("trackalumni1"))
    # Director Login    
    elif usertype=="DIR":
        email = request.form.get('email')
        password = request.form.get('password')
        user = AuthorityLogin.query.filter_by(Email = email).first()
        if not user or (password!=user.Password):
            flash("Invalid Email or Password")
            return redirect(url_for('login'))
        login_user(user)
        return redirect(url_for("dashboarddirector"))

    # Alumni
    elif usertype=="alumni":
        prn = request.form.get('prn')
        password = request.form.get('password')
        clg = request.form.get('clgselect')
        university = request.form.get('universityselect')

        user = AspirantLogin.query.filter_by(prn = prn).first()
        if user.type=="student" or user.type=="pending":
            if not user or (password!=user.password) or university!=user.university or clg!=user.clg:
                flash("Invalid Details")
                return redirect(url_for('login'))
            else:
                user.type="pending"
                db.session.commit()
                login_user(user)
                return redirect(url_for("dashboardalumnidisabled"))

        elif user.type=="alumni":
            if not user or (password!=user.password) or university!=user.university or clg!=user.clg or usertype!=user.type:
                flash("Invalid Details")
                return redirect(url_for('login'))
        
            login_user(user)
            return redirect(url_for("dashboardalumni"))

    # Student
    elif usertype=="student":
        prn = request.form.get('prn')
        password = request.form.get('password')
        clg = request.form.get('clgselect')
        university = request.form.get('universityselect')

        user = AspirantLogin.query.filter_by(prn = prn).first()
        print(user.prn,user.password,user.university,user.clg,user.type)
        print(prn,password,university,clg,usertype)
        if not user or (password!=user.password) or university!=user.university or clg!=user.clg or usertype!=user.type:
            flash("Invalid Details")
            return redirect(url_for('login'))
        login_user(user)
        return redirect(url_for("alumnistudentprofile"))
            

        


@app.route('/DHE/trackalumni')
@login_required
def trackalumni1():
    return render_template("pages/DHE/dhetrackalumni.html")
   
@app.route('/director/trackalumni')
@login_required
def trackalumni():
    return render_template("pages/DIR/directortrackalumni.html")

@app.route('/notfound')
def notfound():
    return render_template("/index.html")

@app.route('/student/schedules')
@login_required
def schedulesstudents():
    return render_template('pages/student/studentschedules.html')


@app.route('/alumni/dashboard')
def dashboardalumni():
    return render_template("pages/alumni/dashboardalumni.html")

@app.route('/alumni/dashboard_disabled')
def dashboardalumnidisabled():
    return render_template("pages/alumni/dashboardalumni_disabled.html")

@app.route('/director/dashboard')
@login_required
def dashboarddirector():
    return render_template("pages/DIR/directordashboard.html")
    

@app.route('/alumni/donation')
@login_required
def aldonatecollegedevlp():
    return render_template("pages/alumni/alumnidonation.html")
 
@app.route('/dhe/dashboard')
@login_required
def dashboarddhe():
    return render_template("pages/DHE/dashboarddhe.html")
  
@app.route('/alumni/profile')
@login_required
def aluminiprofile():
    return render_template("pages/alumni/profile.html")

@app.route('/alumni/www.facebook.com')
@login_required
def alumnifacebook():
    return redirect("https://www.facebook.com",code=302)

@app.route('/alumni/www.twitter.com')
@login_required
def alumnitwitter():
    return redirect("https://www.twitter.com",code=302)

@app.route('/alumni/www.google.com')
def alumnigoogle():
    return redirect("https://www.google.com",code=302)

@app.route('/student/profile')
@login_required
def alumnistudentprofile():
    return render_template("pages/student/studentprofile.html")

@app.route('/student/events')
@login_required
def studentEvents():
    return render_template("pages/student/studentevents.html")
    
@app.route('/alumni/tablealumni')
@login_required
def table():
    return render_template("pages/alumni/tablealumni.html")

@app.route('/director/managefunddirector')
@login_required
def managefunddirector():
    return render_template("pages/DIR/managefunddirector.html")

@app.route('/director/trackstudent')
@login_required
def trackstudents():
    return render_template("pages/DIR/directortrackstudents.html")

@app.route('/director/authentication')
@login_required
def authentication():
    return render_template("pages/DIR/authentication.html")

    
@app.route("/logout")
@login_required
def logout():
    logout_user()
    return redirect(url_for('login'))

@app.route("/alumni/authenticate",methods=['GET','POST'])
def authenticate():
    if request.method=='POST':
        val = request.get_data('data')
        # return val
        user = AspirantLogin.query.filter_by(prn = val).first()
        user.type="alumni"
        db.session.commit()
        return "Alumni Approved"

@app.route("/alumni/authenticate/reject",methods=['GET','POST'])
def reject():
    if request.method=='POST':
        val = request.get_data('data')
        # return val
        user = AspirantLogin.query.filter_by(prn = val).first()
        user.type="student"
        db.session.commit()
        return "Request Rejected"



if __name__=='__main__':
    app.run(debug=True)