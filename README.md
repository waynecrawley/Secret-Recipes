

<div class="input-field col s12">
          <input placeholder="Recipe Name" name="recipe_name" id="recipe_name" type="text" class="validate" value="{{recipes.recipe_name}}">
          <label for="recipe_name">Recipe Name</label>
        </div>
        </div>
        
        
        <div class="input-field col s12">
          <input placeholder="How many people does it serve" name="recipe_serves" id="recipe_serves" type="text" class="validate" value="{{recipes.recipe_serves}}">
          <label for="recipe_serves">Serves</label>
        </div>

        <div class="input-field col s12">
            <select id="course" name="course_type">
            <option value="" diasabled selected>Choose your option</option>
            {% for courses in course %}
                {% if courses.course_type == recipes.course_type %}
                <option value="{{courses.course_type}}" selected >{{courses.course_type}}</option>
                {% else %}
                <option value="{{courses.course_type}}">{{courses.course_type}}</option>
                {% endif %}
            {% endfor %}
            </select>
            <label>Course Type</label>
        </div>


        <div class="input-field col s12">
          <input placeholder="How many minutes to make" name="recipe_time" id="recipe_time" type="text" class="validate" value="{{recipes.recipe_time}}">
          <label for="recipe_time">Cooking Time</label>
        </div>

        <div class="input-field col s6">
          <input placeholder="Ingredients" name="ingredient_1" id="ingredient_1" type="text" class="validate" value="{{recipes.ingredient_1}}">
          <label for="Ingredient_1">Ingredients</label>
        </div>

        <div class="input-field col s6">
          <input placeholder="Ingredients" name="ingredient_2" id="ingredient_2" type="text" class="validate" value="{{recipes.ingredient_2}}">
          <label for="Ingredient_2">Ingredients</label>
        </div>

        <div class="input-field col s6">
          <input placeholder="Ingredients" name="ingredient_3" id="ingredient_3" type="text" class="validate" value="{{recipes.ingredient_3}}">
          <label for="Ingredient_3">Ingredients</label>
        </div>

        <div class="input-field col s6">
          <input placeholder="Ingredients" name="ingredient_4" id="ingredient_4" type="text" class="validate" value="{{recipes.ingredient_4}}">
          <label for="Ingredient_4">Ingredients</label>
        </div>

        <div class="input-field col s6">
          <input placeholder="Ingredients" name="ingredient_5" id="ingredient_5" type="text" class="validate" value="{{recipes.ingredient_5}}">
          <label for="Ingredient_5">Ingredients</label>
        </div>

        <div class="input-field col s6">
          <input placeholder="Ingredients" name="ingredient_6" id="ingredient_6" type="text" class="validate" value="{{recipes.ingredient_6}}">
          <label for="Ingredient_6">Ingredients</label>
        </div>

        <div class="input-field col s6">
          <input placeholder="Ingredients" name="ingredient_7" id="ingredient_7" type="text" class="validate" value="{{recipes.ingredient_7}}">
          <label for="Ingredient_7">Ingredients</label>
        </div>

        <div class="input-field col s6">
          <input placeholder="Ingredients" name="ingredient_8" id="ingredient_8" type="text" class="validate" value="{{recipes.ingredient_8}}">
          <label for="Ingredient_8">Ingredients</label>
        </div>

        <div class="input-field col s6">
          <input placeholder="Ingredients" name="ingredient_9" id="ingredient_9" type="text" class="validate" value="{{recipes.ingredient_9}}">
          <label for="Ingredient_9">Ingredients</label>
        </div>

        <div class="input-field col s6">
          <input placeholder="Ingredients" name="ingredient_10" id="ingredient_10" type="text" class="validate" value="{{recipes.ingredient_10}}">
          <label for="Ingredient_10">Ingredients</label>
        </div>

        <div class="row">
    <form class="col s12">
      <div class="row">
        <div class="input-field col s12">
          <textarea placeholder="Cooking Instructions" id="method" name="method" class="materialize-textarea" class="validate" value="{{recipes.method}}"></textarea>
          <label for="method">Method</label>
        </div>
      </div>
      <div class="row">
            <button class="btn waves-effect waves-light" type="submit">Update
                <i class="material-icons right"></i>
             </button>
      </div>
    </form>
</div>
    </form>
    </div>
        


{% endblock %}
 

 @app.route('/show_recipes/<course_type>')
def show_recipes(course_type):
    return render_template("show-recipes.html",
            recipes=mongo.db.recipes.find({'course_type': course_type}))