======================
cookiecutter-drf-ekman
======================

A properly structured (Two Scoops of Django) Django REST Framework cookiecutter template with a JSON Web Token (JWT) based authentication system.

Usage
-----

Install **cookiecutter**::

    $ pip install cookiecutter

Run cookiecutter against this repo::

    cookiecutter https://github.com/joakimekman/cookiecutter-drf-ekman

Answer the questions prompted to you, and a project will be created.

Then, cd into the project::
  
  $ cd project_name
  
Install requirements::
  
  $ pip install -r requirements.txt
  
Create an **.env** file at root, and define your **SECRET_KEY** and **DB_PASS**.

Customize the user models, and migrate.

At last, create a git repo and push it there::
  
  $ git init
  $ git add .
  $ git commit -m "first commit"
  $ git remote add origin https://github.com/username/project_name.git
  $ git push -u origin master
  
Due to the template structure, each app that you create should reside in the 2nd project directory::

  $ cd project_name
  $ python ../manage.py startapp myapp
  
Make sure to add the correct path to **apps.py** of each created app::
 
  class MyAppConfig(AppConfig):
    name = "**my_project.**myapp"
 
**Before use:** Check for expected behavior by hitting the API endpoints with Postman.