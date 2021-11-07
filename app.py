from flask import Flask, render_template, request
from werkzeug.utils import secure_filename, unescape

app = Flask(__name__)


@app.route("/", methods=["GET"])
def index():
    return render_template("index.html", brand_name="ABC株式会社")


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


@app.route("/upload", methods=["GET"])
def get_upload():
    return render_template("upload.html")


@app.route("/upload", methods=["POST"])
def post_upload():

    if request.files["image"]:
        f = request.files["image"]
        filepath = "static/{}".format(secure_filename(f.filename))
        f.save(filepath)

        return render_template("upload_check.html", name=filepath)
