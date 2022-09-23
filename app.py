from flask import *
from dbhelper import DB

app = Flask(__name__)
db = DB()

is_logged_in = 0


# decorators
@app.route('/')
def hello_world():
    global is_logged_in

    if is_logged_in == 1:
        return "not possible"

    return render_template('login_form.html')


@app.route("/register")
def register():
    return render_template("/registration.html")


@app.route('/login_validation', methods=['POST'])
def login_validation():
    global is_logged_in
    email = request.form.get("user's_email")
    password = request.form.get("user's_password")

    data = db.search(email, password)
    if len(data) == 0:
        return "Incorrect"
    else:
        is_logged_in = 1
        return render_template('home.html', data=data)


# link to english
@app.route('/english', methods=['POST'])
def english():
    return render_template("english.html")


# link to hindi
@app.route('/hindi', methods=['POST'])
def hindi():
    return render_template("hindi.html")


# link to bengali
@app.route('/bengali', methods=['POST'])
def bengali():
    return render_template("bengali.html")


# link to marathi
@app.route('/marathi', methods=['POST'])
def marathi():
    return render_template("marathi.html")


@app.route('/logout')
def logout():
    global is_logged_in
    is_logged_in = 0
    return render_template('login_form.html')


@app.route('/reg_validation', methods=['POST'])
def reg_validation():
    # get all the data form user

    Name = request.form.get("user's_name")
    Email = request.form.get("user's_email")
    Password = request.form.get("user's_password")
    City = request.form.get("user's_city")
    Gender = request.form.get("user's_gender")

    result = db.insert(Name, Email, Password, City, Gender)

    if result == 1:
        return 'Registration Done'
    else:
        return 'not done'


app.run(debug=True)
