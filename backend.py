from flask import Flask, render_template, request, redirect, url_for, flash, session
import mysql.connector as msc
import random,string

app = Flask(__name__)
app.secret_key = "secretkey"

myDB = msc.connect(
    host="localhost", user="root", passwd="@B00y@hmysql", database="schedule"
)
crs = myDB.cursor()

@app.route("/")
def home():
    return render_template("index.html")

@app.route("/admin_login", methods=["POST"])
def admin_login():
    username = request.form["username"]
    password = request.form["password"]

    admin={"1234":"@1234"}

    for a in admin:
        if a==username:
            if admin[a]==password:
                session["user"] = admin[a]
                session["role"] = "admin"
                flash("Admin login successful!", "success")
                return redirect(url_for("admin_dashboard"))   # redirect to dashboard
                break
    else:
        flash("Invalid Admin credentials", "danger")
        return redirect(url_for("admin"))

@app.route("/vendor_login", methods=["POST"])
def vendor_menu():
            query = """INSERT INTO vendor (bid, bname, bseats, bstrength, bcourses_s1, bcourses_s2) 
                       VALUES (%s, %s, %s, %s, %s, %s)"""
             
            values = (bid, bname, bseats,0,bcourses_s1_str,bcourses_s2_str)
            crs.execute(query, values)

            crs.execute(f"CREATE TABLE {bname}(sid INT PRIMARY KEY, sname VARCHAR(100), password VARCHAR(100), sbranch VARCHAR(100), semester INT,scourses VARCHAR(255))")