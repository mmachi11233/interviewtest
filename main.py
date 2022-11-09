# This is a sample Python script.

# Press Shift+F10 to execute it or replace it with your code.
# Press Double Shift to search everywhere for classes, files, tool windows, actions, and settings.


from flask import Flask, render_template, url_for, flash, redirect
from forms import RegistrationForm



app = Flask(__name__)

app.config.update(dict(
    SECRET_KEY="powerful secretkey",
    WTF_CSRF_SECRET_KEY="a csrf secret key"
))

@app.route("/register")
def home():
    return render_template("register.html")

@app.route("/", methods=['GET', 'POST'])
def register():
    form = RegistrationForm()
    if form.validate_on_submit():
        flash(f'Details filled in for {form.fullname.data}!', 'success')
        return redirect(url_for('register'))
    return render_template("home.html", title='login', form=form)


if __name__ == "__main__":
    app.run()
