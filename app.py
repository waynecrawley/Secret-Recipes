import os
from flask import Flask, render_template, redirect, request, url_for
from flask_pymongo import PyMongo
from bson.objectid import ObjectId

if os.path.exists("env.py"):
    import env

app = Flask(__name__)
app.config["MONGO_DBNAME"] = 'secret_recipes'
app.config["MONGO_URI"] = os.environ.get("MONGO_URI")
app.secret_key = os.environ.get("SECRET_KEY")


mongo = PyMongo(app)


@app.route('/')
@app.route('/get_recipes')
def get_tasks():
    return render_template("recipes.html", recipes=mongo.db.recipes.find())

@app.route('/add_recipe')
def add_recipe():
    return render_template('addrecipes.html')


if __name__ == '__main__':
    app.run(host=os.environ.get('IP'),
            port=int(os.environ.get('PORT')),
            debug=True)