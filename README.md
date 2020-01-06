# moviereviews
#This is a Movie review app for English movies
# This code is deployed to heroku and can be accessible at  https://warm-forest-64716.herokuapp.com
# To import the code, add 'movieapp' under INSTALLED_APPS in settings.py file
#Movie Review
=====

Movie review is a Django app to get the reviews from other review app but with a better
UI display.

Quick start
-----------

1. Add "movieapp" to your INSTALLED_APPS setting like this::

    INSTALLED_APPS = [
        ...
        'movieapp',
    ]

2. Run `python manage.py migrate` to create the movieapp models.

4. Start the development server and visit http://127.0.0.1:8000/
   to search a keyword.

5. Visit https://warm-forest-64716.herokuapp.com to view on internet.
