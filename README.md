# DjangoBlog
## After checking out

Run in terminal: `pip install -r requirements.txt` whilst inside the root folder. This will give you the dependencies (there's only 3)

Then, run `cd messageboard` and type `py manage.py createsuperuser`. Follow the instructions to create your user.

Finally, run `manage.py makemigrations` followed straightaway by `manage.py migrate` which will initialise your sqlite database.

Now you can run the blog app with `py manage.py runserver`.

Log in, use the CRUD functionality, develop it however you wish. 

Cheers!
