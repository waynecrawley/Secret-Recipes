import os
from flask import Flask, render_template, redirect, request, url_for
from flask_pymongo import PyMongo
from bson.objectid import ObjectId

if os.path.exists("env.py"):
    import env
# Sets up Mongdb database and hides login details in a Environment variable
app = Flask(__name__)
app.config["MONGO_DBNAME"] = 'secret_recipes'
app.config["MONGO_URI"] = os.environ.get("MONGO_URI")
app.secret_key = os.environ.get("SECRET_KEY")


mongo = PyMongo(app)

# Function used to render Home page and display all recipes
@app.route('/')
@app.route('/get_home')
def get_home():
    return render_template("home.html",
        recipes=mongo.db.recipes.find().sort("_id", -1).limit(4))


@app.route('/get_recipes')
def get_recipes():
    return render_template("recipes.html",
        recipes=mongo.db.recipes.find().sort("_id", -1))


# Function to render addrecipes page
@app.route('/add_recipe')
def add_recipe():
    return render_template('addrecipes.html',
    course=mongo.db.course.find())


# Fuction to insert recipes into the DatabaseS
@app.route('/insert_recipes', methods=['POST'])
def insert_recipes():
    recipes = mongo.db.recipes
    recipes.insert_one(request.form.to_dict())
    return redirect(url_for('get_recipes'))

# Function to render each individual recipe
@app.route('/show_recipe/<recipe_id>')
def show_recipe(recipe_id):
    return render_template("recipe.html",
            recipe=mongo.db.recipes.find_one({'_id': ObjectId(recipe_id)}))

@app.route('/show_recipes/<main>')
def show_recipes(course_type):
    return render_template("show-recipes.html",
            recipes=mongo.db.recipes.find({'course_type': course_type}))


# Function to render edit page
@app.route('/edit_recipe/<recipe_id>')
def edit_recipe(recipe_id):
    the_recipe = mongo.db.recipes.find_one({"_id": ObjectId(recipe_id)})
    all_course = mongo.db.course.find()
    return render_template('editrecipe.html', recipes=the_recipe,
                           course=all_course)

# function to POST changes to Database
@app.route('/update_recipe/<recipe_id>', methods=["POST"])
def update_recipe(recipe_id):
    recipes = mongo.db.recipes
    recipes.update({'_id': ObjectId(recipe_id)},
    {
        'recipe_name': request.form.get('recipe_name'),
        'course_type': request.form.get('course_type'),
        'recipe_serves': request.form.get('recipe_serves'),
        'recipe_time': request.form.get('recipe_time'),
        'ingredient_1': request.form.get('ingredient_1'),
        'ingredient_2': request.form.get('ingredient_2'),
        'ingredient_3': request.form.get('ingredient_3'),
        'ingredient_4': request.form.get('ingredient_4'),
        'ingredient_5': request.form.get('ingredient_5'),
        'ingredient_6': request.form.get('ingredient_6'),
        'ingredient_7': request.form.get('ingredient_7'),
        'ingredient_8': request.form.get('ingredient_8'),
        'ingredient_9': request.form.get('ingredient_9'),
        'ingredient_10': request.form.get('ingredient_10'),
        'method': request.form.get('method')

    })
    return redirect(url_for('get_recipes'))


@app.route('/delete_recipe/<recipe_id>')
def delete_recipe(recipe_id):
    mongo.db.recipes.remove({'_id': ObjectId(recipe_id)})
    return redirect(url_for('get_recipes'))


if __name__ == '__main__':
    app.run(host=os.environ.get('IP'),
            port=int(os.environ.get('PORT')),
            debug=True)


