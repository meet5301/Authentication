
# ---------- Flask + MongoDB Atlas + Authentication + Image Upload ----------

from flask import Flask, render_template, request, redirect, session
from pymongo import MongoClient
import base64, os

app = Flask(__name__)
app.secret_key = "secretkey"

# ---------- MongoDB Atlas Connection ----------
MONGO_URI = "mongodb+srv://meet:meet123@cluster0.fldq0wp.mongodb.net/?appName=Cluster01"
client = MongoClient(MONGO_URI)
db = client["crudDB"]      # Database name
col = db["users"]          # For user data + photo
users = db["okkk"]         # For login/register users

# ---------- HOME PAGE ----------
@app.route('/', methods=['GET', 'POST'])
def index():
    if request.method == 'POST':
        name = request.form['name']
        age = request.form['age']
        photo = request.files['photo']
        photo_data = base64.b64encode(photo.read()).decode('utf-8')
        col.insert_one({"name": name, "age": age, "photo": photo_data})
        return redirect('/')

    all_users = list(col.find({}, {"_id": 0}))
    return render_template('index.html', users=all_users, current_user=session.get('user', 'Guest'))

# ---------- UPDATE ----------
@app.route('/update', methods=['GET', 'POST'])
def update():
    if request.method == 'POST':
        name = request.form['name']
        new_age = request.form['age']
        col.update_one({"name": name}, {"$set": {"age": new_age}})
        return redirect('/')
    return render_template('update.html')

# ---------- DELETE ----------
@app.route('/delete', methods=['GET', 'POST'])
def delete():
    if request.method == 'POST':
        name = request.form['name']
        col.delete_one({"name": name})
        return redirect('/')
    return render_template('delete.html')

# ---------- REGISTER ----------
@app.route('/register', methods=['GET', 'POST'])
def register():
    if request.method == 'POST':
        uname = request.form['username']
        pwd = request.form['password']

        if users.find_one({"username": uname}):
            return "User already exists!"
        
        users.insert_one({"username": uname, "password": pwd})
        return redirect('/login')
    
    return render_template('register.html')

# ---------- LOGIN ----------
@app.route('/login', methods=['GET', 'POST'])
def login():
    if request.method == 'POST':
        uname = request.form['username']
        pwd = request.form['password']

        user = users.find_one({"username": uname, "password": pwd})
        if user:
            session['user'] = uname
            return redirect('/')
        else:
            return "Invalid credentials!"
        
    return render_template('login.html')

# ---------- LOGOUT ----------
@app.route('/logout')
def logout():
    session.pop('user', None)
    return redirect('/login')

# ---------- Run App ----------
if __name__ == '__main__':
    port = int(os.environ.get('PORT', 10000))
    app.run(host='0.0.0.0', port=port)

# ---------- Flask + MongoDB Atlas + Authentication + Image Upload ----------

from flask import Flask, render_template, request, redirect, session
from pymongo import MongoClient
import base64, os

app = Flask(__name__)
app.secret_key = "secretkey"

# ---------- MongoDB Atlas Connection ----------
MONGO_URI = "mongodb+srv://meet:meet123@cluster0.fldq0wp.mongodb.net/?appName=Cluster01"
client = MongoClient(MONGO_URI)
db = client["crudDB"]      # Database name
col = db["users"]          # For user data + photo
users = db["okkk"]         # For login/register users

# ---------- HOME PAGE ----------
@app.route('/', methods=['GET', 'POST'])
def index():
    if request.method == 'POST':
        name = request.form['name']
        age = request.form['age']
        photo = request.files['photo']
        photo_data = base64.b64encode(photo.read()).decode('utf-8')
        col.insert_one({"name": name, "age": age, "photo": photo_data})
        return redirect('/')

    all_users = list(col.find({}, {"_id": 0}))
    return render_template('index.html', users=all_users, current_user=session.get('user', 'Guest'))

# ---------- UPDATE ----------
@app.route('/update', methods=['GET', 'POST'])
def update():
    if request.method == 'POST':
        name = request.form['name']
        new_age = request.form['age']
        col.update_one({"name": name}, {"$set": {"age": new_age}})
        return redirect('/')
    return render_template('update.html')

# ---------- DELETE ----------
@app.route('/delete', methods=['GET', 'POST'])
def delete():
    if request.method == 'POST':
        name = request.form['name']
        col.delete_one({"name": name})
        return redirect('/')
    return render_template('delete.html')

# ---------- REGISTER ----------
@app.route('/register', methods=['GET', 'POST'])
def register():
    if request.method == 'POST':
        uname = request.form['username']
        pwd = request.form['password']

        if users.find_one({"username": uname}):
            return "User already exists!"
        
        users.insert_one({"username": uname, "password": pwd})
        return redirect('/login')
    
    return render_template('register.html')

# ---------- LOGIN ----------
@app.route('/login', methods=['GET', 'POST'])
def login():
    if request.method == 'POST':
        uname = request.form['username']
        pwd = request.form['password']

        user = users.find_one({"username": uname, "password": pwd})
        if user:
            session['user'] = uname
            return redirect('/')
        else:
            return "Invalid credentials!"
        
    return render_template('login.html')

# ---------- LOGOUT ----------
@app.route('/logout')
def logout():
    session.pop('user', None)
    return redirect('/login')

# ---------- Run App ----------
if __name__ == '__main__':
    port = int(os.environ.get('PORT', 10000))
    app.run(host='0.0.0.0', port=port)

