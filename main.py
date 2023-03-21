from flask import Flask, render_template, request, session, url_for, redirect

from functions import Bank

app = Flask(__name__)
users = {}
print(users)
app.secret_key = 'hkjkjhfjoojoff1357216%$^"£"'

@app.route('/')
def home():
    return render_template('home.html')

@app.route('/login', methods = ['GET', 'POST'])
def login():
    global user
    if request.method == 'POST':
        email = request.form['email']
        password = request.form['password']

        if email in email and email[email] == password:
            session['email'] = email

            email = Bank(session['email'])

            print(email.showDetails())

            print('Login successful')
            return render_template('dashboard')
        else:
            print('Username does not exist or wrong password')
            return render_template('login.html')
    return render_template('login.html')

@app.route('/register', methods = ['GET', 'POST'])
def register():
    if request.method == 'POST':
        email = request.form['email']
        if email in email:
            print('Email already exists')
            #include flash message
            return render_template('login.html')
        else:
            password = request.form['password']
            email[email] = password
            print('User created')
            print(email)
            return render_template('dashboard.html')
    else:
        return render_template('dashboard.html')

@app.route('/deposit', methods = ['GET', 'POST'])
def deposit():
    if request.method == 'POST':
        amount = request.form['deposit']
        user.deposit(amount)
        print(user.showDetails())
        return render_template('deposit.html')
    else:
        return render_template('deposit.html')


@app.route('/withdraw', methods = ['GET', 'POST'])
def withdraw():
    if request.method == 'POST':
        amount = request.form['withdraw']
        user.withdraw(amount)
        print(user.showDetails())
        return render_template('withdraw.html')
    else:
        return render_template('withdraw.html')

@app.route('/transfer', methods = ['GET', 'POST'])
def transfer():
    if request.method == 'POST':
        amount = request.form['transfer']
        user.transfer(amount)
        print(user.showDetails())
        return render_template('transfer.html')
    else:
        return render_template('transfer.html')


if __name__ == "__main__":
    app.run(debug = True)