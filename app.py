from flask import Flask, render_template
from database import db

app = Flask(__name__)

app.config["SQLALCHEMY_DATABASE_URI"] = "sqlite:///leave_db.db"

db.init_app(app)

@app.route("/")
def home():
    return render_template("employee.html")

@app.route("/apply", methods = ["GET", "POST"])
def apply_leave():
    return render_template("apply_leave.html")

with app.app_context():
    db.create_all()

if __name__ == "__main__":
    app.run(debug = True)