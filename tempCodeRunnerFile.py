@app.route("/login_validation", methods=["POST"])
def login_validation():
    email = request.form.get("emp")
    password = request.form.get("psw")
    con = sqlite3.connect("database.db")
    con.row_factory = sqlite3.Row
    cur = con.cursor()
    cur.execute("select * from login where email=? and password=?",(email,password))
    data = cur.fetchone()
    if data:
        session["email"] = data["email"]
        session["password"] = data["password"]
        return redirect("/home")
    else:
        return "Login Failed"
   