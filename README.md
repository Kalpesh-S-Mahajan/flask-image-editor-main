# 🚀 LynxLuminate Studio  
**Seamless Image Conversion with Flask & OpenCV**  

## 📌 Overview  
LynxLuminate Studio is a powerful and user-friendly image converter built using **Flask, OpenCV, HTML, CSS, Bootstrap, and JavaScript**. It allows users to convert images to various formats (JPG, PNG, WEBP) and apply basic transformations with ease.  

## 🎯 Features  
✅ Supports multiple formats: **JPG, PNG, WEBP, GIF**  
✅ Converts images with precision using **OpenCV**  
✅ User-friendly interface with a responsive **Bootstrap** design  
✅ Secure user authentication with **SQLite**  
✅ Easy-to-use upload and edit functionality  

## 🛠️ Tech Stack  
- **Backend:** Flask, OpenCV, SQLite  
- **Frontend:** HTML, CSS, Bootstrap, JavaScript  
- **Database:** SQLite  

## 📂 Project Structure  
```
LynxLuminateStudio/
│── static/            # Processed images storage  
│── templates/         # HTML Templates (login, home, about, etc.)  
│── uploads/           # Uploaded images  
│── main.py            # Flask application (backend logic)  
│── database.db        # SQLite database  
│── .gitattributes     # Git configuration  
│── README.md          # Project Documentation  
```

## 🚀 Installation & Setup  
### 1️⃣ Clone the Repository  
```bash
git clone https:https://github.com/Kalpesh-S-Mahajan/flask-image-editor-main.git
cd LynxLuminateStudio
```

### 2️⃣ Install Dependencies  
Ensure you have **Python 3** installed, then run:  
```bash
pip install flask opencv-python
```

### 3️⃣ Run the Application  
```bash
python main.py
```
The app will run on **http://127.0.0.1:5000/**  

## 📸 How It Works  
1️⃣ **Login/Register** to access the application  
2️⃣ **Upload an image** in JPG, PNG, WEBP, or GIF format  
3️⃣ **Choose an operation** (convert to grayscale, PNG, JPG, WEBP, etc.)  
4️⃣ **Download the processed image**  

## 🔒 User Authentication  
- Users can register and log in via **SQLite** database  
- Login credentials are stored securely  

## 🌟 Contribution  
Feel free to contribute by forking the repo and submitting a **pull request**.  

## 📝 License  
This project is **open-source** under the MIT License.  

