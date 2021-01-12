# Portfolio-website-using-django
- A simple personal portfolio website using django

- This portfolio website is fully configurable or customizable

- You can perform any CRUD operation without being able to republish the app

- This project is developed with the motto  ```Deploy once time; customize many time```

# Live Demo

[https://jebaseelan.herokuapp.com/](https://jebaseelan.herokuapp.com/)

## Installation procedure

```shell script

# clone the repo

$ git clone https://github.com/Jebaseelanravi/Portfolio-website-using-django.git

$ cd Portfolio-website-using-django

# install dependencies

$ pip install -r requirements.txt

# create tables

$ python manage.py migrate

$ python manage.py createsuperuser

# Launch the servers

$ python manage.py runserver
```

You can see your website [here](http://127.0.0.1:8000/)

Please login into [Django admin site](http://127.0.0.1:8000/admin/) using the superuser credential  and add your own projets/profile details, blogs,skills etc.



# Publish the website in Heroku

You can then publish you app to heroku and share with friends  