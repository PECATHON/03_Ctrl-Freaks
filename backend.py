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
def vendor():
    return render_template("vendor_login.html")

@app.route("/admin")
def admin():
    return render_template("admin_login.html")

@app.route("/client")
def client():
    return render_template("client_login.html")


@app.route("/vendor_login", methods=["POST","GET"])
def vendor_login():
    username = request.form["username"]
    password = request.form["password"]
    print(username)

    crs.execute("SELECT USERNAME,PASSWORD FROM VENDORS")
    data=crs.fetchall()
    print(data[0])
    for a in data:
        if a[0]==username:
            if a[1]==password:
                session["user"] = a[1]
                session["role"] = "vendor"
                flash("Vendor login successful!", "success")
                return redirect(url_for("vendor_dashboard")) 
                break
    else:
        flash("Invalid Vendor credentials", "danger")
        return redirect(url_for("admin"))

@app.route("/vendor_r",methods=["POST","GET"])
def vendor_r():
            return render_template("vendor_dashboard.html")

@app.route("/vendor_register")
def vendor_register():
            r_name=request.form["res_name"]
            ow_name=request.form["Ow_name"]
            ph_num=request.form["Ph_num"]
            email=request.form["Email"]
            address=request.form["Address"]
            city=request.form["City"]
            type=request.form["Type"]
            fssai=request.form["FSSAI"]
            gstin=request.form["GSTIN"]
            uname=request.form["username"]
            password=request.form["password"]
            
            x=0
            query = """INSERT INTO vendor (, bname, bseats, bstrength, bcourses_s1, bcourses_s2) 
                       VALUES (%s, %s, %s, %s, %s, %s)"""
             
            values = ()
            crs.execute(query, values)

            crs.execute(f"CREATE TABLE {x}(sid INT PRIMARY KEY, sname VARCHAR(100), password VARCHAR(100), sbranch VARCHAR(100), semester INT,scourses VARCHAR(255))")

@app.route("/vendor/dashboard")
def vendor_dashboard():
    if "user" in session and session.get("role") == "vendor":
        return render_template("vendor_dashboard.html")
    else:
        flash("You must log in as Vendor first", "danger")
        return redirect(url_for("vendor"))

if __name__ == "__main__":
    app.run(debug=True)