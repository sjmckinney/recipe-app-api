# recipe-app-api
API for recipe app

Build standalone docker image

`docker build .`

Build docker images referenced in `docker-compose.yml`

`docker-compose build`

To create a Django project within `app` folder in images

`docker-compose run app sh -c "django-admin.py startproject app`

Run tests in terminal

`docker-compose run app sh -c "python manage.py test"`

Add new "app" to existing project

`docker-compose run app sh -c "python manage.py startapp core"`

Create migrations (needs to be rerun every time a model is added or amended)

`docker-compose run app sh -c "python manage.py makemigrations core"`
