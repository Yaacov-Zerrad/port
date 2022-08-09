# for deploy in heroku


### link for help
https://whitenoise.evans.io/en/stable/django.html

## create a django 

## active a virtual environement
pip install sycopg2 gunicorn django-heroku dj_database_url


## create a file runtime.txt in project dossier (django-admin)

in runtime.txt write a python version example:
    python-3.10.3

## create a file Procfile without extension

in Procfile write :
    web: gunicorn <nameproject>.wsgi --log-file - 


you can find the name of you project in <yourproject/wsgi.py>

example:
    web: gunicorn core.wsgi --log-file - 

## create file requirement.txt
whit commande:
    pip freeze > requirements.txt


## in settings.py set:

#### change:
DEBUG = False
#### in  Middleware add
    "whitenoise.middleware.WhiteNoiseMiddleware",

## add this line

import django_heroku
import dj_database_url


# change the ALLOWED_HOSTS variable 

ALLOWED_HOSTS = ['<link of your site>', '127.0.0.1']

##### example:
    ALLOWED_HOSTS = ['https://yaacov-developer.herokuapp.com/', '127.0.0.1']


# add variables
STATIC_ROOT = os.path.join(BASE_DIR, 'staticsfiles')
django_heroku.settings(locals())
STATICFILES_STORAGE = "whitenoise.storage.CompressedManifestStaticFilesStorage"

# IMPORTANT 
## if static not fond 
### run commande in terminal:
python manage.py collectstatic 


# add a function for change db if you want to do maintenance in parallel else write just in os.environ

if 'DATABASE_URL' in os.environ:
    DATABASES = {
        'default': dj_database_url.parse(os.environ.get('DATABASE_URL'))
    }
else:
    print("Postgres URL not found, using sqlite instead")
    DATABASES = {
        'default': {
            'ENGINE': 'django.db.backends.sqlite3',
            'NAME': BASE_DIR / 'db.sqlite3',
        }
    }


# PREPAR FOR DEPLOY IN GIT in <project> file

git init 
git add .

