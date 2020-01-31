from flask import Flask
from flask import render_template,request,redirect
app = Flask(__name__)
    

@app.route('/',methods=['GET','POST'])
def hello_world():
    return render_template('input.html')

@app.route('/alumni/dashboard')
def dashboardalumni():
    return render_template("pages/alumni/dashboardalumni.html")

@app.route('/Director/dashboard')
def dashboarddirector():
    return render_template("pages/DIR/dashboarddirector.html")

@app.route('/DHE/dashboard')
def dashboarddhe():
    return render_template("pages/DHE/dashboarddhe.html")

@app.route('/alumni/profile')
def Aluminiprofile():
    return render_template("pages/alumni/profile.html")

@app.route('/alumni/www.facebook.com')
def facebook():
    return redirect("https://www.facebook.com",code=302)

@app.route('/alumni/www.twitter.com')
def twitter():
    return redirect("https://www.twitter.com",code=302)

@app.route('/alumni/www.google.com')
def google():
    return redirect("https://www.google.com",code=302)

if __name__=='__main__':
    app.run(debug=True)