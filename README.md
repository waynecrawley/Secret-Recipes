# Secret-Recipes
![]()
### Introduction

## UX
The website was built with a mobile first approach. The client wanted a website that was easy to use and simple to navigate
### User Stories

**As a** New Visitor  
**I want** the website to be easy to navigate   
**So that** It’s easy to find Latest Recipes 

**As a** New Visitor   
**I want**  to see all recipes avaialble
**So that**  I have a good variety to view

**As a** Returning Visitor  
**I want** to be able to add new recipes   
**So that** i can share my recipes with the world 

### Strategy
 + This project is for the creation of a website for Secret Recipes to help people share recipes and also  that is visually pleasing and has an ease of use.

### Scope
+ The website should be responsive, work on all devices and browsers. The website must consist of , recipes, be able to add,edit and delete recipes.
### Structure
+ The overall structure of the website is that of a branching structure.

![](https://github.com/waynecrawley/Secret-Recipes/blob/master/static/images/flowchart.png)
### Skeleton

#### Wireframes
+ [index.html Wireframes for Mobile and Tablet](https://github.com/waynecrawley/Secret-Recipes/blob/master/static/images/recipemobileandtablet.png)
+ [index.html Wireframes for Desktop](https://github.com/waynecrawley/Secret-Recipes/blob/master/static/images/desktopview.png)

### Surface

+ A Mostly black and white colour theme was used for this website, which showcases the classic professional look. 


# FEATURES
### Existing Features
+ **Navbar** - A Navbar is available which links to  all sections of the webpage
  * On Mobile these links are hidden in a sidenav for better functionality.
+ **Add Recipe Button** - The add recipe button is featured on the home page on Mobile and tablet to take the user directly to the form to add recipes.
+ **Materialize cards** - Materialize cards were used to house the recipes title and imamges on the home and all recipes pages.
+ **Form** - A form was used to make for the user to be able to add and edit data to the database.

### Features Left to Implement

## Technologies Used
### Frontend
+ **HTML** - This is the Markup Language used to create the main structure of the website.
+ **CSS** - I used CSS to style the visual look of the webpage.
+ **jQuery** -[jQuery](https://jquery.com/) used to help Materializecss Intialization

### Backend
+ **MongoDB** - [MongoDB](https://www.mongodb.com/cloud/atlas) was the database used
+ **FLask** - [Flask] Flask is the micro web framework i used thats written in Python.
+ **Jinja2** - [Jinja2] The templating language used for python


### Other technologies used
+ **Gitpod** - [Gitpod](https://www.gitpod.io/) was the only IDE I used throughout development.
+ **Git** -  [Git](https://git-scm.com/) was used for version control.
+ **GitHub** - [Github](https://github.com/) was used to host the repository for this project.
+ **Heroku** - [Heorku] (www.heroku.com) was used for deployment of the webapp.




## Testing
+ During development I used CRUD to make sure the database was fully functional before proceding with any further design process.
+ I then, worked through my user stories to make sure my website reached all the requirements of my user stories, before moving on to the more technical testing.
+ I ran the HTML for all pages through [W3C HTML Markup Validation](https://validator.w3.org/) by direct input. - **Working as intended**
+ I ran the CSS through [W3C CSS Validation Service](http://www.css-validator.org/) by direct input. - **Working as intended**
+ All links tested manually - **Working as intended**
+ All buttons tested manually - **Working as intended**
+ Tested different screen sizes using Google Developer Tools.
  * Pixel 2 - **Working as intended**
  * iPhone 6 - **Working as intended**
  * iPhone 7 - **Working as intended**
  * iPhone 8 - **Working as intended**
  * iPhone X - **Working as intended**
  * iPad - **Working as intended**
  * iPad Pro  - **Working as intended**
  * Laptop with HiDPI screen 

+ I got friends to test out the live site on Heroku and give me Feedback on any issues. 
+ I used my Huwawei P20 smart Android Phone to test website - **Working as intended**
+ The website was tested on different browsers such as Google Chrome, Safari, Internet Explorer and Mozilla Firefox.

### Issues fixed 
+ On the update recipe form. The Iamge was not updating to the database. This was fixed by adding one line to the update_recipe route. 
'image': request.form.get('image'),

## Deployment
+ This Website was developed using [Gitpod](https://www.gitpod.io/). I commited to Git and Pushed to [Github](https://github.com/)

 I also pushed to heroku using the command line.
### How to Deploy

### How to Deploy Locally

## Credits
### Content

### Media

### Acknowledgements

+ I would like to thank my Mentor who has been a fantastic guidence for me.
+ Tutor support when ever i reached out were fantastic.
+ I would just like to thank all my fellow Code Institute students on Slack, who have been a great
help along the way.
