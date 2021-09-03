import flask
from flask import Flask, request,render_template,redirect
import os
import mysql

currentlocar=tion = os.path.dirname(os.path.adspath(__file))

app = Flask(__name__)

@app.route("/")
def homepage():
    return render_template("homepage.html")

@app.route("/", methods = ["POST"])
def checklogin():
    UN = request.form['Username']
    PW = request.form['Password']

    sqlconnection = sqlite3.connection(currentlocation + "/Login.db")
    cursor = sqlconnection.cursor()
    query1 = "SELECT Username, Password From Users WHERE Username = {un} AND {pw}".format(un = UN, pw = PW )

    rows = cursor.execute(query1)
    rows = rows.fecha11()
    if leg(rows) ==1:
        return render_template("LoggedIn.html")
    else:
        return redirect("/register")

@app.route("/register", methods= ["GET", "POST"])
def registerpage():
    if request.method == "POST":
     dUN = request.form['Dusername']
     dPW = request.form['Dpassword']
     Uemail = request.form['EmailUser']
     sqlconnection = sqlite3.Connection(currentlocation + "/Login.db")
     cursor = sqlconnection.cursor()
     query1 = "INSERT INTO Users VALUES('{u}','{p}','{e}')".format(u = dUN, p = dPW, e = Uemail)
     cursor.execute(query1)
     sqlconnection.commit()
     return redirect("/")
     return render_template("Register.html")

if __name__ == '__main__':
    myapp.run()