from flask import Flask, render_template, request, redirect, url_for, flash, session
import mysql.connector as msc
import random,string

app = Flask(__name__)
app.secret_key = "secretkey"

myDB = msc.connect(
    host="localhost", user="root", passwd="@B00y@hmysql", database="FOOD_DELIVERY"
)
crs = myDB.cursor()

@app.route("/")
def home():
    return render_template("index.html")

@app.route("/vendor")
def home():
    return render_template("vendor_login.html")

@app.route("/admin")
def home():
    return render_template("admin_login.html")

@app.route("/client")
def home():
    return render_template("client_login.html")


@app.route("/vendor_login", methods=["POST"])
def admin_login():
    username = request.form["username"]
    password = request.form["password"]

    crs.execute("SELECT USERNAME,PASSWORD FROM VENDORS")
    data=crs.fetchall()

    for a in data:
        if a[0]==username:
            if a[1]==password:
                session["user"] = a[1]
                session["role"] = "vendor"
                flash("Vendor login successful!", "success")
                return redirect(url_for("admin_dashboard"))   # redirect to dashboard
                break
    else:
        flash("Invalid Vendor credentials", "danger")
        return redirect(url_for("admin"))

@app.route("/vendor_register", methods=["POST"])
def vendor_login():
            x=0
            query = """INSERT INTO vendor (bid, bname, bseats, bstrength, bcourses_s1, bcourses_s2) 
                       VALUES (%s, %s, %s, %s, %s, %s)"""
             
            values = ()
            crs.execute(query, values)

            crs.execute(f"CREATE TABLE {x}(sid INT PRIMARY KEY, sname VARCHAR(100), password VARCHAR(100), sbranch VARCHAR(100), semester INT,scourses VARCHAR(255))")

if __name__ == "__main__":
    app.run(debug=True)