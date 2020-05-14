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

![Posting Comments](https://gyazo.com/6ce976b7d37114ae6452e4bdc323e541.png)

![Posts Overview](https://gyazo.com/112c40e82643186ca8c0df6c5a8218d2.png)

![Profile Editing](https://gyazo.com/ce599ae381256edcff580f1cfcd4e40e.png)
