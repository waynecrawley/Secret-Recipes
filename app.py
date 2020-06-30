import os
from flask import Flask, render_template, redirect, request, url_for
from flask_pymongo import PyMongo
from bson.objectid import ObjectId

if os.path.exists("env.py"):
    import env
#Sets up Mongdb database and hides login details in a Environment variable
app = Flask(__name__)
app.config["MONGO_DBNAME"] = 'secret_recipes'
app.config["MONGO_URI"] = os.environ.get("MONGO_URI")
app.secret_key = os.environ.get("SECRET_KEY")


mongo = PyMongo(app)

#Function used to render Home page and display all recipes
@app.route('/')
@app.route('/get_recipes')
def get_recipes():
    return render_template("recipes.html", recipes=mongo.db.recipes.find())

#Function to render addrecipes page
@app.route('/add_recipe')
def add_recipe():
    return render_template('addrecipes.html')


#Fuction to insert recipes into the Database
@app.route('/insert_recipes', methods=['POST'])
def insert_recipes():
    recipes = mongo.db.recipes
    recipes.insert_one(request.form.to_dict())
    return redirect(url_for('get_recipes'))

#Function to Display each individual recipe
@app.route('/show_recipe/<recipe_id>')
def show_recipe(recipe_id):
    return render_template("recipe.html",
            recipe=mongo.db.recipes.find_one({'_id': ObjectId(recipe_id)}))


if __name__ == '__main__':
    app.run(host=os.environ.get('IP'),
            port=int(os.environ.get('PORT')),
            debug=True)


