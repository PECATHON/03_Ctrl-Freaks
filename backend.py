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


@app.route("/vendor_login", methods=["POST"])
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
        return redirect(url_for("vendor_dashboard"))

@app.route("/vendor_r")
def vendor_r():
            return render_template("vendor_register.html")

@app.route("/vendor_register", methods=["POST","GET"])
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
            
            query = """INSERT INTO vendors (USERNAME,PASSWORD ,NAME, RES_NAME,EMAIL,P_NUM,ADDRESS,CITY,TYPE,FSSAI,GSTIN )
            VALUES (%s, %s, %s, %s, %s, %s,%s, %s, %s, %s, %s)"""
            values = (uname,password,ow_name,r_name,email,ph_num,address,city,type,fssai,gstin)

            crs.execute(query, values)
            myDB.commit()


            return redirect(url_for("vendor_dashboard"))

            #crs.execute(f"CREATE TABLE {uname}(category VARCHAR(100), PID INT PRIMARY KEY, PNAME VARCHAR(100), PRICE FLOAT, Discount VARCHAR(5)")

@app.route("/vendor/dashboard")
def vendor_dashboard():
    if "user" in session and session.get("role") == "vendor":
        return render_template("vendor_dashboard.html")
    else:
        flash("You must log in as Vendor first", "danger")
        return redirect(url_for("vendor"))

if __name__ == "__main__":
    app.run(debug=True)