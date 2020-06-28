import os
from flask import Flask, render_template, redirect, request, url_for
from flask_pymongo import PyMongo
from bson.objectid import ObjectId

app = Flask(__name__)
app.config["MONGO_DBNAME"] = 'secret_recipes'
app.config["MONGO_URI"] = 'mongodb+srv://soolander:Waynelorisa@myfirstcluster-6szsu.mongodb.net/secret_recipes?retryWrites=true&w=majority'

mongo = PyMongo(app)


@app.route('/')
@app.route('/get_recipes')
def get_tasks():
    return render_template("recipes.html", recipes=mongo.db.secret_in.find())



if __name__ == '__main__':
    app.run(host=os.environ.get('IP'),
            port=int(os.environ.get('PORT')),
            debug=True)