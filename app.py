import csv
import smtplib
from flask import Flask, render_template, redirect, url_for, request
from wtforms import StringField, TextAreaField, form
from wtforms.fields.html5 import EmailField
from wtforms.validators import InputRequired, Email
from flask_wtf import FlaskForm
from forms import MailForm, ReminderForm, PasswordForm, BookmarkForm


app = Flask(__name__)
app.debug = True

import os

SECRET_KEY = os.urandom(32)
app.config['SECRET_KEY'] = SECRET_KEY

url = ""


class PasswordForm(FlaskForm):
    password = StringField('password', validators=[InputRequired()])


class ReminderForm(FlaskForm):
    reminders = StringField('reminder', validators=[InputRequired()])


class MailForm(FlaskForm):
    mail = EmailField('email', validators=[InputRequired(), Email()])
    contents = TextAreaField('contents', validators=[InputRequired()])


class BookmarkForm(FlaskForm):
    identifier = StringField('identifier', validators=[InputRequired()])
    link = StringField('link', validators=[InputRequired()])


@app.route('/base')
def base():
    return render_template('base.html')


@app.route('/reset', methods=["POST", "GET"])
def reset():
    if request.method == "POST":
        return render_template("Reset.html")


@app.route('/test', methods=["POST", "GET"])
def confirmreset():
    if request.method == "POST":
        answer = request.form["answer"]
        x = "soen287"


        if answer == x:

            # opening the file with w+ mode truncates the file
            f = open("../a@/ data/password.csv", "w+")

            f.close()


            return redirect(url_for('confirm'))
        else:
            return redirect('/access')
    else:
        return render_template("Login.html")


@app.route('/confirm')
def confirm():
    return render_template("Change.html")


@app.route('/confirmchange', methods=["POST", "GET"])
def finalchange():
    if request.method == "POST":
        form = PasswordForm()
        if form.is_submitted():
            with open(' data/password.csv', 'a') as f:
                writer = csv.writer(f)
                writer.writerow(request.form["newPassword"])
            return redirect("/")
            return render_template("Login.html")
    else:
        return redirect("/")
        return render_template("Login.html")


@app.route("/", methods=["POST", "GET"])
def login():
    if request.method == "POST":
        user = request.form["ps"]
        x = ""
        with open('../a@/ data/password.csv') as csv_file:
            csv_reader = csv.reader(csv_file, delimiter=',')
            line_count = 0
            for row in csv_reader:
                if line_count == 0:

                    for k in row:
                        x += str(k)
                    line_count += 1
                else:
                    try:

                        for k in row:
                            x += str(k)
                        line_count += 1
                    except:
                        print("")


        if user == x:
            return redirect(url_for("base", usr=user))
        else:
            return render_template("Wrong.html")
    else:
        return render_template("Login.html")


@app.route('/home')
def template1():
    return render_template("base.html")


@app.route('/CV.html')
def CV():
    return render_template("CV.html")

@app.route('/CVguest.html')
def CVguest():
    return render_template("CVguest.html")


@app.route("/upload_image.html")
def seeCV():
    return render_template("upload_image.html")


@app.route('/Bookmarks.html')
def Bookmarks():
    return render_template("Bookmarks.html")


@app.route('/BookmarksData', methods=["POST"])
def Bookmarsregister():
    form = BookmarkForm()
    if request.method == "POST" and form.is_submitted():
        identifier = request.form.get("identifier")
        link = request.form.get("link")
        with open(' data/bookmarks.csv', 'a') as f:
            writer = csv.writer(f)
            writer.writerow(identifier)
            writer.writerow(link)
    return render_template("Bookmarks.html")


@app.route('/BookmarksShow', methods=["POST"])
def showbookmarks():
    x = ""
    id = True
    listID = []
    listLink = []
    with open('../a@/ data/bookmarks.csv') as csv_file:
        csv_reader = csv.reader(csv_file, delimiter=',')
        line_count = 1
        for row in csv_reader:
            for k in row:
                x += str(k)
            if id and len(x)>0:
                listID.append(x)

                id = False
                x = ""
            elif id == False and len(x) > 0:
                listLink.append(x)

                id = True
                x = ""

    return render_template("BookmarksData.html", id=listID, link=listLink)


@app.route('/Documents.html')
def Documents():
    return render_template("Documents.html")


@app.route('/Projects.html')
def Projects():
    return render_template("Projects.html")


@app.route('/ProjectsGuest.html')
def ProjectsGuest():
    return render_template("ProjectsGuest.html")


@app.route('/Mail.html')
def Mail():
    return render_template("Mail.html")


@app.route('/MailGuest.html')
def MailGuest():
    return render_template("MailGuest.html")


@app.route('/MessageSentGuest.html')
def MailGuestSent():
    return render_template("MessageSentGuest.html")


@app.route('/contact_mail', methods=['GET', 'POST'])
def handle_mailing():
    if request.method == "POST":
        form = MailForm()
        if form.is_submitted():
            email = request.form.get("email")
            message = request.form.get("contents")
            server = smtplib.SMTP("smtp.gmail.com", 587)
            server.starttls()
            server.login("soen287assignment@gmail.com", "soen287password")
            server.sendmail("soen287assignment@gmail.com", email, message)
            return render_template('MessageSent.html', data=request.form, mssage=message)
        else:
            return render_template("base.html")
    else:
        return render_template("base.html")


app.config["IMAGE_UPLOADS"] = "C:/Users/xelma/PycharmProjects/a@/static/"


@app.route("/upload-image", methods=["POST", "GET"])
def upload_image():
    if request.method == "POST":
        if request.files:
            image = request.files["image"]
            image.save(os.path.join(app.config["IMAGE_UPLOADS"], image.filename))

            return redirect(request.url)
    return render_template("base.html")


@app.route("/Reminders.html")
def reminder():
    return render_template("Reminders.html")


@app.route('/Reminders_data', methods=['GET', 'POST'])
def handle_reminders():
    form = ReminderForm()
    if form.is_submitted():
        with open(' data/messages.csv', 'a') as f:
            writer = csv.writer(f)
            writer.writerow(request.form['reminder'])
        # return render_template("RemindersData.html", result=request.form['reminder'])
    return render_template("Reminders.html")


@app.route('/RemindersData.html')
def listReminders():
    lis = []

    x = ""
    y = ""
    with open('../a@/ data/messages.csv') as csv_file:
        csv_reader = csv.reader(csv_file, delimiter=',')
        line_count = 0
        for row in csv_reader:
            if line_count == 0:

                for k in row:
                    x += str(k)
                line_count += 1
            else:
                try:

                    for k in row:
                        x += str(k)
                    line_count += 1
                except:
                    print("")

            if len(x) > 0:

                lis.append(x)

            x = ""


    return render_template("RemindersData.html", list=lis)


@app.route('/delete', methods=["POST", "GET"])
def deletereminders():
    if request.method == "POST":
        # opening the file with w+ mode truncates the file
        f = open("../a@/ data/messages.csv", "w+")

        f.close()
    return render_template("Reminders.html")


@app.route('/access')
def reaccess():
    return render_template("Wrong.html")


@app.route('/Wrong.html', methods=["POST"])
def noAccess():
    return redirect("/")


@app.route('/guest', methods=["POST"])
def guestaccess():
    if request.method == "POST":
        return redirect('/guestbase')


@app.route('/guestbase', methods=["POST", "GET"])
def gueest():
    return render_template("Guest.html")


@app.route('/Guest.html', methods=["POST", "GET"])
def gueestbase():
    return render_template("Guest.html")



if __name__ == '__main__':
    app.run(Debug=True)
