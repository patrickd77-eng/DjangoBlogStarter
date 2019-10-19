# DjangoBlog
A simple blog with CRUD functionality. Runs on Django. Great starter kit.

## After checking out

1. Run in terminal: `pip install -r requirements.txt` whilst inside the root folder. This will give you the dependencies (there's only 3)

2. Then, run `cd messageboard` and type `py manage.py createsuperuser`. Follow the instructions to create your user.

3. Finally, run `manage.py makemigrations` followed straightaway by `manage.py migrate` which will initialise your sqlite database.

4. Now you can run the website with `py manage.py runserver`.

Log in, use the CRUD functionality, develop it however you wish. 

Cheers!

### Using Python 3.7.x and Django 2.x


## NOTE

The site has full privacy (you can only see posts if logged in. only admins can make posts.)

This can be removed by simply changing the {% if user.is_authenticated %} tags used in the HTML templates.

[![Watch a video demo](https://gyazo.com/aa53a7529104172eff4027d24bd0e7b9)](https://gyazo.com/aa53a7529104172eff4027d24bd0e7b9)
