from flask import Flask, render_template, redirect, request, session, flash
import model

app = Flask(__name__)
app.secret_key = '\xfa\xd7\xe7AOZ\x00\x0f\xaez0\xb1>,cg&N#5ST{\xa2'

@app.route("/")
def index():
    #user_list = model.session.query(model.User).limit(5).all()
    return render_template("index.html")
    #return render_template("user_list.html", users=user_list)

@app.route("/user_list")
def show_users():
    user_list = model.session.query(model.User).options(model.joinedload('ratings')).limit(25).all()
    return render_template("user_list.html", users=user_list)

@app.route("/signup", methods=["GET"])
def show_signup():
    return render_template("signup.html")

@app.route("/signup", methods=["POST"])
def process_signup():
    email = request.form['username']
    password = request.form['password']
    age = request.form['age']
    gender = request.form['gender']
    occupation = request.form['occupation']
    zipcode = request.form['zipcode']
    new_user = model.add_user(email, password, age, gender, occupation, zipcode)
    return redirect("/")


@app.route("/login", methods=["GET"])
def show_login():
    return render_template("login.html")


@app.route("/login", methods=["POST"])
def process_login():
    """Receive the user's login credentials located in the request.form
    dictionary, look up the user and store them in the session."""

    email = request.form['username']
    password = request.form['password']
    user = model.get_user_by_email_password(email, password)
    if user:
    
        session['user'] = user.id
        flash("Successfully logged in")
        return redirect("/user_detail/" + str(user.id))
    else:
        flash("Account not found.")
        return redirect("/login")

@app.route("/logout")
def logout():
    session.clear()
    return redirect("/")

@app.route("/user_detail/<int:user_id>", methods=["GET"])
def show_user_details(user_id):
    user = model.session.query(model.User).get(user_id)
    return render_template("user_detail.html",
                            user = user)
@app.route("/add_rating", methods=["GET", "POST"])
def add_rating():
    if request.method == "GET":
        return "testing add rating page"
    else:
        return "testing post add rating page"

if __name__ == "__main__":
    app.run(debug=True)