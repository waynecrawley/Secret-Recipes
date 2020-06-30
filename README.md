<img src="https://codeinstitute.s3.amazonaws.com/fullstack/ci_logo_small.png" style="margin: 0;">

Welcome waynecrawley,

This is the Code Institute student template for Gitpod. We have preinstalled all of the tools you need to get started. You can safely delete this README.md file, or change it for your own project.

## Gitpod Reminders

To run a frontend (HTML, CSS, Javascript only) application in Gitpod, in the terminal, type:

`python3 -m http.server`

A blue button should appear to click: *Make Public*,

Another blue button should appear to click: *Open Browser*.

To run a backend Python file, type `python3 app.py`, if your Python file is named `app.py` of course.

A blue button should appear to click: *Make Public*,

Another blue button should appear to click: *Open Browser*.

In Gitpod you have superuser security privileges by default. Therefore you do not need to use the `sudo` (superuser do) command in the bash terminal in any of the backend lessons.

## Updates Since The Instructional Video

We continually tweak and adjust this template to help give you the best experience. Here are the updates since the original video was made:

**April 16 2020:** The template now automatically installs MySQL instead of relying on the Gitpod MySQL image. The message about a Python linter not being installed has been dealt with, and the set-up files are now hidden in the Gitpod file explorer.

**April 13 2020:** Added the _Prettier_ code beautifier extension instead of the code formatter built-in to Gitpod.

**February 2020:** The initialisation files now _do not_ auto-delete. They will remain in your project. You can safely ignore them. They just make sure that your workspace is configured correctly each time you open it. It will also prevent the Gitpod configuration popup from appearing.

**December 2019:** Added Eventyret's Bootstrap 4 extension. Type `!bscdn` in a HTML file to add the Bootstrap boilerplate. Check out the <a href="https://github.com/Eventyret/vscode-bcdn" target="_blank">README.md file at the official repo</a> for more options.

--------

{% for ingreds in recipes %}
        {{ingreds.recipe_name}}
        {{ingreds.recipe_serves}}
        {{ingreds.recipe_time}}
        {{ingreds.recipe_difficulty}}

Happy coding!

 <div class="input-field col s12">
            <select id="recipe_serves">
            <option value="" selected>Choose your option</option>
            <option value="1"> 1 person</option>
            <option value="2"> 2 people</option>
            <option value="3"> 3 people</option>
            <option value="4"> 4 people</option>
            </select>
            <label for="recipe_serves">Serves</label>
        </div>

        <div class="row">
        <div class="input-field col s12">
          <input placeholder="Enter cooking time" id="recipe_time" type="text" class="validate">
          <label for="recipe_time">Cooking Time</label>
        </div>
        </div>

         <div class="input-field col s12">
            <select id="recipe_difficulty">
            <option value="" selected>Choose your option</option>
            <option value="1"> Easy</option>
            <option value="2"> Medium</option>
            <option value="3"> Hard</option>
            
            </select>
            <label for="recipe_difficulty">Difficulty</label>
        </div>

        <div class="input-field col s6">
          <input placeholder="Ingredients" id="ingredient_1" type="text" class="validate">
          <label for="Ingredient_1">Ingredients</label>
        </div>
        <div class="input-field col s6">
          <input placeholder="Ingredients" id="ingredient_2" type="text" class="validate">
          <label for="Ingredient_2">Ingredients</label>
        </div>

        <div class="input-field col s6">
          <input placeholder="Ingredients" id="ingredient_3" type="text" class="validate">
          <label for="Ingredient_3">Ingredients</label>
        </div>
        <div class="input-field col s6">
          <input placeholder="Ingredients" id="ingredient_4" type="text" class="validate">
          <label for="Ingredient_4">Ingredients</label>
        </div>

        <div class="input-field col s6">
          <input placeholder="Ingredients" id="ingredient_5" type="text" class="validate">
          <label for="Ingredient_5">Ingredients</label>
        </div>
        <div class="input-field col s6">
          <input placeholder="Ingredients" id="ingredient_6" type="text" class="validate">
          <label for="Ingredient_6">Ingredients</label>
        </div>

        <div class="input-field col s6">
          <input placeholder="Ingredients" id="ingredient_7" type="text" class="validate">
          <label for="Ingredient_7">Ingredients</label>
        </div>
        <div class="input-field col s6">
          <input placeholder="Ingredients" id="ingredient_8" type="text" class="validate">
          <label for="Ingredient_8">Ingredients</label>
        </div>

        <div class="input-field col s6">
          <input placeholder="Ingredients" id="ingredient_9" type="text" class="validate">
          <label for="Ingredient_9">Ingredients</label>
        </div>
        <div class="input-field col s6">
          <input placeholder="Ingredients" id="ingredient_10" type="text" class="validate">
          <label for="Ingredient_10">Ingredients</label>
        </div>

        <div class="row">
            <form class="col s12">
                <div class="row">
                    <div class="input-field col s12">
                     <textarea id="recipe_howtocook" class="materialize-textarea"></textarea>
                     <label for="textarea1">How To Cook</label>
                    </div>
                </div>
            </form>
        </div>
