# User-API
In this project I have implemented django rest framework to get some data via API's. I have implemented functionality of GET, PUT, POST, DELETE and to POST multiple JSON data at once.
I have used Postgresql database and have deployed it on heroku.
Link - https://tomarji-api-wale.herokuapp.com/api/users/

# How to setup

## Step - 1
You have to fork this repo and clone it, for this
You can see the `fork` option on the top right corner, after that you'll see an option to `clone` this repo, you have to copy the URL and go to the local folder you want this project to get saved and open it in terminal then run `git clone "URL you copied"`

## Step - 2
It's advised to create a virtual environment so that the project dependencies dosent get installed in the main system, So for this run 
- `pip install virtualenv`
- `virtualenv env_name`
- `pip install requirements.txt`
This will install all the dependencies.

## Step - 3
Run
`python manage.py runserver`

All set and you are ready to go.

# This is home page.
![Alt text](/images/home-page.png?raw=true "Title")

# This is /api/users page
![Alt text](/images/home-page.png?raw=true "Title")

# You can get data with query parameters
![Alt text](/images/query-parameter.png?raw=true "Title")

# This is single user detail page with id
![Alt text](/images/single-user.png?raw=true "Title")

# This page will help you to send multiple JSON data at once to save in database
![Alt text](/images/multiple-users-at-once.png?raw=true "Title")

# This is the modified django admin page

You can create a superuser to login to admin page by - 
`python manage.py createsuperuser` and add all details

![Alt text](/images/admin-pannel.png?raw=true "Title")