from flask import Flask
from flask import render_template,request,redirect,url_for
from flask_sqlalchemy import SQLAlchemy
from flask import flash

app = Flask(__name__)
 
app.config['SQLALCHEMY_DATABASE_URI'] = 'mysql://root:@localhost/alumni_system'

db = SQLAlchemy(app)

# TABLE FOR COLLEGES
class Colleges(db.Model):
    __tablename__="colleges"
    College_ID = db.Column(db.Integer,primary_key=True)
    College_Name = db.Column(db.String(60))
    University = db.Column(db.String(60),nullable=False)
    Director_Name = db.Column(db.String(60),nullable=False)

#TABLE FOR AUTHORITY
class AuthorityLogin(db.Model):
    __tablename__="authority_login"
    Email = db.Column(db.Integer,primary_key=True)
    Password = db.Column(db.String(60))
    Type = db.Column(db.String(60),nullable=False)
    University = db.Column(db.String(60),nullable=True)
    College = db.Column(db.String(60),nullable=True)
    
@app.route('/',methods=['GET','POST'])
def login():
    if request.method=='POST':
        usertype =  request.form.get('usertype')
        if usertype == "DHE":
            email = request.form.get('email')
            password = request.form.get('password')
            data = AuthorityLogin.query.all()
            for i in data:
                if i.Email==email and i.Password==password:
                    return redirect('/dhe/dashboard')
                else:
                    flash("some text to flash")

    return render_template('input.html')

@app.route('/DHE/trackalumni')
def trackalumni1():
    return render_template("pages/DHE/dhetrackalumni.html")
   
@app.route('/director/trackalumni')
def trackalumni():
    return render_template("pages/DIR/directortrackalumni.html")

@app.route('/notfound')
def notfound():
    return render_template("/index.html")

@app.route('/student/schedules')
def schedulesstudents():
    return render_template('pages/student/studentschedules.html')


@app.route('/alumni/dashboard')
def dashboardalumni():
    return render_template("pages/alumni/dashboardalumni.html")

@app.route('/director/dashboard')
def dashboarddirector():
    return render_template("pages/DIR/directordashboard.html")
    

@app.route('/alumni/donation')
def aldonatecollegedevlp():
    return render_template("pages/alumni/alumnidonation.html")
 
@app.route('/dhe/dashboard')
def dashboarddhe():
    return render_template("pages/DHE/dashboarddhe.html")
  
@app.route('/alumni/profile')
def aluminiprofile():
    return render_template("pages/alumni/profile.html")

@app.route('/alumni/www.facebook.com')
def alumnifacebook():
    return redirect("https://www.facebook.com",code=302)

@app.route('/alumni/www.twitter.com')
def alumnitwitter():
    return redirect("https://www.twitter.com",code=302)

@app.route('/alumni/www.google.com')
def alumnigoogle():
    return redirect("https://www.google.com",code=302)

@app.route('/student/profile')
def alumnistudentprofile():
    return render_template("pages/student/studentprofile.html")

@app.route('/student/events')
def studentEvents():
    return render_template("pages/student/studentevents.html")
    
@app.route('/alumni/tablealumni')
def table():
    return render_template("pages/alumni/tablealumni.html")

@app.route('/director/managefunddirector')
def managefunddirector():
    return render_template("pages/DIR/managefunddirector.html")

@app.route('/director/trackstudent')
def trackstudents():
    return render_template("pages/DIR/directortrackstudents.html")

if __name__=='__main__':
    app.run(debug=True)