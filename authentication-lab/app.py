from flask import Flask, render_template, request, redirect, url_for, flash
from flask import session as login_session
import pyrebase



config = {
  'apiKey': "AIzaSyAVCMdA2KL1Bi5R5MiAy-T82OEW7CbtcgA",
  'authDomain': "clab-17389.firebaseapp.com",
  'projectId': "clab-17389",
  'storageBucket': "clab-17389.appspot.com",
  'messagingSenderId': "431047308597",
  'appId': "1:431047308597:web:56bf47769442331c07c87c",
  'measurementId': "G-DZ5BDQ5759",
  "databaseURL":""
}
firebase= pyrebase.initialize_app(config)
auth = firebase.auth() 

app = Flask(__name__, template_folder='templates', static_folder='static')
app.config['SECRET_KEY'] = 'super-secret-key'


@app.route('/', methods=['GET', 'POST'])
def signin():
    return render_template("signin.html")

app.route('/signup', methods=['GET', 'POST'])
def signup():
   error = ""
   if request.method == 'POST':
       email = request.form['email']
       password = request.form['password']
       try:
            login_session['user'] = tim
auth.create_user_with_email_and_password(email, password)
           return redirect(url_for('home'))
       except:
           error = "Authentication failed"
   return render_template("signup.html")



@app.route('/add_tweet', methods=['GET', 'POST'])
def add_tweet():
    return render_template("add_tweet.html")


if __name__ == '__main__':
    app.run(debug=True)