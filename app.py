from flask import Flask, render_template, request, redirect,session
from pymongo import MongoClient
import base64

app = Flask(__name__)
app.secret_key = "secretkey"

client = MongoClient("mongodb://localhost:27017/")
db = client["crudDB"]
col = db["users"]
users = db['okkk']

@app.route('/', methods=['GET', 'POST'])
def index():
    if request.method == 'POST':
        name = request.form['name']
        age = request.form['age']
        photo = request.files['photo']
        photo_data = base64.b64encode(photo.read()).decode('utf-8')
        col.insert_one({"name": name, "age": age, "photo": photo_data})
        return redirect('/')

    users = list(col.find({}, {"_id": 0}))
    return render_template('index.html', users=users, current_user=session.get('user', 'Guest'))


@app.route('/update', methods=['GET', 'POST'])
def update():
    if request.method == 'POST':
        name = request.form['name']
        new_age = request.form['age']
        col.update_one({"name": name}, {"$set": {"age": new_age}})
        return redirect('/')
    return render_template('update.html')

@app.route('/delete', methods=['GET', 'POST'])
def delete():
    if request.method == 'POST':
        name = request.form['name']
        col.delete_one({"name": name})
        return redirect('/')
    return render_template('delete.html')
@app.route('/register',methods=['GET','POST'])
def register():
    if request.method == 'POST':
        uname = request.form['username']
        pwd = request.form['password']

        if users.find_one({"username":uname}):
            return "user already"
        
        users.insert_one({"usersname":uname,"password":pwd})
        return redirect('/login')
    
    return render_template('register.html')


@app.route('/login',methods=['GET','POST'])
def login():
    if request.method == 'POST':
        uname =request.form['username']
        pwd = request.form['password']

        user = users.find_one({"usersname":uname,"password":pwd})
        if user:
            session['user'] = uname
            return redirect('/')
        else:
            return "invalid credentaials"
        
    return render_template('login.html')

import os

if __name__ == '__main__':
    port = int(os.environ.get('PORT', 5000))
    app.run(host='0.0.0.0', port=port)

