from flask import Flask
from flask import render_template,request,redirect,url_for
app = Flask(__name__)
    

@app.route('/',methods=['GET','POST'])
def hello_world():
    return render_template('input.html')

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
 
@app.route('/DHE/dashboard')
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
    
@app.route('/alumni/tablealumni')
def table():
    return render_template("pages/alumni/tablealumni.html")

@app.route('/director/managefunddirector')
def managefunddirector():
    return render_template("pages/DIR/managefunddirector.html")

if __name__=='__main__':
    app.run(debug=True)