# Banking Website
from flask import Flask, render_template, request, session, url_for, redirect

from flask.globals import request

from functions import Bank

# app initialisation
app = Flask(__name__)

users = {}
# to print the users to the console
print(users)
app.secret_key = 'hhft7yqr7526%$^"£"'



# defining the home page
@app.route('/')
def home():
  if 'user' in session:
    firstname = request.form.get('firstname')
    lastname = request.form.get('lastname')
    money = user.viewBalance()
    return render_template('home.html', money=money)
    
  else:
    return render_template('home.html')

# defining the login page
@app.route('/login', methods = ['GET', 'POST'])
def login():
  global user
  if request.method == 'POST':
    username = request.form['username']
    password = request.form['password']


    if username in users and users[username] == password:
      session['user'] = username
      session['fname'] = request.form['firstname']
      session['lname'] = request.form['lastname']
      

      user = Bank(session['user'])

      print(user.showDetails())

      print('Login Successful')
      return render_template('home.html',firstname = request.form.get('firstname'), lastname = request.form.get('lastname'))
    else:
      print('Email doesnt exist or wrong password')
      return render_template('login.html')
      

  return render_template('login.html')


# defining the register page
@app.route('/register', methods= ['GET', 'POST'])
def register():
  if request.method == 'POST':
    username = request.form['username']
    if username in users:
      print('User already exists')
      return render_template('register.html')
    else:
      password = request.form['password']
      users[username] = password
      print('user created')
      print(users)
      
      session['user'] = username
      session['fname'] = request.form['firstname']
      session['lname'] = request.form['lastname']
      
      return render_template('home.html',firstname = request.form.get('firstname'), lastname = request.form.get('lastname'))
  else:
    return render_template('register.html')

# defining the deposit page
@app.route('/deposit', methods = ['GET', 'POST'])
def deposit():
  global user
  if request.method == 'POST' and 'user' in session:
    user = Bank(session['user'])
    amount = request.form['deposit']
    user.deposit(amount)
    print(user.showDetails())
    
  
    
    return render_template('deposit.html')
  else:
    return render_template('deposit.html')

#defining the withdraw page
@app.route('/withdraw', methods = ['GET', 'POST'])
def withdraw():
  global user
  if request.method == 'POST':
    user = Bank(session['user'])
    amount = request.form['withdraw']
    user.withdraw(amount)
    print(user.showDetails())
    return render_template('withdraw.html')
  else:
    return render_template('withdraw.html')

# defining the transfer page
@app.route('/transfer', methods = ['GET', 'POST'])
def transfer():
  global user
  if request.method == 'POST':
    user = Bank(session['user'])
    amount = request.form['transfer']
    user.transfer(amount)
    print(user.showDetails())
    return render_template('transfer.html')
  else:
    return render_template('transfer.html')

# defining the dashboard page
@app.route('/dashboard', methods = ['GET', 'POST'])
def dashboard():
  global user
  firstname = request.form.get('firstname')
  lastname = request.form.get('lastname')
  if request.method == 'POST':
    user = Bank(session['user'])
    return render_template('home.html',firstname = firstname, lastname = lastname)
  else:
    return render_template('home.html',firstname = firstname, lastname = lastname)

# @app.route('/logout')
# def logout():
#   session.pop('user', None)
#   return redirect(url_for('home'))
  


if __name__ == "__main__":
  app.run(debug=True)
