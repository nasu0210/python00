from flask import Flask, render_template, request, redirect, url_for
from dao import UserDAO

app=Flask(__name__)
user_dao=UserDAO()

@app.route('/')
def home():
    return redirect(url_for('register'))

@app.route('/register',methods=['GET','POST'])
def register():
    if request.method=='POST':
        email=request.form['email']
        username=request.form['username']
        password=request.form['password']
        user_dao.create_user(email,username,password)
        return redirect(url_for('users'))
    return render_template('register.html')

@app.route('/users')
def users():
    users=user_dao.get_all_users()
    return render_template('users.html',users=users)


if __name__=='__main__':
    app.run(host='0.0.0.0',port=9400,debug=True)