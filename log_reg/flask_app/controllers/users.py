from flask_bcrypt import Bcrypt

@app.route("/")
def index():
    return render_template('index.html')

# PROCESS THE REGISTER
@app.post("/register")
def register():
    # IF REGISTER VALIDATIONS FAIL
    if not User.validate_register(request.form):
        return redirect("/")
    # IF REGISTER VALIDATIONS PASS
    pw_hash = Bcrypt.generate_password_hash(request.form['password'])
    data = {
        'first_name':request.form['first_name'],
        'last_name':request.form['last_name'],
        'email':request.form['email'],
        'password':pw_hash
    }
    user_id = User.save(data)
    session['user_id'] = user_id
    return redirect("/home")

# PROCESS THE LOGIN
@app.post("/login")
def login():
    # CHECK TO SEE IF EMAIL EXISTS IN DB
    data = {
        'email':request.form['email']
    }
    user_in_db = User.find_user_by_email(data)
    if not user_in_db:
        flash("INVALID EMAIL")
        return redirect("/")
    # CHECK TO SEE IF THE PASSWORD MATCHES
    if not Bcrypt.check_password_hash(user_in_db.password, request.form['password']):
        flash("INVALID PASSWORD")
        return redirect("/")
    session['user_id'] = user_in_db.id
    return redirect("/home")


@app.get("/home")
def home():
    data = {
        'id':session['user_id']
    }
    user = User.find_by_id(data)
    return render_template("home.html")


