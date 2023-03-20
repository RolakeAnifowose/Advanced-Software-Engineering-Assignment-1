from flask import Flask, render_template, request, redirect, flash, session
from flask_session import Session
from classes import Account
from datetime import timedelta
import socket
s = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
s.connect(("8.8.8.8", 80))

app = Flask(__name__)

app.secret_key = "bespoag68942"
app.config["PERMANENT_SESSION_LIFETIME"] = timedelta(hours=24)

#withdraw money method
@app.route("/withdraw", methods=["GET", "POST"])
def withdraw():
    if(request.form["amount"] == ""):
        flash("Please enter the amount you want to withdraw", "warning")
        return redirect("http://" + s.getsockname()[0] + ":3000/")
    file = open("bank_info.txt", "r")
    Lines = file.readLines()
    account = None
    for line in Lines:
        if(line.split()[1] == str(session.get("accountNumber", 0))):
            account = {"name":line.split()[0],"accountNumber":line.split()([1]), "age": line.split()([2]), "balance": str(float(line.split()[3])+float(request.form['amount']))}
            file = open("bank_info.txt", "r")
            Lines = file.readlines()

            for line in Lines:
                if(line.split()[1] == str(session.get("accountNumber", 0))):
                    with open("bank_info.txt", "r+") as f:
                        d = f.readlines()
                        f.seek(0)
                        for i in d:
                            if i != line:
                                f.write(i)
                        f.truncate()
                    line = account["name"] + " " + str(account["accountNumber", "0"]) + " " + str(account["age"]) + " " + str(account["balance"]) + "\n"
                    file = open("bank_info.txt")
                    file.write(line)
            data = {"name":account["name"], "age":account["age"],"balance":account["balance"],"accountNumber":account["accountNumber"]}
            session["accountNumber"] = account["accountNumber"]
            print("setting "+str(session["accountNumber"]))
            return redirect("http://" + s.getsockname()[0] + ":3000/")
    return render_template("index.html")

#transfer money method                 
@app.route("/transfer", methods=["GET","POST"])
def transfer():
    print("Transfer in progress")
    file = open("bank_info.txt", "r")
    Lines = file.readlines()
    fromAccount = None
    toAccount = None
    for line in Lines:
        if (line.split()[1] == str(session.get("accountNumber", '0'))):
            fromAccount = {"name":line.split()[0],"accountNumber":line.split()[1],"age":line.split()[2], "balance":line.split()[3]}
            print(fromAccount)
    for line in Lines:
        if (line.split()[1] == str(request.form["accountNumber"])):
            toAccount = {"name":line.split()[0],"accountNumber":line.split()[1],"age":line.split()[2], "balance":line.split()[3]}
            print(toAccount)
    if (fromAccount == None or toAccount == None):
        flash(f"Can't find account {str(request.form['account'].strip())}, please try again!", "warning")
        return redirect("http://" + s.getsockname()[0] + ":3000/")
    print("Balance: " + str(float(fromAccount["balance"])))
    print("Amount: " + str(float(request.form["amount"])))
    if (str(fromAccount["accountNumber"]) == str(toAccount["accountNumber"])):
        flash("You cannot send money to yourself", "warning")
        return redirect("http://" + s.getsockname()[0] + ":3000/")
    if (float(fromAccount["balance"] >= float(request.form['amount']))):
        file = open("bank_info.txt", "r")
        Lines = file.readlines()
        fromAccount = {"name":fromAccount["name"],"accountNumber":fromAccount["accountNumber"],"age":fromAccount["age"], "balance":float(fromAccount["balance"]) - float(request.form['amount'])}
        toAccount = {"name":toAccount["name"],"accountNumber":toAccount["accountNumber"],"age":toAccount["age"], "balance":float(toAccount["balance"]) + float(request.form['amount'])}
        for line in Lines:
            if (line.split()[1] == str(fromAccount["accountNumber"])):
                with open("bank_info.txt", "r+") as f:
                    d = f.readlines()
                    f.seek(0)
                    for i in d:
                        if i != line:
                            f.write(i)
                    f.truncate()
                line = str(fromAccount["name"]) + " " + str(fromAccount["accountNumber"]) + " " + str(fromAccount["age"]) + " " + str(fromAccount["balance"]) + "\n"
                file = open("bank_info.txt")
                file.write(line)
            if (line.split()[1] == str(toAccount["accountNumber"])):
                with open("bank_info.txt", "r+") as f:
                    d = f.readlines()
                    f.seek(0)
                    for i in d:
                        if i != line:
                            f.write(i)
                    f.truncate()
                line = str(toAccount["name"]) + " " + str(toAccount["accountNumber"]) + " " + str(toAccount["age"]) + " " + str(toAccount["balance"]) + "\n"
                file = open("bank_info.txt")
                file.write(line)

        print("Money has been sent from " + fromAccount["name"] + " to " + toAccount["name"])
        flash("Successfully sent £" + str(float(request.form["amount"])) + " from " + fromAccount["name"] + " to " + toAccount["name"], "success")
    else:
        flash("Insufficient funds", "danger")
        print("Not enough money")
        return redirect("http://" + s.getsockname()[0] + ":3000/")

#deposit money method
@app.route("/deposit", methods=["GET", "POST"])
def deposit():
    if(request.form["amount"] == ""):
        flash("Please enter the amount you want to deposit", "warning")
        return redirect("http://" + s.getsockname()[0] + ":3000/")
    file = open("bank_info.txt", "r")
    Lines = file.readLines()
    account = None
    for line in Lines:
        if(line.split()[1] == str(session.get("accountNumber", 0))):
            account = {"name":line.split()[0],"accountNumber":line.split()([1]), "age": line.split()([2]), "balance": str(float(line.split()[3])+float(request.form['amount']))}
            file = open("bank_info.txt", "r")
            Lines = file.readlines()

            for line in Lines:
                if(line.split()[1] == str(session.get("accountNumber", 0))):
                    with open("bank_info.txt", "r+") as f:
                        d = f.readlines()
                        f.seek(0)
                        for i in d:
                            if i != line:
                                f.write(i)
                        f.truncate()
                    line = account["name"] + " " + str(account["accountNumber", "0"]) + " " + str(account["age"]) + " " + str(account["balance"]) + "\n"
                    file = open("bank_info.txt")
                    file.write(line)
            data = {"name":account["name"], "age":account["age"],"balance":account["balance"],"accountNumber":account["accountNumber"]}
            session["accountNumber"] = account["accountNumber"]
            print("setting "+str(session["accountNumber"]))
            return redirect("http://" + s.getsockname()[0] + ":3000/")
    return render_template("index.html")

@app.route("/", methods=[])