from flask import Flask, render_template
from flask_pymongo import PyMongo

app = Flask(__name__)
app.config["MONGO_URI"] = "mongodb://localhost:27017/puppies"
mongo = PyMongo(app)

@app.route("/")
def home_page():
    puppies = mongo.db.inventory.find({})
    
    return render_template("index.html",
        puppies=puppies)