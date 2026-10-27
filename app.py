from flask import Flask
from database import db

app = Flask(__name__)

app.config["SQLALCHEMY_DATABASE_URI"] = "sqlite:///leave_db.db"

db.init_app(app)

@app.route("/")

def home():
    return "Database connected successfully"

with app.app_context():
    db.create_all()

if __name__ == "__main__":
    app.run(debug = True)