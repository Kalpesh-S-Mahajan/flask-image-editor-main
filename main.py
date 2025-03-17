# pip3 install flask opencv-python
from flask import Flask, render_template, request, flash,session,redirect
from werkzeug.utils import secure_filename
import cv2
import os
import sqlite3

con = sqlite3.connect("database.db")
con.execute("create table if not exists login(username text,email text, password text)")
con.close()


UPLOAD_FOLDER = 'uploads'
ALLOWED_EXTENSIONS = {'png', 'webp', 'jpg', 'jpeg', 'gif'}

app = Flask(__name__)
app.secret_key = 'super secret key'
HOME = os.getcwd()
app.config['UPLOAD_FOLDER'] = os.path.join(HOME, UPLOAD_FOLDER)

log_emp = "kalpesh@gmail.com"
log_psw = "12345"

def allowed_file(filename):
    return '.' in filename and \
           filename.rsplit('.', 1)[1].lower() in ALLOWED_EXTENSIONS

def processImage(filename, operation):
    print(f"the operation is {operation} and filename is {filename}")

    img = cv2.imread(os.path.join(app.config['UPLOAD_FOLDER'], filename))
    
    match operation:
        case "ccrt":
            imgProcessed =cv2.cvtColor(img, cv2.COLOR_BGR2RGB)
            newFilename = f"static/{filename}"

            cv2.imwrite(newFilename, imgProcessed)
            return newFilename
        
        case "cgray":
            imgProcessed = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
            newFilename = f"static/{filename}"
            cv2.imwrite(newFilename, imgProcessed)
            return newFilename
        case "cwebp":  
            newFilename = f"static/{filename.split('.')[0]}.webp"
            cv2.imwrite(newFilename, img)
            return newFilename
        case "cjpg": 
            newFilename = f"static/{filename.split('.')[0]}.jpg"
            cv2.imwrite(newFilename, img)
            return newFilename
        case "cpng": 
            newFilename = f"static/{filename.split('.')[0]}.png"
            cv2.imwrite(newFilename, img)
            return newFilename
    print('NO MATCH FOUND')

@app.route("/home")
def index():
    return render_template("index.html")
@app.route("/")
def home():
    return render_template("login.html")

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
   

@app.route('/logout')
def logout():
    session.clear()
    return redirect("/")


@app.route("/register",methods=["POST"])
def register():
       nme = request.form.get("nme")
       email = request.form.get("emp")
       psw = request.form.get("psw")
       con = sqlite3.connect("database.db")
       cur = con.cursor()
       cur.execute("insert into login(username,email,password)values(?,?,?)",(nme,email,psw))
       con.commit()
       con.close()
       return redirect("/home")
   
   
@app.route("/about")
def about():
    return render_template("about.html")


@app.route("/how")
def how():
    return render_template("how.html") 
# In this section I am trying to call the same file by a different route.
@app.route("/contact")
def contact():
    return render_template("contact.html") 

@app.route("/edit", methods=["GET", "POST"])
def edit():
    if request.method == "POST": 
        operation = request.form.get("operation")
        # check if the post request has the file part
        if 'file' not in request.files:
            flash('No file part')
            return "error"
        file = request.files['file']
        # If the user does not select a file, the browser submits an
        # empty file without a filename.
        if file.filename == '':
            flash('No selected file')
            return "error no selected file"
        if file and allowed_file(file.filename):
            filename = secure_filename(file.filename)
            file.save(os.path.join(app.config['UPLOAD_FOLDER'], filename))
            new = processImage(filename, operation)
            flash(f"Your image has been processed and is available <a href='/{new}' target='_blank'>here</a>")
            return render_template("index.html")

    return render_template("index.html")

if __name__ == '__main__':
    app.run(debug=True, port=5000)
