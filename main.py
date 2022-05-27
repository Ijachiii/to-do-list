from flask import Flask, render_template, url_for, request, redirect
from flask_sqlalchemy import SQLAlchemy

app = Flask(__name__)

app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///list.db'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
db = SQLAlchemy(app)


class List(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    activity = db.Column(db.String, unique=True, nullable=False)


tolist = []


@app.route("/", methods=["GET", "POST"])
def home():
    if request.method == "POST":
        tolist.append(request.form["todo"])
        print(tolist)
        return redirect(url_for("home"))
    return render_template("index.html", tolist=tolist)


if __name__ == "__main__":
    app.run(debug=True)
