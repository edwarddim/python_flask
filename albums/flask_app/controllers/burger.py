

# ROUTE TO RENDER THE BURGER CREATION FORM
@app.route("/burger/create")
def create():
    return render_template("create.html")


# PROCESSING THE BURGER CREATION
@app.post("/burger/create")
def process():
    # VALIDATE THE BURGER
    if not Burger.validate_burger(request.form):
        return redirect("/burger/create")

    # CREATE A BURGER METHOD
    Burger.save(request.form)
    return redirect("/dashboard")