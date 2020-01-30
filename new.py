from flask import Flask
from flask import render_template,request
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

if __name__=='__main__':
    app.run(debug=True)