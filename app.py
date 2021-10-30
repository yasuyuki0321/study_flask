from flask import Flask, render_template, request

app = Flask(__name__)


@app.route("/login", methods=["GET"])
def ger_login():
    return render_template("login.html")


@app.route("/login", methods=["POST"])
def post_login():

    print(request.form)

    if request.form["name"] and request.form["email"]:
        return render_template(
            "check.html", email=request.form["email"], name=request.form["name"]
        )
    else:
        return render_template("error.html")
